# Chapter 4 Plan — War Hero, Statehood, Oil
## Book Chapters XVI–XX | c. 1898–1907 | ~9 years

---

## Overview

Yancey returns from the Spanish-American War a hero in a Rough Rider uniform — and leaves again inside a year. Sabra runs the paper, runs the town, and raises two children alone. She defends her newspaper's independence through the statehood debate, the first oil strikes, and the trial of Dixie Lee — a trial that asks what kind of woman Osage wants to be. By the end of this chapter, Osage is a city, oil has changed everything, and Sabra Cravat is its most visible figure.

New variable introduced: `newspaper_stance` (negative = conservative, positive = progressive).

---

## New Characters (add to characters.rpy)

```renpy
define tracy = Character("Tracy Wyatt", color="#5F4F3B")
# Donna's eventual suitor; oil money. Introduced late Ch 4.
```

---

## New Backgrounds Needed

| Filename | Description |
|---|---|
| `bg_osage_street_1900` | Osage has sidewalks, a hotel, and one electric streetlamp |
| `bg_courthouse_interior` | Simple wooden courtroom; pine benches; a hanging oil lamp |
| `bg_oil_derrick_distant` | Prairie horizon with the first derricks, far away, like alien structures |
| `bg_wigwam_modern` | The Wigwam office, 1905-ish: a telephone on the wall, a newer press |
| `bg_civic_hall` | Women's club meeting room; chairs in rows; bunting on the wall |

---

## Scene 19 — "The Rough Rider Returns"
**Source:** Book Chapter XVI
**Time:** 1898, autumn

### Narration
Yancey rides into Osage in his Rough Rider uniform — the broad-brimmed khaki hat with the crossed sabers, the brown canvas coat. He looks like a recruiting poster. The town turns out to see him. He tells stories of Cuba, of Roosevelt, of the charge. Sabra stands beside him and feels simultaneously proud and furious.

He has been gone four months. She has run the paper, the house, and a good portion of the Territory. Four months was enough time for her to wonder whether she needed him home at all.

### Beats
1. Yancey rides in to a crowd on Pawhuska Avenue. Sol Levy and Doc Valliant are in the front row.
2. Speeches. Yancey speaks beautifully about the men who died.
3. Private reunion — the first evening alone.
4. Yancey tells her about Roosevelt; about the Cubans; about what he saw.

### Choice 1 — The Public Moment
> He is standing on a wagon bed, hat off, the setting sun behind him. The crowd is completely his. Sabra is beside him. She is part of the pageant.

- **"Stand beside him. Smile. This is his moment."**
  - `yancey_relationship += 5`
  - Narrator: *She gives him this freely. She knows what it costs and she gives it.*
- **"She steps back. Lets him have it alone."**
  - `sabra_independence += 1`
  - Narrator: *She is glad he is safe. But she is also, irrevocably, her own person now.*
- **"She waves to the crowd herself — a small gesture of partnership."**
  - `community_standing += 2`
  - Narrator: *The crowd cheers for her too. That is new.*

### Choice 2 — The Private Reunion
> They are finally alone. He is thinner. There are new lines around his eyes. He is thirty-eight years old and looks like a man who has been to war, which he has.

- **"Tell me everything. From the beginning."**
  - `yancey_relationship += 10`
  - He talks until midnight. She listens without interruption. It is one of the best nights of their marriage.
- **"I need to tell you what happened here while you were gone."**
  - `sabra_independence += 2`
  - She leads. He listens. This, too, is new.
- **"I'm glad you're home."** *(Simple, complete)*
  - `yancey_relationship += 5`
  - She means it without qualification. That is enough for tonight.

### Journal Entry 19
> *"He came home in a soldier's hat with the brim pinned up on one side. He still has both six-shooters. I counted: eight notches now."*

---

## Scene 20 — "Dixie Lee's Trial"
**Source:** Book Chapter XVII (implied) / Ch XV context
**Time:** 1899

### Narration
Dixie Lee has been charged under a new ordinance pushed by Osage's women's clubs. The charge: operating a disorderly house. The evidence is overwhelming. The conviction, with any other lawyer, would be certain. But Yancey takes her case. Pro bono. Because — he says — the law must be the same for everyone.

This is the scene that Sabra has dreaded and prepared for simultaneously. She sits in the gallery. She is the editor of the newspaper that will print the verdict.

### Beats
1. Yancey announces he will defend Dixie Lee. Sabra's reaction, private.
2. The courtroom. Half the town is there. The ladies of the Philomathean Club occupy one entire bench.
3. Yancey's argument: a woman who pays taxes and breaks no violence has the right to her trade.
4. The jury — nine men from the Territory — deliberates.
5. Verdict: not guilty. Yancey wins.
6. Dixie Lee, in the hallway: a brief moment between her and Sabra.

### Choice 1 — Sabra's Private Reaction (before the trial)
> She is alone with Yancey the night before. She could still ask him not to do this. She won't. But she can say what she thinks.

- **"I think you're wrong. She's not a victim — she chose this."**
  - `yancey_relationship -= 5`, `newspaper_stance -= 1`
  - Yancey: "Most of those girls didn't choose anything." The argument goes nowhere. They sleep on opposite sides of the bed.
- **"I think you're right. I hate that you're right."**
  - `yancey_relationship += 5`, `indian_sympathy += 1` (extends her capacity for hard truths)
  - He looks at her steadily. He has waited years for her to say something like this.
- **"Tell me the legal argument. I need to understand it."**
  - `newspaper_stance += 1`, `sabra_independence += 1`
  - She is not conceding; she is preparing. The editorial will be the hardest she has written.

### Choice 2 — The Editorial
> She sits at her desk the night after the verdict. The Wigwam goes to press Thursday. What does Osage need to read?

- **"The verdict was just. The law protected a woman others wanted to punish."** *(Support Yancey)*
  - `newspaper_stance += 2`, `community_standing -= 1` (loses some readers)
  - Yancey reads it and says nothing. He looks at her a long time.
- **"This court has failed Osage's women and children."** *(Oppose publicly)*
  - `newspaper_stance -= 2`, `community_standing += 2`
  - Half the town nods. Dixie Lee sends no note.
- **"Report the facts only. The community will decide."** *(Neutral)*
  - `newspaper_stance += 0`, `sabra_independence += 1`
  - The most journalistic choice. Also the loneliest.

### Choice 3 — Dixie Lee in the Hallway
> She is wearing dove gray again. She has not looked at Sabra directly since the Run. She looks at her now.

- **"I hope you find peace in whatever you do next."** *(Grace)*
  - `community_standing += 1`
  - Dixie Lee: "Thank you, Mrs. Cravat." That is all. It is enough.
- **"Your man won. That's all this is."** *(Cool, brief)*
  - A closed door. Neutral.
- **Say nothing. Walk past.**
  - `community_standing -= 1`
  - Narrator: *Sabra knows, walking away, that she is the smaller person. She keeps walking.*

### Journal Entry 20
> *"Not guilty. I sat in the gallery and watched the jury file in and I was not sure, until the foreman spoke, whether I wanted them to say guilty or not. I still don't know."*

---

## Scene 21 — "The Statehood Question"
**Source:** Book Chapter XVIII
**Time:** 1901–1906

### Narration
Oklahoma is debating statehood. The great question: will the Indian Territory and the white-settled Oklahoma Territory be joined into one state, or two? Yancey has always advocated consolidation — one state, both peoples. Sabra's paper has published both views. Now a decision is coming, and the Wigwam must take a stand.

This scene is an editorial board of one: Sabra at her desk, the arguments laid out, the Territory holding its breath.

### Beats
1. A delegation from the Double Statehood party comes to the Wigwam.
2. Then a delegation from the Single Statehood party.
3. Sabra writes an editorial. This is the paper's defining moment on the question.
4. Yancey's position (via letter from wherever he is) is clear: one state, the Indians included.

### Choice 1 — The Editorial Stance
> She has the arguments in front of her. She has Yancey's letter. She has her own years in this territory.

- **"Oklahoma Territory and Indian Territory must be one state. The people cannot be divided."**
  - `newspaper_stance += 2`, `indian_sympathy += 2`
  - A bold position that costs her some subscribers. It is also, she believes, correct.
- **"Two states is the safer, more stable choice for both peoples."**
  - `newspaper_stance -= 2`, `indian_sympathy -= 1`
  - The conservative position. She writes it carefully, without cruelty.
- **"The Wigwam cannot in good conscience advocate for either without more consultation with the affected communities."**
  - `newspaper_stance += 0`, `sabra_independence += 2`
  - She goes to the Osage Reservation. She talks to Pete Pitchlyn. She talks to the women's club. Then she writes.

### Choice 2 — Yancey's Letter
> He has written from — she doesn't know where — a long, characteristically passionate letter about the Indian's right to be part of the new state as equals.

- **"He's right. I'll say so."**
  - `yancey_relationship += 5`, `indian_sympathy += 1`
- **"He's not wrong, but he's not here. I'll decide this myself."**
  - `sabra_independence += 2`, `yancey_relationship -= 5`
- **"I'll print his letter. Let the readers see his argument."**
  - `newspaper_stance += 1` (opens the paper to his voice, separate from hers)

### Journal Entry 21
> *"November 16, 1907. Oklahoma is a state. They rang the church bell at noon and fired a cannon in the square and Doc Valliant came to the office with a bottle of whisky and said, 'Well, Sabra, we made it.' I said we did. I didn't say what I was thinking: that we made it without him."*

---

## Scene 22 — "The First Oil"
**Source:** Book Chapters XIX–XX
**Time:** 1905–1907

### Narration
A rancher near the Osage Reservation notices a rainbow sheen on the surface of his stock pond. Someone brings a geologist. The geologist brings investors. The investors bring chaos.

Oil. The word begins to appear in the Wigwam's pages. Sabra writes it with increasing frequency and uncertainty. It means money — more money than she has ever imagined — and it means something else, something she can't quite name.

### Beats
1. The first oil strike is reported in the Wigwam. Sabra writes the story herself.
2. Osage begins to change. Men with money arrive. The streets look different.
3. Cim — home from college in Colorado — is drawn into the oil world. He has geology training. Oil companies want him.
4. Sabra's editorial on oil: promise or corruption?

### Choice 1 — The Oil Story
> She is writing the headline. It is a real story — the biggest economic event in Oklahoma's history may be beginning.

- **"This is progress. I'll cover it fully — the good and the risk."**
  - `newspaper_stance += 1` (even-handed)
  - `community_standing += 1` (respected journalism)
- **"Oil brings the wrong kind of people. I'll be careful what I celebrate."**
  - `newspaper_stance -= 1` (cautious conservatism)
  - She is not wrong. She is also not entirely right.
- **"This is the story of the decade. The Wigwam will own it."**
  - `sabra_independence += 1`, `community_standing += 2`
  - Aggressive journalism. She sends letters to papers in New York and Chicago.

### Choice 2 — Cim and Oil
> Her son is twenty years old, home for the summer, and already the oil companies are circling. He has his father's magnetism and his mother's practicality. The combination makes him dangerous to himself.

- **"Cim, finish your degree first."**
  - `yancey_relationship += 0`; this is a Sabra-Cim relationship choice
  - He listens. He goes back to Colorado. (He will not stay.)
- **"If this is what you want, learn all of it before you commit."**
  - Practical maternal wisdom. He respects this.
- **"Your father would tell you to stay out of it. I don't know if he's right."**
  - `yancey_relationship += 5` (she invokes him as wisdom, not obstacle)

### Journal Entry 22
> *"The derricks on the horizon look like enormous iron insects. At night you can see the flare-off fires from the bedroom window. The smell of crude oil drifts into town when the wind blows from the northeast. I keep writing it up as progress. I'm not sure I believe myself."*

---

## Scene 23 — "What Yancey Left"
**Source:** Book Chapter XX (closing)
**Time:** 1907

### Narration
The chapter's closing scene. Yancey is somewhere — he has been somewhere for most of the last nine years. He sends letters occasionally. He appears rarely. When he appears, the town stops to watch. Sabra does not stop to watch anymore.

A letter arrives. He is in the Cimarron country, he says. He is working for something or other. He is coming home soon. He always says he is coming home soon.

Donna is fifteen. She wants to go east to school. Sabra has already arranged it.

### Beats
1. Sabra reads Yancey's letter at her desk.
2. She tells Cim and Donna about it — a family supper scene.
3. Donna announces she wants to go east. Sabra says yes immediately.
4. Cim says nothing. He is already thinking about the oil.
5. Sabra, alone at the end: she counts what she has, what she has built.

### Choice 1 — The Letter
> His handwriting is still large and slanted and full of underlines. She can hear his voice reading it aloud.

- **"Write back. Tell him what Donna is doing, what Cim is doing."**
  - `yancey_relationship += 5`
  - She does. She writes a careful, measured letter that is kinder than her feelings.
- **"File it with the others. Don't write back."**
  - `sabra_independence += 2`, `yancey_relationship -= 5`
  - She has dozens of his letters. She has kept them all. She has answered fewer and fewer.
- **"Read it to the children. Let them decide how they feel."**
  - A generous choice. She removes herself as interpreter of Yancey.

### Choice 2 — Taking Stock
> She is the editor of a newspaper, president of two civic organizations, mother of two, and the most recognizable woman in a hundred miles. What she is not: the wife of a man who stays.

- **"I chose this. I'd choose it again."** *(Acceptance)*
  - `sabra_independence += 1`, `community_standing += 1`
  - Narrator: *She means it. The freedom is real, even if it cost something she hadn't planned to pay.*
- **"It is what it is. Don't romanticize it."** *(Pragmatism)*
  - Neutral. Honest. No meter change.
- **"I'm still waiting. I don't think I'll stop."** *(Faithful)*
  - `yancey_relationship += 5`, `sabra_independence -= 1`
  - A quiet admission. Not weakness — just truth.

### Journal Entry 23
> *"Donna leaves for Miss Dignum's on the Hudson on Monday. She packed three times and was still dissatisfied. She has absolutely no aptitude for the frontier and I could not be more proud of her."*

---

## Chapter 4 Summary

| Variable | Expected range after Ch 4 |
|---|---|
| `yancey_relationship` | 20–75 |
| `sabra_direction` | -3 to +4 |
| `community_standing` | +4 to +12 |
| `indian_sympathy` | -4 to +9 |
| `sabra_independence` | 3 to 14 |
| `newspaper_stance` | -5 to +6 |

### Key Flags Set This Chapter
- `dixie_lee_editorial` — tracks which stance Sabra took in scene 20 (referenced in Ch 5's monument speech)
- `statehood_stance` — single or double statehood (referenced in Ch 5's congressional career)
- `journal_scene19` through `journal_scene23` — all True by chapter end

---

## Verification

- [x] Book chapters XVI–XX all represented
- [x] `newspaper_stance` has 5+ choice points
- [x] Dixie Lee trial included (scene 20)
- [x] Statehood debate included (scene 21)
- [x] First oil covered (scene 22)
- [x] Cim established as college-age, oil-adjacent
- [x] Donna's eastern education set up
- [x] Yancey's absences continue without explanation

---

## Mini Game Spec: Trial Arguments (Scene 20)

### Narrative Setup
The night before the trial. Yancey spreads six slips of paper on the kitchen table — argument notes for his defense of Dixie Lee. "I can't use them all," he says. "Three is the number. Opening, middle, close. You know a good argument, Sabra. Which three?"

He is asking her. She can't decide if this is an insult or a compliment.

### The Six Arguments (fixed content)
| # | Argument | Type |
|---|---|---|
| 1 | "She pays taxes — same as any merchant." | Legal / equality |
| 2 | "These women came to Oklahoma the same as everyone else — to survive." | Sympathy / humanity |
| 3 | "The ordinance is selectively enforced — only women are charged, not their customers." | Legal / hypocrisy |
| 4 | "The territory has no jurisdiction to regulate private commerce of this kind." | Legal / jurisdictional |
| 5 | "Half this jury has a standing account at the establishment in question." | Jury challenge (dramatic/risky) |
| 6 | "A woman's livelihood cannot be taken without due process." | Constitutional |

### Mechanic — Two Phases

**Phase 1 — Select:**
- 6 argument cards displayed
- Player clicks 3 to select (selected cards glow/highlight); a brief tooltip shows likely effect on hover
- "Proceed" button activates when exactly 3 are selected

**Phase 2 — Order:**
- The 3 selected cards move to a vertical stack with three labeled slots: OPENING / MIDDLE / CLOSING
- Player clicks a card to place it in the next available slot; clicking a placed card returns it
- "Present to Jury" button submits when all 3 slots are filled

### Outcomes — Selection
| Selection | Effect |
|---|---|
| Argument 2 selected | `yancey_relationship += 5` (she chose humanity over legalism; Yancey is moved) |
| Argument 3 selected | `newspaper_stance += 1` (legal hypocrisy angle resonates with Sabra's journalism instincts) |
| Argument 5 selected | `yancey_relationship += 3`, `community_standing -= 1` (bold; the jury is flustered) |
| Argument 6 selected | `newspaper_stance += 1` (principled constitutional frame) |
| Arguments 1 + 4 both selected | `newspaper_stance -= 1`, `yancey_relationship -= 3` (too dry; Yancey: "lawyerly mush") |

### Outcomes — Order Bonus
| Placement | Effect |
|---|---|
| Argument 2 in CLOSING slot | `yancey_relationship += 3` additional (emotional close lands hard) |
| Argument 5 in OPENING slot | `community_standing -= 1` (aggressive opener; jury bristles immediately) |
| Argument 6 in OPENING slot | `newspaper_stance += 1` (principled frame sets the right tone) |

*The verdict is always not guilty — the story requires it. The mini game shapes the editorial Sabra writes afterward and the conversation she has with Yancey that night.*

### Ren'Py Implementation Notes
- Screen name: `trial_arguments_minigame`
- Phase 1: 6 `button` widgets; `selected_args = []` list; `sensitive len(selected_args) < 3`; confirmed selection stored before phase 2
- Phase 2: 3 slot `frame` widgets (OPENING / MIDDLE / CLOSING); adapt the TypesetPlace/TypesetRemove pattern from Ch 1 for argument objects instead of letter tiles
- "Present to Jury" calls `Return((selected_args, ordered_args))`; outcome logic runs in calling label `scene20_trial_result`
- Implementation file (when built): `minigame_trial.rpy`
