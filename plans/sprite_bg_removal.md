# Sprite Background Removal — Process Notes

How to detect and remove baked-in checkerboard backgrounds from AI-generated character sprites.

---

## The Problem

AI image generators frequently save sprites with the transparency-indicator **baked in as pixels**. The grey-and-white checkerboard that image editors show to indicate "this area is transparent" gets written into the file as actual RGB pixel data rather than alpha-channel transparency. The image may even be saved in RGBA format with the alpha channel fully set to 255 (opaque) everywhere, making the checkerboard invisible to tools that only check the mode.

What you see in-game: a large horizontal band of grey-and-white squares overlaid on the scene background wherever the sprite's non-character area would otherwise be transparent.

---

## Detecting the Problem

Run this Python snippet on any suspect sprite:

```python
from PIL import Image

img = Image.open("sprite.png").convert("RGBA")
w, h = img.size
px = img.load()

# Corners should be fully transparent (alpha = 0) if the background was removed
corners = [px[0,0], px[w-1,0], px[0,h-1], px[w-1,h-1]]
print("Corner alpha values:", [c[3] for c in corners])

# Check edge area for opaque grey/white pixels
edge_opaque = 0
for y in range(0, h, 8):
    for x in range(0, min(w//6, 100), 8):
        if px[x,y][3] > 10:
            edge_opaque += 1
print("Opaque samples in left edge:", edge_opaque, "(> 3 = likely background baked in)")
```

Or run the batch scanner:

```bash
python3 << 'EOF'
from PIL import Image
import os

sprites_dir = 'cimarron/game/images/sprites'
for fname in sorted(os.listdir(sprites_dir)):
    if not fname.endswith('.png') or '/' in fname:
        continue
    img = Image.open(os.path.join(sprites_dir, fname)).convert('RGBA')
    w, h = img.size; px = img.load()
    if img.mode == 'RGB':
        print(f"RGB (no alpha channel): {fname}")
    elif px[0,0][3] > 10:
        print(f"Non-transparent corner: {fname}")
EOF
```

---

## Background Type Taxonomy

Three types of baked-in backgrounds appear across these sprites, each needing a slightly different fix:

### Type A — Solid flat background (RGB mode, no alpha)
The file has no alpha channel at all. The background is a solid color (usually white, light grey, or medium grey).

**How to spot it:** `Image.mode == 'RGB'`

**Fix:** ImageMagick flood fill from 4 corners with appropriate fuzz:
```bash
convert input.png -alpha set -fuzz 12% -fill none \
    -draw "color 0,0 floodfill" \
    -draw "color $((W-1)),0 floodfill" \
    -draw "color 0,$((H-1)) floodfill" \
    -draw "color $((W-1)),$((H-1)) floodfill" \
    output.png
```
(Replace `$((W-1))` and `$((H-1))` with the actual pixel dimensions minus 1.)

**Limitation:** Only works if both checkerboard colors are within `fuzz`% of the corner color. A 12-pixel-tile checkerboard alternating dark grey (~75) and medium grey (~140) will only have one color removed per pass — the other color remains as isolated tiles.

---

### Type B — Tiled checkerboard (RGBA with two alternating tile colors, ~12×12 px tiles)
The image is RGBA but the background area has alternating solid color blocks (typically ~12×12 pixel tiles). Each tile is uniformly one of two achromatic grey values.

**How to spot it:** Corners may already be partially transparent (one tile was cleaned), but large regions of the image still look like a visible checker grid. Both the grey AND the "opposite" color remain opaque in the background.

**Fix:** Apply the achromatic pixel removal script (see below). Both background colors are achromatic (R ≈ G ≈ B) and in the mid-grey range, while character pixels have color (skin, clothing) or are very dark/very light.

---

### Type C — Anti-aliased or 1-pixel checkerboard (RGBA with pixel-by-pixel alternation)
The background alternates color at the individual pixel level — every pixel is different from its 4-connected neighbors. Flood fill cannot spread through this pattern at all (each pixel's neighbors are a different color, outside fuzz tolerance from the starting pixel).

**How to spot it:** A large flood fill from the corner produces almost no change, leaving nearly the entire image opaque.

**Fix:** Same achromatic pixel removal script as Type B.

---

## The Fix

### Step 1 — Convert RGB to RGBA (only for Type A)

```bash
SPRITES_DIR="cimarron/game/images/sprites"

process_sprite() {
    local f="$1"
    local path="$SPRITES_DIR/$f"
    local dims=$(python3 -c "from PIL import Image; img=Image.open('$path'); print(img.size[0]-1, img.size[1]-1)")
    local w=$(echo $dims | cut -d' ' -f1)
    local h=$(echo $dims | cut -d' ' -f2)
    convert "$path" -alpha set -fuzz 12% -fill none \
        -draw "color 0,0 floodfill" \
        -draw "color ${w},0 floodfill" \
        -draw "color 0,${h} floodfill" \
        -draw "color ${w},${h} floodfill" \
        "$path"
}
export -f process_sprite
export SPRITES_DIR
echo "sprite1.png sprite2.png ..." | tr ' ' '\n' | xargs -P 8 -I{} bash -c 'process_sprite "$@"' _ {}
```

This initial flood fill handles sprites where one background color is directly connected from corner to corner. Leaves isolated tiles of the other color — clean those up with Step 2.

### Step 2 — Achromatic grey removal

Save this as `/tmp/fix_sprites.py`:

```python
from PIL import Image
import sys, os

def fix_sprite(path):
    img = Image.open(path).convert('RGBA')
    w, h = img.size
    pixels = img.load()
    removed = 0

    def is_bg_color(r, g, b):
        """Achromatic grey/white — all three channels similar, any brightness."""
        return max(r, g, b) - min(r, g, b) < 20 and (r + g + b) // 3 > 50

    def all_neighbors_bg_or_transparent(x, y):
        for nx, ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if 0 <= nx < w and 0 <= ny < h:
                np = pixels[nx, ny]
                if np[3] > 0 and not is_bg_color(np[0], np[1], np[2]):
                    return False
        return True

    # Pass 1: remove achromatic grey in the typical background range (50–170)
    # Safe: character dark clothing is < 50, character skin is not achromatic
    for y in range(h):
        for x in range(w):
            p = pixels[x, y]
            if p[3] == 0:
                continue
            r, g, b = p[0], p[1], p[2]
            spread = max(r, g, b) - min(r, g, b)
            avg = (r + g + b) // 3
            if spread < 18 and 50 < avg < 170:
                pixels[x, y] = (r, g, b, 0)
                removed += 1

    # Pass 2: remove lighter grey / white (170+) only if all opaque neighbors
    # are also achromatic grey — i.e. the pixel is isolated from character pixels.
    # This preserves grey hair and light trim connected to the body.
    for y in range(h):
        for x in range(w):
            p = pixels[x, y]
            if p[3] == 0:
                continue
            r, g, b = p[0], p[1], p[2]
            spread = max(r, g, b) - min(r, g, b)
            avg = (r + g + b) // 3
            if spread < 20 and avg >= 170:
                if all_neighbors_bg_or_transparent(x, y):
                    pixels[x, y] = (r, g, b, 0)
                    removed += 1

    img.save(path)
    return removed

sprites_dir = 'cimarron/game/images/sprites'
for fname in sys.argv[1:]:
    path = os.path.join(sprites_dir, fname)
    removed = fix_sprite(path)
    print(f"  {fname}: {removed} pixels removed")
```

Run it:
```bash
python3 /tmp/fix_sprites.py \
  felice_neutral.png lewis_neutral.png yancey_neutral.png \
  sol_neutral.png ...
```

Takes ~3–5 seconds per sprite in Python without numpy. Run in parallel with `xargs -P 8` if doing many at once.

---

## Color Safety Notes

The achromatic removal is designed around the observation that background checkerboards are **grey with no color bias** (R ≈ G ≈ B), while character pixels either:
- Have color (warm skin tones, colored clothing) — non-achromatic, high spread → safe
- Are very dark (dark clothing, hair < value 50) — below threshold → safe
- Are very bright (white lace, bright highlights > value 230) — only removed if isolated

**Characters at risk:**
- **Grey hair** (e.g. Mr. Venable): Pass 2 will remove isolated interior grey-hair pixels but preserve those adjacent to face/skin because `all_neighbors_bg_or_transparent` returns False when a neighbor has skin color. Result: thin grey at hair boundary remains. At 45% sprite zoom in-game this is acceptable; if fidelity is needed, fix manually.
- **Light grey clothing** (e.g. neutral suits): Same pass-2 behavior — edges preserved, interior may be thinned.
- **White accessories** (collars, cuffs): Same. The lace border connecting to the character body is preserved; isolated white pixels (background remnants) are removed.

---

## Verification

After running the fix, confirm with:

```bash
python3 << 'EOF'
from PIL import Image
import os

sprites_dir = 'cimarron/game/images/sprites'
for fname in sorted(os.listdir(sprites_dir)):
    if not fname.endswith('.png') or '/' in fname:
        continue
    img = Image.open(os.path.join(sprites_dir, fname)).convert('RGBA')
    w, h = img.size; px = img.load()
    edge_opaque = sum(
        1 for y in range(0, h, 8)
        for x in list(range(0, min(w//6, 100), 8)) + list(range(max(0, w-100), w, 8))
        if px[x,y][3] > 10
    )
    if edge_opaque > 10:
        print(f"Still has edge pixels: {fname} ({edge_opaque} samples)")
print("Scan complete.")
EOF
```

Edge pixel counts > 10 in the left or right sixth of the image indicate remaining background. Counts of 1–10 are usually character overlap at the image edge — visually inspect before re-processing.

---

## Full Batch Run (from scratch)

If starting fresh with a new set of sprites:

```bash
# 1. Identify which need fixing
python3 << 'SCAN'
from PIL import Image
import os
for fname in sorted(os.listdir('cimarron/game/images/sprites')):
    if not fname.endswith('.png') or '/' in fname:
        continue
    img = Image.open(f'cimarron/game/images/sprites/{fname}')
    if img.mode == 'RGB':
        print(f"RGB:  {fname}")
    elif img.convert('RGBA').getpixel((0,0))[3] > 10:
        print(f"RGBA opaque corner:  {fname}")
SCAN

# 2. For RGB sprites: flood fill pass (ImageMagick, parallelized)
#    [use the batch script from Step 1 above]

# 3. For all sprites with baked-in backgrounds: achromatic pass
python3 /tmp/fix_sprites.py sprite1.png sprite2.png ...

# 4. Verify
#    [use the verification script above]
```

---

## Tools Required

- **ImageMagick 6.x** (`convert`) — flood fill step. `sudo apt install imagemagick`
- **Python 3 + Pillow** — achromatic removal step. Pillow: `sudo apt install python3-pil`
- No numpy, scipy, or rembg required.

If `rembg` is available (`pip install rembg`), it provides AI-based background removal that handles all three types in one pass with no color tuning needed:
```bash
rembg p cimarron/game/images/sprites/ cimarron/game/images/sprites/
```
But it requires internet access to download the model on first run and is significantly slower per image.
