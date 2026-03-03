# Cimarron: Chapter One — Ren'Py Project

A visual novel based on *Cimarron* by Edna Ferber (1929).

---

## How to Run

1. **Download Ren'Py** from https://www.renpy.org/ (free, Windows/Mac/Linux).
2. Open the Ren'Py launcher.
3. Click **"Open Project"** and navigate to this folder (`cimarron_chapter1/`).
4. Click **"Launch Project"** to play.

---

## Project Structure

```
cimarron_chapter1/
├── game/
│   ├── script.rpy        ← All 7 scenes, dialogue, and choices
│   ├── characters.rpy    ← Character definitions and colors
│   ├── variables.rpy     ← Game state (relationship meter, character direction)
│   ├── options.rpy       ← Project settings (title, screen size, transitions)
│   ├── gui.rpy           ← Visual theme (colors, fonts, layout)
│   ├── images/           ← Backgrounds and character sprites (add files here)
│   │   └── sprites/
│   ├── audio/            ← Music tracks (add .ogg files here)
│   └── gui/              ← GUI images (textbox, buttons — add .png files here)
└── README.md             ← This file
```

---

## Assets You Need to Add

The script references image and audio files that you must source and place in the
correct folders. The game will run without them (Ren'Py shows a placeholder), but
adding art and music makes it a real experience.

### Background Images

Place `.jpg` or `.png` files in `game/images/`:

| Filename | Description | AI Prompt Suggestion |
|---|---|---|
| `bg_venable_home.jpg` | Elegant 1889 Kansas parlor, Sunday dinner | "Victorian parlor 1889, mahogany table, Sunday dinner, warm candlelight, oil painting style" |
| `bg_land_run.jpg` | The Oklahoma Land Run, April 22 1889 | "Oklahoma Land Run 1889, thousands of settlers racing across open prairie, dramatic sky, painted illustration" |
| `bg_wagon_trail.jpg` | Prairie wagon trail, red clay Oklahoma | "Prairie wagon trail 1889, red clay Oklahoma, vast sky, two covered wagons, impressionist painting" |
| `bg_osage_tent_town.jpg` | Boom town tents and mud, Osage 1889 | "Oklahoma boom town 1889, tents and mud streets, frontier chaos, painted illustration" |
| `bg_wigwam_office.jpg` | Canvas tent with printing press inside | "1889 frontier newspaper tent office, hand printing press, oil lamps, letterpress type cases" |
| `bg_journal.jpg` | Parchment paper journal page | "Aged parchment journal page, sepia, handwritten, Victorian era, soft lighting" |

**Free AI image tools**: Adobe Firefly (free tier), DALL-E 3 (via ChatGPT Plus), or
Midjourney. Search itch.io for "western visual novel backgrounds" for ready-made packs.

### Character Sprites

Place `.png` files (transparent background) in `game/images/sprites/`:

| Filename | Character |
|---|---|
| `yancey_neutral.png` | Yancey Cravat — tall, dark-haired, Prince Albert coat |
| `sabra_neutral.png` | Sabra Cravat — young, dark-haired, gray cheviot dress |
| `sol_neutral.png` | Sol Levy — small, quiet man in a black coat |
| `felice_neutral.png` | Mrs. Venable — imperious, gray-haired, matriarchal |
| `lewis_neutral.png` | Mr. Venable — frail, fine-featured, gentle |
| `stranger_neutral.png` | Frontier stranger — sunburned, bearded |

**Sprite options**:
- Generate with AI (Midjourney, Adobe Firefly) — ask for "visual novel sprite, transparent background"
- Search itch.io for "western VN sprites" or "historical character sprites"
- Use silhouette-style sprites (all black with colored outlines) if portrait art isn't ready

### Music

Place `.ogg` files in `game/audio/`:

| Filename | Mood |
|---|---|
| `wichita_parlor.ogg` | Refined, Victorian parlor ambience — piano, quiet strings |
| `frontier_theme.ogg` | Open frontier feeling — folk guitar, fiddle, wide and lonely |

**Free music sources**:
- https://freemusicarchive.org — search "western folk" or "frontier"
- https://itch.io — search "western RPG OST" or "frontier music pack"
- https://opengameart.org — search "western" or "americana"

All three sites offer royalty-free music. Download as `.mp3` and convert to `.ogg`
using [Audacity](https://www.audacityteam.org/) (free).

---

## Fonts (Optional but Recommended)

Download from **Google Fonts** and place `.ttf` files in `game/fonts/`:

- **Playfair Display** (narration and names) — search "Playfair Display" on fonts.google.com
- **IM Fell English** (UI menus) — search "IM Fell English" on fonts.google.com

Then uncomment the font lines in `game/gui.rpy`.

---

## Game Mechanics

### Yancey Relationship Meter (`yancey_relationship`)
- Starts at 50 (out of 100)
- Goes up when Sabra supports Yancey's vision or shows warmth
- Goes down when Sabra stays distant or guarded
- Affects the end-of-chapter summary tone

### Sabra's Character Direction (`sabra_direction`)
- Starts at 0
- Positive = Frontier Woman track (bold, adaptive)
- Negative = Refined Lady track (composed, cautious)
- Affects available dialogue in future chapters

### Journal Entries
- Appear at the end of each scene
- Summarize Sabra's emotional state in her own voice
- Function as a recap and character development device

---

## Scenes

| Scene | Location | Key Choice |
|---|---|---|
| 1. The Venable Home | Wichita parlor | How Sabra reacts to Yancey's storytelling |
| 2. The Land Run | Flashback | Does she admire or fear his idealism? |
| 3. The Decision | Venable dining room | Confront mother / stand behind Yancey / private doubt |
| 4. The Journey West | Wagon trail | Does she open up to the frontier? |
| 5. Arriving at Osage | Osage tent town | First confrontation with a rough frontier character |
| 6. The Oklahoma Wigwam | Newspaper tent | How she responds to danger |
| 7. End of Chapter | Osage / epilogue | Reflection — what was gained, what was lost |

---

## Extending the Game

To add more expressions to character sprites (happy, worried, angry):
1. Add more sprite files: `yancey_happy.png`, `yancey_worried.png`, etc.
2. In `script.rpy`, change `show yancey neutral` to `show yancey happy` at the
   appropriate moments.

To add sound effects:
1. Place `.ogg` files in `game/audio/`
2. Add `play sound "audio/yourfile.ogg"` in `script.rpy`

---

*Based on Cimarron by Edna Ferber (1929) — public domain in the United States.*
