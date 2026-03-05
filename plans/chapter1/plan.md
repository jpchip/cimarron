# Cimarron — Chapter 1 Game Plan

## Context

The source material is *Cimarron* by Edna Ferber (1929), an epic historical novel about the Oklahoma Land Run of 1889. The player controls Sabra Cravat, a refined Southern belle who is pulled into frontier life by her charismatic husband Yancey. Chapter 1 covers the Wichita home scene through the founding of Osage, Oklahoma — establishing the world, characters, and the central tension of civilization vs. frontier.

The user is a beginner with no strong tech preference, targeting a Chapter 1 MVP.

---

## Recommendation: Visual Novel in Ren'Py

**Why Ren'Py over the alternatives:**

| Option | Fit | Reason |
|---|---|---|
| Text-based (Twine) | Fair | Too limited visually; no dialogue portraits or music |
| 2D RPG (RPGJS) | Poor | Combat mechanics don't fit; art pipeline is heavy for a beginner |
| Point-and-click (Godot) | Good | Strong visual storytelling, but steeper learning curve |
| **Visual Novel (Ren'Py)** | **Best** | Purpose-built for dialogue-heavy, choice-driven stories; beginner-friendly Python-like scripting; exports to web |

Ren'Py strengths for this project:
- Built-in dialogue, choices, character sprites, backgrounds, music, save/load, rollback
- Beginner-friendly scripting (`.rpy` files, simple syntax)
- Free export to Windows / Mac / Linux / Web (HTML5)
- Large community with free asset packs for historical/western themes
- The novel's literary prose translates directly into narration boxes

---

## Chapter 1 Scene Structure

### Scene 1 — The Venable Home (Wichita, Kansas)
- Setting: Refined Southern home, family gathered at dinner
- Yancey arrives dramatically, larger than life
- Yancey narrates the Land Run to the assembled family
- **Player choices**: How does Sabra react? (Wide-eyed admiration / Quiet skepticism / Polite reserve)
- Sets up the Yancey Relationship meter

### Scene 2 — The Land Run Flashback
- Cinematic narration: Yancey's account of April 22, 1889
- The woman in black tights on the thoroughbred — Yancey gives up his claim
- Sabra listens and privately reacts
- **Player choices**: Does Sabra admire his idealism or find it reckless?

### Scene 3 — The Decision
- Felice Venable (Sabra's mother) opposes the move fiercely
- Yancey announces they are leaving for Oklahoma Territory
- **Player choices**: Does Sabra confront her mother? Stand behind Yancey? Express private doubts?
- Choice affects Yancey Relationship and Sabra's starting "frontier toughness" stat

### Scene 4 — The Journey West
- Wagon trail narration with vignette moments
- First taste of the frontier's danger and beauty
- Conversation with Yancey about his vision for Oklahoma
- **Player choices**: Does Sabra open up to Yancey's dream, or stay guarded?

### Scene 5 — Arriving at Osage
- Culture shock: mud, tents, saloons, chaos
- Introduction to Sol Levy (the Jewish merchant) — quiet, sad-eyed, perceptive
- Introduction to Isaiah (young servant who followed them)
- **Player choice**: First interaction with a rough frontier character — how does Sabra handle it?

### Scene 6 — Building the Oklahoma Wigwam (Newspaper)
- Setting up the print press in a tent
- Yancey writes the first editorial; Sabra helps typeset
- A crisis arrives: a local gunfight or threat to the paper
- **Player choice**: How does Sabra respond to the first real danger?

### Scene 7 — End of Chapter 1
- Osage has its first church service (held in a gambling tent)
- A moment of quiet between Sabra and Yancey — what was gained, what was lost
- Journal entry: Sabra writes to her mother
- End-of-chapter summary of relationship status and character direction

---

## Key Game Mechanics

### Yancey Relationship Meter
- Tracks trust/tension between Sabra and Yancey
- Affected by dialogue choices throughout Chapter 1
- High trust → warm dialogue, Yancey confides in Sabra
- High tension → Yancey is distant, Sabra feels more alone

### Sabra's Character Direction
- Two implicit tracks (not shown as a bar): **Refined Lady** vs. **Frontier Woman**
- Choices shift Sabra's narration voice and dialogue options in later chapters
- By end of Chapter 1, the game reflects which direction she's heading

### Sabra's Journal
- Unlocked at end of each scene
- Brief entry written from Sabra's perspective summarizing her emotional state
- Functions as a recap and character depth device

### Narration + Dialogue
- Third-person literary narration (preserves Ferber's prose style)
- Character dialogue with portrait sprites
- Choices are presented as Sabra's internal thoughts → external actions

---

## Technical Implementation Plan

### Step 1: Install Ren'Py
- Download from https://www.renpy.org/ (free, Windows/Mac/Linux)
- Create a new project: `cimarron_chapter1`

### Step 2: Project Structure
```
cimarron_chapter1/
├── game/
│   ├── script.rpy          # Main story script
│   ├── characters.rpy      # Character definitions
│   ├── variables.rpy       # Game state variables
│   ├── images/             # Backgrounds and character sprites
│   │   ├── bg_venable_home.jpg
│   │   ├── bg_wagon_trail.jpg
│   │   ├── bg_osage_tent_town.jpg
│   │   ├── bg_wigwam_office.jpg
│   │   └── sprites/
│   │       ├── yancey_neutral.png
│   │       ├── sabra_neutral.png
│   │       └── sol_levy.png
│   ├── audio/              # Music and sound
│   │   ├── frontier_theme.ogg
│   │   └── wichita_parlor.ogg
│   └── gui/                # UI customization (fonts, colors)
```

### Step 3: Define Characters and Variables
```python
# characters.rpy
define sabra = Character("Sabra", color="#8B4513")
define yancey = Character("Yancey", color="#2F4F4F")
define sol = Character("Sol Levy", color="#556B2F")
define felice = Character("Mrs. Venable", color="#800000")

# variables.rpy
default yancey_relationship = 50    # 0-100
default sabra_direction = 0         # negative = Refined, positive = Frontier
```

### Step 4: Write the Script (script.rpy)
- Each scene is a Ren'Py label block
- Use `menu:` for player choices
- Use `$ yancey_relationship += 10` to track meter changes
- Narration uses the literary style of Ferber's prose

### Step 5: Source Art Assets
**Beginner-friendly free sources:**
- **Backgrounds**: Generate with AI tools (Adobe Firefly, DALL-E, Midjourney) — prompt for "1889 Oklahoma frontier town, painted style" etc. Or use public domain historical photos.
- **Character sprites**: Use Ren'Py's default sprite library, or generate with AI. Silhouette-style is also effective and easier.
- **Music**: Free on itch.io (search "frontier folk music" or "western RPG OST") or use `freemusicarchive.org`
- **Fonts**: Google Fonts — `Playfair Display` (Victorian serif for narration) + `IM Fell English` (period feel)

### Step 6: UI Customization
- Color palette: Dusty earth tones (ochre, burnt sienna, dark brown, cream)
- Dialogue box: Parchment-textured background
- Font: Period-appropriate serif
- Chapter title cards: Hand-lettered style with a Western motif

### Step 7: Playtest and Polish
- Play through all 7 scenes
- Test all choice branches
- Check relationship meter values for balance
- Add transition effects between scenes (fade, dissolve)

---

## Critical Files (to be created)
- `game/script.rpy` — Core story (primary development effort)
- `game/characters.rpy` — Character definitions
- `game/variables.rpy` — State tracking
- `game/gui/` — Visual theme (color, fonts)

---

## Verification / Testing
1. Launch Ren'Py project → click "Launch Project" to test in editor
2. Play through Scene 1 completely, verify all choices branch correctly
3. Check that `yancey_relationship` and `sabra_direction` change as expected after each scene
4. Verify journal entries appear at scene end
5. Export to Web (HTML5) from Ren'Py launcher and open in browser to confirm
6. Have someone unfamiliar with the novel play Scene 1 and describe who Sabra is — success if they can articulate her character clearly

---

## Estimated Scope for Chapter 1 MVP
- 7 scenes, ~30-60 minutes of play
- ~15-20 choice moments
- 4 background images, 3-4 character sprites
- 2 music tracks
- ~1,500-2,000 lines of `.rpy` script
