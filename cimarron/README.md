# Cimarron — Ren'Py Visual Novel

A visual novel based on *Cimarron* by Edna Ferber (1929). Covers **all five chapters** — the complete game (Scenes 1–28, 1889–1931).

---

## How to Run

1. **Download Ren'Py** from https://www.renpy.org/ (free, Windows/Mac/Linux).
2. Open the Ren'Py launcher.
3. Click **"Open Project"** and navigate to this folder (`cimarron/`).
4. Click **"Launch Project"** to play.

---

## Project Structure

```
cimarron/
├── game/
│   ├── script.rpy                ← Entry point; jumps to chapter1_start
│   ├── script_chapter1.rpy       ← Scenes 1–7, Chapter 1 summary
│   ├── script_chapter2.rpy       ← Scenes 8–13, Chapter 2 summary
│   ├── script_chapter3.rpy       ← Scenes 14–18, Chapter 3 summary
│   ├── script_chapter4.rpy       ← Scenes 19–23, Chapter 4 summary
│   ├── script_chapter5.rpy       ← Scenes 24–28, three ending branches (final chapter)
│   ├── characters.rpy            ← All character definitions and colors
│   ├── variables.rpy             ← Game state (all meters and flags)
│   ├── options.rpy               ← Project settings (title, screen size, transitions)
│   ├── gui.rpy                   ← Visual theme (colors, fonts, layout)
│   ├── screens.rpy               ← UI screens (save/load, menus, quick bar)
│   ├── minigame_typesetting.rpy  ← Scene 6 typesetting mini-game
│   ├── minigame_collection.rpy   ← Scene 8 church collection mini-game
│   ├── minigame_letters.rpy      ← Scene 16 letters-to-the-editor mini-game
│   ├── minigame_trial.rpy        ← Scene 20 trial arguments mini-game
│   ├── minigame_photographs.rpy  ← Scene 28 photograph box mini-game
│   ├── images/                   ← Backgrounds and character sprites (add files here)
│   │   └── sprites/
│   ├── audio/                    ← Music tracks (add .ogg files here)
│   └── gui/                      ← GUI images (textbox, buttons — add .png files here)
└── README.md                     ← This file
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
| `bg_mission_wichita.png` | Catholic mission grounds, Wichita 1889, rhubarb garden | "1889 Wichita Kansas Catholic mission grounds, rhubarb garden foreground, osage orange hedge, whitewashed frontier chapel with cross, morning light, oil painting style" |
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
- Generate with AI (Midjourney, Adobe Firefly) — use the four-part phrasing: "transparent background, PNG with alpha channel, isolated figure, no background"
- Search itch.io for "western VN sprites" or "historical character sprites"
- Use silhouette-style sprites (all black with colored outlines) if portrait art isn't ready

**Important — background removal:** AI generators often bake the transparency checkerboard in as actual pixels. Always verify the PNG has true alpha-channel transparency before use. If the background is visible in-game, see `plans/sprite_bg_removal.md` for the detection and fix process.

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

### Community Standing (`community_standing`) — Chapter 2+
- Starts at 0; tracks how Osage as a town sees Sabra
- High = well-regarded civic figure; Low = has made enemies being right

### Indian Sympathy (`indian_sympathy`) — Chapter 2+
- Starts at 0; tracks Sabra's stance toward the Osage/Cherokee peoples
- High = active advocate; Low = accommodates the town's prejudices

### Sabra's Independence (`sabra_independence`) — Chapter 2+
- Starts at 0; tracks how self-sufficient Sabra becomes without Yancey
- Rises when she acts alone, falls when she defers or waits for him

### Journal Entries
- Appear at the end of each scene
- Summarize Sabra's emotional state in her own voice
- Function as a recap and character development device

### Newspaper Stance (`newspaper_stance`) — Chapter 3+
- Starts at 0
- Positive = progressive (Indian rights, women's voice, reform journalism)
- Negative = conservative (advertiser-friendly, civic respectability)
- Influenced by Sabra's editorial choices and which letters she prints

### Chapter 4 Flags
- `dixie_lee_editorial` — how the Wigwam covered the Dixie Lee verdict: `"support"` / `"oppose"` / `"neutral"`
- `statehood_stance` — the Wigwam's position on Oklahoma statehood: `"single"` / `"double"` / `"consult"`
- Both appear in the Chapter 4 summary

### Trial Arguments Mini-Game (Scene 20)
- Yancey defends Dixie Lee on a charge of keeping a disorderly house
- **Phase 1** — six argument cards; click to select/deselect (max 3); "Proceed to Ordering" activates at exactly 3 selected
- **Phase 2** — place the three arguments into labeled slots: OPENING / MIDDLE / CLOSING; click a filled slot to view and remove its argument; "Present to Jury" activates when all three slots are filled
- Returns `([selected_ids], [opening_id, middle_id, closing_id])`
- Selection bonuses: sympathy arg → `yancey_relationship +5`; hypocrisy arg → `newspaper_stance +1`; jury challenge → `yancey_relationship +3`, `community_standing -1`; due process → `newspaper_stance +1`; equality + jurisdictional together → `newspaper_stance -1`, `yancey_relationship -3`
- Order bonuses: sympathy arg in CLOSING → `yancey_relationship +3`; jury challenge in OPENING → `community_standing -1`; due process in OPENING → `newspaper_stance +1`
- Implemented in `game/minigame_trial.rpy`

### Typesetting Mini-Game (Scene 6)
- Sabra sets the first headline for the *Oklahoma Wigwam*
- Five scrambled lead-type tiles spell the town name: **O S A G E**
- Click a tile to place it in the composing stick (left to right)
- Click a placed tile to send it back to the tray (undo)
- Hit **Set the Type** once all five slots are filled
- **Correct order** → `sabra_direction +2`, Yancey is impressed
- **Wrong order or Give Up** → Yancey quietly corrects it, neutral outcome
- Implemented in `game/minigame_typesetting.rpy`

### Church Collection Mini-Game (Scene 8)
- Sabra watches the Sunday collection hat pass through 8 congregation members
- The hat moves left to right, spending ~4 seconds on each member
- 3 of the 8 members are secretly skimming — they show an amber `!` tell while the hat is on them
- Click a member while the hat is on them to flag them as a cheat
- You have 30 seconds total; flagging a non-cheat counts against you (false positive)
- **Score 3/3** → `community_standing +3`, the congregation notices Sabra's sharp eye
- **Score 1–2** → `community_standing +1–2`
- **Score 0** → no bonus
- Implemented in `game/minigame_collection.rpy`
- The `!` and `O` symbols are placeholders; see the **Chapter 2 Assets** section below for how to swap in sprites

---

## Scenes

### Chapter One — The Land of the Fair God (1889)

| Scene | Location | Key Moment |
|---|---|---|
| 1. The Venable Home | Wichita parlor | How Sabra reacts to Yancey's storytelling |
| 2. The Land Run | Flashback | Does she admire or fear his idealism? |
| 3. The Decision | Venable dining room | Confront mother / stand behind Yancey / private doubt |
| 4. The Journey West | Wagon trail | Does she open up to the frontier? |
| 5. Arriving at Osage | Osage tent town | First confrontation with a rough frontier character |
| 6. The Oklahoma Wigwam | Newspaper tent | **Typesetting mini-game** + response to danger |
| 7. End of Chapter | Osage / epilogue | Reflection — what was gained, what was lost |

### Chapter Two — Building Osage (1890–1893)

| Scene | Location | Key Moment |
|---|---|---|
| 8. The Lion in the Streets | Church tent | Yancey faces down a gunman; **collection mini-game** |
| 9. Seven Notches | Wigwam office | Sabra learns about Yancey's past killings |
| 10. The Wigwam Lives | Wigwam office | Indian rights editorial; Arita Red Feather brings documents |
| 11. The Wind and Donna | Cravat home | Donna born; Yancey is away |
| 12. Respectability | Osage parlor | Women's Club founding; who gets to belong |
| 13. The Cherokee Strip | Wigwam office | Yancey rides for the last land run |

### Chapter Three — Yancey Leaves; Sabra Rises (1893–1898)

| Scene | Location | Key Moment |
|---|---|---|
| 14. Five Years | Wigwam office | Sabra holds Osage together across Yancey's 5-year absence |
| 15. The Kid | Osage street | Yancey returns after killing the Kid; reward money choice |
| 16. Running the Paper | Wigwam office | Sabra as editor; Indian allotment editorial; **letters mini-game** |
| 17. Isaiah | Wigwam office | Isaiah reads type; defended against an advertiser; his death planted |
| 18. The War | Editorial office | Yancey enlists for Spanish-American War; Dixie Lee at the door |

### Chapter Four — War Hero, Statehood, Oil (1898–1907)

| Scene | Location | Key Moment |
|---|---|---|
| 19. The Rough Rider | Osage main street / Wigwam | Yancey returns from Cuba; public moment + private reunion |
| 20. Dixie Lee's Trial | Courthouse | Night-before choice; **trial mini-game**; editorial; hallway |
| 21. The Statehood Question | Civic hall / Wigwam | One state vs. two; Yancey's letter; statehood day, Nov 16 1907 |
| 22. The First Oil | Wigwam / oil fields | Derricks rising; Tracy Wyatt in town; Cim's future |
| 23. What Yancey Left | Wigwam (1907) | Yancey absent; a letter; Donna leaving; Sabra takes stock |

---

## Chapter 2 Assets

### Additional Backgrounds

| Filename | Description | AI Prompt Suggestion |
|---|---|---|
| `bg_tent_church.jpg` | Canvas tent serving as a frontier church, wooden pew benches, oil lamps | "Oklahoma frontier church tent interior 1890, rough pine benches, oil lamps, congregation, painted illustration" |
| `bg_cravat_home.jpg` | Interior of a simple but sturdy frame house on the Oklahoma prairie | "1890s Oklahoma frontier farmhouse interior, cookstove, glass windows, modest but cared-for, painted illustration" |
| `bg_osage_parlor.jpg` | A respectable Osage parlor — better-furnished than a tent, not yet grand | "1890s small-town Oklahoma parlor, floral wallpaper, horsehair sofa, afternoon light, Victorian frontier, painted illustration" |

### Additional Audio

| Filename | Mood |
|---|---|
| `osage_sunday.ogg` | Quiet Sunday-morning hymn feeling — slow, plain, earnest |
| `wigwam_press.ogg` | Low rhythmic ambience of a working print shop — mechanical, purposeful |
| `cherokee_strip.ogg` | Wide-open, urgent, bittersweet — the last land run, something ending |

### Additional Sprites

| Filename | Character |
|---|---|
| `doc_neutral.png` | Doc Valliant — weathered frontier doctor, medical bag, sardonic expression |
| `arita_neutral.png` | Arita Red Feather — young Osage woman, calico dress, moccasins, still face |
| `pete_neutral.png` | Pete Pitchlyn — half-Cherokee lawyer, well-tailored suit, measuring eyes |
| `isaiah_neutral.png` | Isaiah — young Black man (Ch 2 version, age ~13), working clothes |

See `plans/character_bible.md` for full visual descriptions and AI generation prompts for each character.

### Church Collection Mini-Game (Scene 8)

The mini-game currently uses text symbols (`!` for cheating members, `O` for
innocent) as placeholders. These can be replaced with actual sprite art:

**Member silhouettes** — 8 generic congregation members, shown as small
standing figures (no individual names needed). A single reusable silhouette
works for all 8:

| Filename | Usage |
|---|---|
| `congregation_neutral.png` | Default member — standing figure, Sunday dress, facing forward |
| `congregation_cheat.png` | Same figure with a guilty tell — eyes shifted, hand slightly extended toward the hat |

Place both in `game/images/sprites/`. Then in `minigame_collection.rpy`,
replace the `text "O"` and `text "!"` blocks inside each button with:

```renpy
## Replace placeholder text with sprites:
if is_hat and is_cheat and not is_flagged:
    add "sprites/congregation_cheat.png" xalign 0.5
else:
    add "sprites/congregation_neutral.png" xalign 0.5
```

The amber highlight and `FLAGGED` label can stay as-is — they overlay the
sprite automatically via the button's background color.

---

## Chapter 3 Assets

### Additional Backgrounds

| Filename | Description | AI Prompt Suggestion |
|---|---|---|
| `bg_wigwam_office_daytime.jpg` | The Wigwam press room in daylight — Sabra at the compositor's desk | "1890s frontier newspaper office, daylight through dusty windows, letterpress cases, woman working, painted illustration" |
| `bg_osage_street_1895.jpg` | Main street of Osage circa 1895 — frame buildings, boardwalks, horses | "1895 Oklahoma small town main street, wooden storefronts, horse-tied hitching posts, afternoon light, painted illustration" |
| `bg_hefner_window.jpg` | A single lit window at night — warm glow against a dark sky | "Lit window at night, Oklahoma prairie darkness, warm amber light inside, silhouette, oil painting style" |
| `bg_editorial_office_night.jpg` | The Wigwam at night — oil lamps, ink smell, a woman at her desk | "1890s newspaper office at night, oil lamps, woman editor at desk, letterpress in shadows, painted illustration" |

### Additional Audio

| Filename | Mood |
|---|---|
| `five_years.ogg` | Slow, persistent, quietly determined — time passing without stopping |
| `kid_return.ogg` | Low tension releasing — relief mixed with unease, a man returned from violence |
| `war_march.ogg` | Martial and far-off — patriotic brass dulled by distance and loss |

### Letters Mini-Game (Scene 16)

Scene 16 uses `minigame_letters.rpy`. No sprite replacements needed — the
mini-game uses styled text cards. The 8 letter senders and their tag categories are:

| Sender | Tag | Effect if Printed |
|---|---|---|
| A.J. Folsom | anti-indian | `newspaper_stance -2`, `indian_sympathy -1` |
| Pete Pitchlyn | pro-indian | `newspaper_stance +2`, `indian_sympathy +1` |
| Mrs. Wyatt | neutral | No variable change |
| Shanghai Wiley | yancey | `yancey_relationship +1` |
| Anonymous | gossip | `community_standing -2` |
| A Ponca farmer | pro-indian | `newspaper_stance +2`, `indian_sympathy +1` |
| Oil Company Rep | oil | `newspaper_stance -1` (applied in result) |
| Name Withheld | frontier | Special narrative beat if printed |

---

## Chapter 4 Assets

### Additional Backgrounds

| Filename | Description | AI Prompt Suggestion |
|---|---|---|
| `bg_osage_street_1900.jpg` | Osage main street circa 1900 — frame buildings, some brick, boardwalks | "Oklahoma small town main street 1900, frame and brick storefronts, boardwalk, a crowd gathered, painted illustration" |
| `bg_courthouse_interior.jpg` | Territorial courtroom — wood-paneled bench, gallery pews, high windows | "1890s Oklahoma territorial courthouse interior, wood benches, judge's bench, afternoon light, painted illustration" |
| `bg_civic_hall.jpg` | Town meeting hall — rows of chairs, a raised platform, American flags | "1900s small-town civic hall interior, folding chairs, platform with podium, bunting, painted illustration" |
| `bg_oil_derrick_distant.jpg` | Oklahoma plains with oil derricks on the horizon at dawn | "Oklahoma plains 1905, oil derricks on distant horizon against dawn sky, red clay, sparse grass, painted illustration" |
| `bg_wigwam_modern.jpg` | The Wigwam pressroom in 1907 — more equipment, settled, Sabra's own | "1907 Oklahoma newspaper pressroom, letterpress machinery, woman's personal items, evening lamp, painted illustration" |

### Additional Audio

| Filename | Mood |
|---|---|
| `hero_return.ogg` | Triumphant but understated — brass with frontier undertones, a crowd's warmth |
| `courthouse_quiet.ogg` | Tense, minimal — low strings, something unresolved |
| `state_seal.ogg` | Civic, measured — a sense of mixed feeling; something ending as something begins |
| `oil_derricks.ogg` | Industrial rhythm — something new and mechanical arriving on the prairie |

### Additional Sprites

| Filename | Character |
|---|---|
| `tracy_neutral.png` | Tracy Wyatt — modern Tulsa oil investor; well-tailored, self-assured, mid-40s |
| `cim_neutral.png` | Cim Cravat — Sabra's son as a young man (~17); his father's frame, quieter manner |
| `donna_neutral.png` | Donna Cravat — Sabra's daughter as a teenager (~16); sharp-eyed, opinionated |

### Trial Mini-Game (Scene 20)

The mini-game uses styled text cards — no sprite replacements needed. The six argument
cards and their selection/ordering effects are:

| Argument | Type | Selection Bonus | Order Bonus |
|---|---|---|---|
| She pays taxes | Legal / Equality | — | — |
| Came to survive | Sympathy | `yancey_relationship +5` | +3 more if placed in CLOSING |
| Selective enforcement | Legal / Hypocrisy | `newspaper_stance +1` | — |
| No jurisdiction | Jurisdictional | — | — |
| Challenge the jury | Jury Challenge | `yancey_relationship +3`, `community_standing -1` | -1 more `community_standing` if in OPENING |
| Due process | Constitutional | `newspaper_stance +1` | +1 more `newspaper_stance` if in OPENING |

Selecting both **She pays taxes** and **No jurisdiction** together applies a penalty:
`newspaper_stance -1`, `yancey_relationship -3` (redundant legal strategy).

---

## Chapter 5 Assets

### Scenes

| Scene | Location | Key Moment |
|---|---|---|
| 24. Cim Brings Ruby Home | Kihekah Street parlor | Cim marries Ruby Big Elk; Sabra meets her daughter-in-law |
| 25. The Congresswoman | Washington / Osage | Sabra runs for and serves in Congress; chooses her platform |
| 26. Donna's Wedding | Kihekah Street parlor | Donna marries Tracy Wyatt; Sabra's five private minutes |
| 27. The Word from Bowlegs | Bowlegs oil field | Nitroglycerin catch; Yancey's death; the Peer Gynt line |
| 28. The Monument | Ceremony square | **Photograph mini-game**; monument unveiled; ending branch |

### Ending Branches

| Branch | Name | Condition | Music |
|---|---|---|---|
| 1 | She Was His Shadow | `sabra_independence ≤ 4` AND `yancey_relationship ≥ 65` | `monument_shadow.ogg` |
| 2 | She Built It Herself | `sabra_independence ≥ 8` AND `community_standing ≥ 8` | `monument_builder.ogg` |
| 3 | The Land Belongs to All | `indian_sympathy ≥ 7` AND (`sabra_independence ≥ 5` OR `yancey_relationship ≥ 50`) | `monument_land.ogg` |

Branches checked in order: 3 → 2 → 1. Branch 1 is the fallback.

### Additional Backgrounds

| Filename | Description | AI Prompt Suggestion |
|---|---|---|
| `bg_kihekah_house_parlor.jpg` | The Cravat house on Kihekah Street, now comfortable: old mahogany, polished floor | "1910s Oklahoma small-town parlor, mahogany furniture, embroidered antimacassars, afternoon light, painted illustration" |
| `bg_washington_dc_hall.jpg` | A congressional hallway — marble, hushed, 1920s | "1920s US congressional hallway, marble columns, afternoon light through tall windows, painted illustration" |
| `bg_oil_field_bowlegs.jpg` | The raw Bowlegs oil field, 1930 — mud, derricks, tin shacks, workers | "Oklahoma oil field 1930, wooden derricks, mud, workers, raw industrial landscape, painted illustration" |
| `bg_monument_ceremony.jpg` | Ceremony square, covered statue, crowd, Oklahoma sky | "1931 Oklahoma public square, covered monument, large crowd, bright sky, civic ceremony, painted illustration" |

### Additional Audio

| Filename | Used in | Mood |
|---|---|---|
| `kihekah_parlor.ogg` | Scenes 24, 26, 28 (opening) | Warm but autumnal — chamber strings or piano, a well-lived life |
| `congress_hall.ogg` | Scene 25 | Formal and measured — stately piano or sparse brass |
| `bowlegs_field.ogg` | Scenes 26 (transition), 27 | Nearly silent — stark industrial drone, grief through absence |
| `monument_shadow.ogg` | Branch 1 ending | Romantic and swelling — full strings, unambiguously emotional |
| `monument_builder.ogg` | Branch 2 ending | Resolute and clear — piano-led, forward motion |
| `monument_land.ogg` | Branch 3 ending | Open and elemental — sparse, wide, hint of Native melodic color |

### Additional Sprites

| Filename | Character |
|---|---|
| `ruby_neutral.png` | Ruby Big Elk — young Osage woman, composed, direct, watchful |
| `krbecek_neutral.png` | Masja Krbecek — small Polish sculptor in round glasses; precise, observant |

### Chapter 5 Flags

| Variable | Values | Set in |
|---|---|---|
| `ruby_welcomed` | True/False | Scene 24 — chose "Welcome to our family" |
| `ruby_time_needed` | True/False | Scene 24 — chose "I need time" |
| `congress_issue` | `"indian"` / `"oil_law"` / `"education"` | Scene 25 |
| `donna_wedding_advice` | `"chose_well"` / `"cravat_stock"` / `"be_happy"` | Scene 26 |

### Photograph Mini-Game (Scene 28)

Krbecek asks Sabra for photographs before the monument ceremony. She selects 2 of 6 from the cedar box she has kept for forty years.

- Six photo cards in a 2×3 grid; click to see caption, chapter reference, and memory text
- Select/Deselect buttons in the detail overlay; max 2 selected
- "Give to Krbecek" activates when exactly 2 are selected
- Each photo pair nudges the ending branch when meters are near a threshold:

| Photos | Ending Nudge |
|---|---|
| 1 (Run) + 4 (Rough Rider) | `yancey_relationship +3` — tips toward Branch 1 |
| 3 (Sabra at press) + 2 (tent church) | `community_standing +2` — tips toward Branch 2 |
| 5 (Kid's burial) + 6 (Cim/Ruby) | `indian_sympathy +2` — tips toward Branch 3 |
| Any other pair | `yancey_relationship +1` (mild default) |

Implemented in `game/minigame_photographs.rpy`.

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
