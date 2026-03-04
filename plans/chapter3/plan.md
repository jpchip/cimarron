# Chapter 3 Plan — Yancey Leaves; Sabra Rises
## Book Chapters XIII–XV | c. 1893–1898 | ~5 years

---

## Overview

Yancey is gone. For five years Sabra runs the Oklahoma Wigwam alone, raises two children, leads women's clubs, and becomes — whether she planned it or not — the backbone of Osage. When Yancey finally returns (he has killed the outlaw known as the Kid), the town celebrates him. Sabra must choose how she feels. Then he disappears again — this time to war.

New variable introduced: `sabra_independence` (0–10). Tracks whether Sabra has accepted her own authority, separate from Yancey.

---

## Characters (no new additions to characters.rpy beyond Ch 2)
*(The Kid appears briefly in backstory; never on screen. Jesse Rickey continues. Isaiah continues until his death this chapter.)*

---

## New Backgrounds Needed

| Filename | Description |
|---|---|
| `bg_wigwam_office_daytime` | Sabra alone at the editor's desk; quieter, more organized than Yancey kept it |
| `bg_osage_street_1895` | Pawhuska Avenue, mid-decade: a few more buildings, a sidewalk, still red dust |
| `bg_hefner_window` | The dark window of Hefner's Furniture and Undertaking; a crowd outside |
| `bg_editorial_office_night` | Lamp-lit desk, galley proofs, ink smell; Sabra working late |

---

## Scene 14 — "Five Years"
**Source:** Book Chapter XIII (opening)
**Time:** 1893–1898 (montage / summary scene)

### Narration
A compressed, lyrical scene. Five years of absence. Sabra narrates directly through her journal: what she learned, what hardened, what softened. The Wigwam. The children. The Territory changing around her. Arita Red Feather. Isaiah's growing up. The women's clubs.

This scene is primarily narration with one key choice that sets the tone for Sabra's inner life during the absence.

### Beat
*Sabra sits at her desk in the Wigwam office. Outside the window: Osage is growing up. Inside: she is growing up too.*

### Choice 1 — How Sabra Held On
> Five years is a long time to wait for someone who hasn't promised to come back. Sabra found ways to fill it.

- **"I told myself he would return. I kept a place for him."** *(Faithful)*
  - `yancey_relationship += 5` (she stayed emotionally open)
  - `sabra_independence += 1` (low growth; she needed the belief in him)
- **"I stopped waiting. I ran the paper. That was enough."** *(Independent)*
  - `sabra_independence += 3`
  - `yancey_relationship -= 5` (the gap widened in her heart)
- **"I made a life. It isn't the life I planned. It might be better."** *(Acceptance)*
  - `sabra_independence += 2`, `community_standing += 1`
  - The most nuanced position. She is neither bitter nor naive.

### Journal Entry 14 (pre-formatted, displayed mid-scene)
> *"Years three and four, I stopped counting weeks. I counted ink orders instead. Forty pounds of type alloy. Sixty reams of newsprint. Fifteen gallons of ink. That is what five years looks like from the inside."*

---

## Scene 15 — "The Kid"
**Source:** Book Chapter XIII
**Time:** 1898, a Tuesday

### Narration
Sabra steps off the train from Wichita. Yancey is not on the platform. The station agent tells her: there's been a gunfight. Yancey killed the Kid — the most wanted outlaw in the Territory. He's alive, but wounded in the arm, and the whole town is celebrating.

Isaiah runs out to meet her: alive, gangling, overjoyed.

### Beats
1. The empty platform. The frantic telegraph clicking.
2. Pat Leary at the station window gives her the news.
3. Isaiah runs to meet her, rattling off the story in his breathless way.
4. The newspaper office: packed with strangers. Yancey in the corner, gray-faced, exhausted.
5. "Send them away. I'm so tired. Oh, God, I'm so tired."

### Choice 1 — When She Sees Him
> He looks smaller than she remembers. Not physically — he is still enormous — but somehow diminished. As though the act of killing, even a man like the Kid, costs something that doesn't grow back.

- **Run to him. Hold him.**
  - `yancey_relationship += 10`
  - She crosses the room without thinking. He sags into her arms. The crowd watches.
- **Stand still. Let him come to her.**
  - `sabra_independence += 1`
  - A small test. He takes three steps toward her. That is enough.
- **"Everyone out. My husband needs rest."** *(Take charge)*
  - `community_standing += 2`, `sabra_independence += 2`
  - She clears the office herself. Yancey watches her with something new in his eyes.

### Choice 2 — The Reward Money
> The railroads, the banks, the government — everyone is sending money. Five thousand dollars from the Santa Fe alone. Yancey refuses all of it. He will not take money for killing a man.

- **"That money could give Cim an education. Donna a future."**
  - `yancey_relationship -= 5`
  - She says it once, clearly, and lets it go. He doesn't move.
- **"I understand. But I want you to explain it to the children."**
  - `yancey_relationship += 5`
  - He does. It is one of the finest conversations in her memory.
- **"It's your decision. I'll run the paper."** *(Accept it)*
  - `sabra_independence += 1`
  - She has learned, slowly, that some of Yancey's choices are not hers to make.

### Journal Entry 15
> *"They put the Kid in Hefner's window in a new suit of store clothes. I told Cim he was absolutely not to go. Then, at sunset, I went myself. I stood there until I had seen enough. I still don't know what I was looking for."*

---

## Scene 16 — "Running the Paper"
**Source:** Book Chapter XIV
**Time:** 1898 (after Yancey's return, before his next departure)

### Narration
Yancey is back — but wrong. His hands shake before his morning whisky. He refuses the governorship, refuses a Congressional seat, laughs at the suggestion. He writes a brilliant editorial and disappears for three days. Sabra, meanwhile, is the paper. She has learned to be.

A brief, warm scene showing what Sabra has become in his absence: decisive, respected, occasionally frightening to those who expected someone softer.

### Beats
1. Sabra edits Yancey's editorial — tightening it without asking permission. He reads the revised version and says nothing for a long moment.
2. She publishes the arguments of the Double Statehood party (she is not sure she agrees with Yancey's Indian advocacy).
3. The women's Philomathean Club votes her president.

### Choice 1 — The Edited Editorial
> She has cut three paragraphs of his florid opening. What remains is better. She knows it. She waits.

- **Yancey: "You cut the Shakespeare quote."**
  - **"It slowed the argument down."** — He stares, then laughs. "You're right." `yancey_relationship += 5`, `sabra_independence += 1`
  - **"I'm sorry. Do you want me to put it back?"** — `sabra_independence -= 1` (she hedges)
- **Yancey says nothing. He goes to the compositing room.**
  - She doesn't know if she's right. She publishes it anyway.
  - `sabra_independence += 2`

### Choice 2 — The Indian Question
> The paper has been publishing Yancey's pro-Indian statehood arguments for years. Sabra has been — quietly, carefully — also printing the other side.

- **"I think our readers deserve to hear both arguments."**
  - `newspaper_stance = 0` (early signal; balanced)
  - `indian_sympathy += 1` (she is engaging seriously with the question)
- **"The Indians should have their own state. I've come to see it."**
  - `indian_sympathy += 2`, `newspaper_stance += 1` (progressive lean)
- **"The Territory needs to be one state. For the white settlers' sake."**
  - `indian_sympathy -= 1`, `newspaper_stance -= 1` (conservative lean)

### Journal Entry 16
> *"They offered him the governorship. He laughed. I did not. I stood very still and thought about the mahogany from Wichita and whether it would fit in the Governor's mansion, and then I put the thought away."*

---

## Scene 17 — "Isaiah"
**Source:** Book Chapters XIII–XIV
**Time:** 1898

### Narration
Isaiah has grown from the boy on the punkah board into a young man in his teens. He is part of the household — part of the paper — part of Osage in his own way. He has been helping Arita Red Feather with the house and running errands for the Wigwam. He is also, increasingly, present in a world that does not always welcome him.

This scene explores Sabra's relationship with Isaiah — her feelings about him, her assumptions, her affection.

*Note: Isaiah dies in a riding accident (off-screen in the book) some time in this period. This scene plants the relationship before the loss.*

### Beats
1. Isaiah demonstrates that he can read — he has been teaching himself from the Wigwam's type cases.
2. A local man makes a disparaging remark about Isaiah's presence in the newspaper office.
3. Sabra defends Isaiah.

### Choice 1 — Isaiah Reads
> He has typeset a short paragraph himself — his name, the name of the paper, the date. He holds it up to show her, ink-smeared and grinning.

- **"That's remarkable. We'll teach you more."**
  - `community_standing += 1` (she is generous; people notice)
  - `indian_sympathy += 1` (her openness extends to all people the Territory's hierarchy diminishes)
- **"Good. But it's for the paper — don't let it distract you from your other work."**
  - A practical kindness. Not cruel, not expansive.
- **"You shouldn't be setting type. That's Jesse's job."**
  - `sabra_direction -= 1` (Refined Lady instinct — things in their proper place)

### Choice 2 — The Defense
> The man — a new advertiser — says Isaiah should not be behind the counter when a customer comes in. He says it mildly, as though it is a reasonable preference.

- **"He works here. If that's a problem, I'll find a different advertiser."**
  - `community_standing += 2` (bold; some will approve, some won't)
  - `sabra_independence += 1`
- **"I'll speak to him about where he stands." *(Accommodate the customer)*
  - `community_standing -= 1`
  - Narrator: *She regrets it as she says it. She doesn't take it back.*
- **"This is my office. I run it as I see fit."** *(Neither conciliation nor drama)*
  - `sabra_independence += 1`, `community_standing += 1`

### Journal Entry 17
> *"Isaiah can set type faster than Jesse Rickey when Jesse is sober, which lately is not often. I don't know what we would do without him."*

---

## Scene 18 — "He Goes to War"
**Source:** Book Chapter XV (late)
**Time:** 1898, spring

### Narration
"Remember the Maine!" The Spanish-American War. Yancey reads the news with blazing eyes. Theodore Roosevelt is forming a regiment of cavalry — the Rough Riders — and the Oklahoma country is perfect breeding ground for the kind of men he wants.

Yancey is going. Sabra has learned, by now, what this look means.

### Beats
1. Yancey reads the headlines aloud. His voice rings.
2. He tells Sabra: he has already spoken to the recruiting officer.
3. The argument — or its absence. Sabra is different now. She does not scream.
4. Dixie Lee appears at the office door with a brief, cool nod. She is sending two men from her establishment to enlist.
5. Yancey rides south to join his regiment. Sabra watches from the porch.

### Choice 1 — Sabra's Response to His Enlistment
> She could fight it. She has the words for it — she has sharpened them over five years. But something has changed. She is not the same woman who ran after him on the Cherokee Strip road.

- **"I won't beg you to stay. But you will write to me."**
  - `sabra_independence += 2`
  - `yancey_relationship += 5` (a mature request; he is moved by it)
- **"Go. But this is the last time I wait."**
  - `sabra_independence += 3`
  - `yancey_relationship -= 5`
  - A line drawn. She means it. He doesn't quite believe her. She almost means it.
- **"Cim is nine. He needs a father."**
  - `yancey_relationship -= 5`
  - A true plea. Yancey: "He has a mother who could run three territories." It lands wrong.

### Choice 2 — Dixie Lee at the Door
> She is immaculate in dove gray. She does not come inside. She says, "Tell him the boys from my place send their regards to the regiment." She meets Sabra's eyes once, directly.

- **Nod and close the door.**
  - Neutral. It is the civil minimum.
- **"Thank you for telling me."** *(Acknowledge)*
  - `community_standing += 1` (seen as gracious by passersby)
  - Narrator: *Sabra does not know why she says it. Only that it feels right.*
- **Turn away without a word.**
  - `community_standing -= 1`
  - Narrator: *A small ugliness. She knows it.*

### Journal Entry 18
> *"He rode south in his white sombrero and the Oklahoma sun on his back. He looked like a painting of himself. The children waved until he was gone. Then Donna asked for supper. I made it."*

---

## Chapter 3 Summary

| Variable | Expected range after Ch 3 |
|---|---|
| `yancey_relationship` | 25–70 |
| `sabra_direction` | -3 to +4 |
| `community_standing` | +2 to +10 |
| `indian_sympathy` | -3 to +6 |
| `sabra_independence` | 2 to 10 |

### Key Flags Set This Chapter
- `yancey_mystery` (from Ch 2, scene 13) — referenced in scene 15 if True: Sabra expected the absence; it doesn't quite destroy her
- `journal_scene14` through `journal_scene18` — all True by chapter end

---

## Verification

- [x] Book chapters XIII, XIV, XV all represented
- [x] `sabra_independence` has 8+ choice points
- [x] Isaiah's presence and death planted (death is off-screen, but referenced in scene 17)
- [x] Dixie Lee appears without the trial (deferred to Ch 4)
- [x] Yancey's two departures both present: Cherokee Strip (Ch 2) and War (this chapter)
- [x] All journal entries written

---

## Music

| Filename | Used in | Mood |
|---|---|---|
| `five_years.ogg` | Scene 14 (five-year montage), Scenes 16–17 (Sabra at work) | Solo piano or solo fiddle — resolute and measured, not sad but not celebratory |
| `kid_return.ogg` | Scene 15 (Yancey's homecoming and aftermath) | Bittersweet minor-key folk — slightly triumphant but undershadowed; two instruments at most |
| `war_march.ogg` | Scene 18 (Yancey enlists, rides south) | Building march energy — fife or tin whistle driving rhythm, stirs the blood without glorifying |

**Search terms (freemusicarchive.org / itch.io / opengameart.org):**
- `five_years`: "solo piano americana" or "contemplative folk" / "emotional piano RPG" / "quiet piano"
- `kid_return`: "minor folk guitar" or "appalachian fiddle" / "bittersweet folk" / "folk guitar sad"
- `war_march`: "civil war fife" or "rough riders march" / "historical march RPG" / "military folk march"

Place `.ogg` files in `game/audio/`. Convert from `.mp3` using Audacity (free).

---

## Mini Game Spec: Letters to the Editor (Scene 16)

### Narrative Setup
It's a Tuesday — press day minus two. The mail pouch has arrived and Sabra empties it onto the composing desk. Eight letters to the editor. She has space to print four. Jesse Rickey peers over her shoulder: "Don't print the one from Folsom. He still owes us for three months of advertising."

### The Eight Letters (fixed content)
| # | Sender | Position | Tags |
|---|---|---|---|
| 1 | A.J. Folsom, farmer | Against Indian land rights | anti-indian, conservative |
| 2 | Pete Pitchlyn (Cherokee lawyer) | For consolidated statehood | pro-indian, progressive |
| 3 | Mrs. Wyatt | Praise for women's club event | community, neutral |
| 4 | Shanghai Wiley | Praise for Yancey's cattle article | yancey, neutral |
| 5 | Anonymous | Rumor about Dixie Lee's establishment | gossip, community |
| 6 | A Ponca farmer | Request for news about reservation conditions | pro-indian, progressive |
| 7 | Oil Company Rep | Promotional letter for lease opportunities | oil, conservative |
| 8 | Unknown settler | Letter praising law and order after the Kid | frontier, yancey |

### Mechanic
- 8 letter cards laid out in two rows of 4
- Each card shows: sender name, one-line summary, a small tag icon
- Player clicks a card to read the full text (3–4 lines)
- After reading, player clicks PRINT (moves card to left "print" column) or SPIKE (moves to right "discard" bin)
- Must print exactly 4; both columns have 4 slots
- When all 8 are sorted, a "Go to Press" button appears

### Data Structures
```python
default letters_printed = []   # list of letter IDs (1–8) selected for print column
```

### Outcomes (checked after submission, cumulative)
| Condition | Effect |
|---|---|
| Letter 2 printed | `indian_sympathy += 1` |
| Letter 6 printed | `indian_sympathy += 1` |
| Letter 1 printed | `indian_sympathy -= 1` |
| Letter 7 printed | `indian_sympathy -= 1` |
| Letter 5 printed | `community_standing += 1` (readers love it) |
| Letter 5 NOT printed | `community_standing += 1` (respectable paper doesn't print rumor) — same reward, different flavor text |
| Letter 2 printed | `newspaper_stance += 1` |
| Letter 7 printed | `newspaper_stance -= 1` |
| Letter 4 or 8 printed | `yancey_relationship += 3` each (his name kept alive in print) |

*Note: outcomes are cumulative; a player can earn both `indian_sympathy +2` and `newspaper_stance +1` by printing letters 2 and 6.*

### Ren'Py Implementation Notes
- Screen name: `letters_minigame`
- Cards: `button` widgets with a backing frame; clicking opens `show screen letter_detail(letter_id)` overlay
- `letter_detail` screen shows full text + PRINT / SPIKE buttons calling `Return("print")` or `Return("spike")`
- Track state in `letters_printed` list; enforce 4-max with `sensitive len(letters_printed) < 4`
- "Go to Press" button: `sensitive len(letters_printed) == 4`; calls `Return(letters_printed)`
- Outcome logic runs in calling label `scene16_letters_result`
- Implementation file (when built): `minigame_letters.rpy`
