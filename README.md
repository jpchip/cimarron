# Cimarron

A visual novel adaptation of *Cimarron* by Edna Ferber (1929), built in Ren'Py.

![Main menu screenshot](screenshot_mainmenu.png)

You play as **Sabra Cravat** — a refined Southern belle pulled into frontier life
by her charismatic husband Yancey. The complete game covers five chapters
(Scenes 1–28, 1889–1931): the Oklahoma Land Run and founding of Osage (Chapter One),
the town's early years and Yancey's first disappearance (Chapter Two, 1890–1893),
Yancey's five-year absence and Sabra's rise as editor (Chapter Three, 1893–1898),
the Rough Rider return, Dixie Lee's trial, statehood, and the first oil boom
(Chapter Four, 1898–1907), and the final chapter covering Cim's marriage, Sabra's
congressional career, Yancey's death at Bowlegs, and the Oklahoma Pioneer monument
unveiling with three possible endings (Chapter Five, 1910–1931).

---

## Quick Start

1. **Download Ren'Py** (free) from https://www.renpy.org/
2. Open the Ren'Py launcher → **Open Project** → select `cimarron/`
3. Click **Launch Project**

---

## Repository Layout

```
cimarron/
├── book.md               ← Source text: Cimarron by Edna Ferber (public domain)
├── PLAN.md               ← Design document and scene breakdown
├── LICENSE               ← MIT license (game code) + public domain note (source text)
└── cimarron/             ← Ren'Py game project
    ├── README.md         ← Full asset guide, mechanics reference, scene list
    └── game/
        ├── script.rpy                ← Entry point
        ├── script_chapter1.rpy       ← Scenes 1–7
        ├── script_chapter2.rpy       ← Scenes 8–13
        ├── script_chapter3.rpy       ← Scenes 14–18
        ├── characters.rpy            ← Character definitions
        ├── variables.rpy             ← Game state variables
        ├── options.rpy               ← Project configuration
        ├── gui.rpy                   ← Visual theme (earth tones, fonts)
        ├── screens.rpy               ← UI screens (save/load, menus)
        ├── script_chapter4.rpy       ← Scenes 19–23
        ├── minigame_typesetting.rpy  ← Scene 6 typesetting mini-game
        ├── minigame_collection.rpy   ← Scene 8 collection mini-game
        ├── minigame_letters.rpy      ← Scene 16 letters mini-game
        ├── minigame_trial.rpy        ← Scene 20 trial arguments mini-game
        ├── images/                   ← Backgrounds and sprites (add your art here)
        └── audio/                    ← Music tracks (add .ogg files here)
```

See **`cimarron/README.md`** for the full asset guide, font setup,
mechanics reference, and scene breakdown.

---

## Chapter One — What's in the Game

**7 scenes** covering Wichita through the founding of Osage:

1. The Venable Home — Yancey arrives and recounts the Land Run
2. The Land Run Flashback — the woman on the black thoroughbred
3. The Decision — Sabra chooses to go west against her mother's will
4. The Journey West — nine days across the red clay of Oklahoma
5. Arriving at Osage — culture shock and first frontier encounters
6. The Oklahoma Wigwam — setting up the press; typesetting mini-game
7. End of Chapter — church in a saloon; Sabra writes home

**~18 choice moments** that shape two tracked values:

| Meter | Range | Effect |
|---|---|---|
| Yancey Relationship | 0 – 100 | Dialogue warmth; end-of-chapter summary |
| Sabra's Direction | negative ↔ positive | Refined Lady vs. Frontier Woman track |

**Typesetting mini-game** in Scene 6: arrange five scrambled lead-type tiles to
spell **OSAGE** in the composing stick. Getting it right earns Yancey's respect
and nudges Sabra toward the Frontier Woman track.

---

## Chapter Two — Building Osage (1890–1893)

**6 scenes** covering Osage's growth and Yancey's first disappearance:

8. The Lion in the Streets — a gunman disrupts Sunday service; Yancey faces him down
9. Seven Notches — Pete Pitchlyn names the men Yancey has killed; Sabra decides what to do with that
10. The Wigwam Lives — Yancey's Indian rights editorials make enemies; Arita Red Feather arrives with documents
11. The Wind and Donna — Donna is born while Yancey is away covering the territory
12. Respectability — the Osage Women's Club is founded; Sabra decides who belongs
13. The Cherokee Strip — Yancey rides for the last land run and does not come back on schedule

**~16 choice moments** that add four new tracked values:

| Meter | Range | Effect |
|---|---|---|
| Yancey Relationship | 0 – 100 | Carries over from Chapter 1 |
| Sabra's Direction | negative ↔ positive | Carries over from Chapter 1 |
| Community Standing | negative ↔ positive | How Osage sees Sabra; affects Chapter 2 summary |
| Indian Sympathy | negative ↔ positive | Sabra's stance toward the Nations; affects Chapter 2 summary |
| Sabra's Independence | 0 → positive | How self-sufficient Sabra becomes without Yancey |

**Church collection mini-game** in Scene 8: watch as the collection hat passes
through 8 congregation members. Three of them are skimming — they show a brief
tell while the hat is on them. Click to flag them before the hat moves on.
You have 30 seconds. Score affects community standing.

---

## Chapter Three — Yancey Leaves; Sabra Rises (1893–1898)

**5 scenes** covering Yancey's five-year absence and Sabra's growth:

14. Five Years — montage of Sabra holding the Wigwam together; how she found her footing
15. The Kid — Yancey returns after killing a young gunman; the reunion is complicated
16. Running the Paper — Sabra writes her own editorials; **letters-to-the-editor mini-game**
17. Isaiah — Sabra discovers Isaiah's literacy; defends him against an advertiser; his death is planted
18. The War — Yancey enlists for the Spanish-American War; Dixie Lee comes to the door

**~14 choice moments** that add one new tracked value:

| Meter | Range | Effect |
|---|---|---|
| Newspaper Stance | negative ↔ positive | Conservative vs. progressive editorial direction |

**Letters mini-game** in Scene 16: 8 letters arrive; Sabra must select exactly 4 to print.
Each letter has a tag (pro-indian, anti-indian, gossip, oil, yancey, neutral, frontier).
Which letters she prints shifts `newspaper_stance`, `indian_sympathy`, and `community_standing`.

---

## Chapter Four — War Hero, Statehood, Oil (1898–1907)

**5 scenes** covering the Rough Rider return through Oklahoma statehood and the oil boom:

19. The Rough Rider — Yancey returns from Cuba in uniform; public moment and private reunion
20. Dixie Lee's Trial — Yancey defends Dixie Lee; **trial arguments mini-game**; editorial choice
21. The Statehood Question — one state or two; Yancey's letter; statehood day
22. The First Oil — the derricks rise; Tracy Wyatt arrives; Cim's future
23. What Yancey Left — statehood day 1907; Yancey absent; Donna leaving; taking stock

**~14 choice moments** — no new meters, but two new flag-tracked decisions:

| Flag | Values | Effect |
|---|---|---|
| `dixie_lee_editorial` | support / oppose / neutral | Chapter summary reflects the Wigwam's public stance |
| `statehood_stance` | single / double / consult | Chapter summary reflects the editorial position |

**Trial arguments mini-game** in Scene 20: choose 3 of 6 legal arguments for Yancey to present,
then arrange them as OPENING / MIDDLE / CLOSING. Selection and ordering both affect
`yancey_relationship`, `newspaper_stance`, and `community_standing`.

### Chapter 4 — New Assets Needed

**Backgrounds:**
- `bg_osage_street_1900` — main street, slightly more developed than 1895 version
- `bg_courthouse_interior` — territorial courtroom, wood benches, judge's bench
- `bg_civic_hall` — town meeting hall, chairs and a raised platform
- `bg_oil_derrick_distant` — Oklahoma plains with derricks on the horizon
- `bg_wigwam_modern` — the Wigwam pressroom in 1907, more equipment, settled

**Audio:**
- `hero_return.ogg` — triumphant but understated; brass with frontier undertones
- `courthouse_quiet.ogg` — tense, minimal; low strings
- `state_seal.ogg` — civic, measured; a sense of mixed feeling
- `oil_derricks.ogg` — industrial rhythm; something new arriving

**New Characters:**
- `tracy` — Tracy Wyatt, oil investor; needs `tracy_neutral.png`
- `cim` — Cim Cravat as a young man; needs `cim_neutral.png`
- `donna` — Donna Cravat as a teenager; needs `donna_neutral.png`

---

## Source Material

> *Cimarron* by Edna Ferber, first published 1929.
> In the public domain in the United States.
> Source text via [Standard Ebooks](https://standardebooks.org) (CC0).

---

## License

The game code (all `.rpy` files and other software) is released under the
**MIT License** — see `LICENSE` for details.

The source novel text is public domain. Any art assets or music you add may
carry their own licenses; check before redistributing.


## Note

```bash
systemd-inhibit --what=sleep:idle --who="Claude Remote" --why="Remote Session Active" claude remote-control
```