# Chapter 2 Plan — Building Osage
## Book Chapters VIII–XII | c. 1890–1894 | ~4 years

---

## Overview

Osage is real now — a town with streets, a newspaper, grudging neighbors, and the first whisper of law. Sabra is no longer just Yancey's wife; she is the woman who keeps the Wigwam running while her husband tilts at windmills. This chapter is about Sabra finding her footing: in the community, in marriage, in the Territory itself.

New variables introduced: `community_standing`, `indian_sympathy`.

---

## New Characters (add to characters.rpy)

```renpy
define doc = Character("Doc Valliant", color="#8B7355")
define arita = Character("Arita Red Feather", color="#8B4513")
define pete = Character("Pete Pitchlyn", color="#6B8E23")
define dixie = Character("Dixie Lee", color="#8B0032")
define kid = Character("The Kid", color="#333333")
```

*(Sol Levy, Lewis, Felice, Isaiah, Sabra, Yancey defined in Ch 1)*

---

## New Backgrounds Needed

| Filename | Description |
|---|---|
| `bg_wigwam_office_interior` | Inside the print shop: type cases, ink smell, windows onto the street |
| `bg_osage_street_1890` | Pawhuska Avenue, 1890: wooden storefronts, red dust, no trees |
| `bg_church_tent_service` | Canvas tent interior, roulette table as pulpit, oil lamps overhead |
| `bg_bedroom_frontier` | Small, spare bedroom; wind rattling the window |
| `bg_osage_homestead_yard` | Back yard of the Cravat house; a well, a few scraggly trees |

---

## Scene 8 — "The Lion in the Streets"
**Source:** Book Chapter VIII–IX
**Time:** 1890, a Sunday

### Narration
Yancey has been asking around town about the Pegler murder. Today is Osage's first church meeting — held in Grat Gotch's gambling tent. Everyone comes: cowboys, settlers, a row of Osage and Ponca Indians in blankets along the back wall. And then — Dixie Lee and her six girls, plumes and parasols, announced by the rustle of silk.

### Beats
1. Sabra notices the Indians at the back of the tent — a silent frieze.
2. Dixie Lee's entrance. Yancey flushes. He whispers: "That's the girl. From the Run."
3. Yancey leaps onto the roulette table and begins preaching — with a Bible and two six-shooters.
4. Mid-sermon: a shot from the back. Yancey ducks (drops his Bible), fires from the hip. Lon Yountis is dead.
5. "—Lon Yountis," Yancey finishes his sentence.

### Choice 1 — The Indians
*After Sabra notices the Indians ranged along the back wall.*

> Sabra studies the row of faces — Osage, Ponca, Cherokee — impassive as bronze. She has been told they are dangerous. She has also been told a good many things that turned out to be false.

- **"Keep Donna close. They make me uneasy."**
  - `indian_sympathy -= 1`
  - Sabra holds Donna tight, eyes forward.
- **"They've come to worship too. That seems right."**
  - `indian_sympathy += 1`
  - Sabra gives the nearest Indian woman a small nod. The woman does not respond. But she doesn't look away either.

### Choice 2 — Dixie Lee's Entrance
*After Dixie Lee's procession sweeps the tent.*

> Yancey's face has gone dark with something Sabra can't name. She has never seen him blush before. The memory of the Run — of the woman on the thoroughbred who took their land — rises in her throat like bile.

- **"Tell me what's happening. I deserve to know."** *(Press him)*
  - `yancey_relationship -= 5`
  - He whispers the story — curtly, reluctantly. She feels the truth like a slap.
- **"This is a church service. I will not make a scene."** *(Hold yourself together)*
  - `community_standing += 1`
  - Sabra sets her face into a mask. She will ask questions later, in private.
- **"Sit here. Don't look at her."** *(Practical)*
  - Neutral. A quiet choice that keeps peace without solving anything.

### Choice 3 — After the Shooting
*Yountis is dead on the tent floor. Yancey calls for prayer — guns still drawn.*

> The crowd is silent. Cim is trembling against Sabra's side. Around her, Osage holds its breath, deciding what it will do with a man who just killed someone in church.

- **"I'm proud of him."** *(Admiration)*
  - `yancey_relationship += 5`, `sabra_admires_yancey = True` (carry from Ch1 flag)
  - Narrator: *This is the man she married. Wild, alarming, magnificent.*
- **"My son just watched his father shoot a man dead."** *(Fear and grief)*
  - `yancey_relationship -= 5`
  - Narrator: *Cim is four years old. He will remember this his whole life. She is sure of it.*
- **"The town needed this. Someone had to do it."** *(Frontier pragmatism)*
  - `community_standing += 1`
  - Narrator: *Pegler's murderer is dead. There is something cold and clarifying about that fact.*

### Journal Entry 8
> *"The first church meeting of Osage was conducted from a roulette table, with two six-shooters for a cross. We sang a song called 'Who Were You at Home?' — and the answer, for most in that tent, is: someone else entirely."*

---

## Scene 9 — "Seven Notches"
**Source:** Book Chapter X
**Time:** 1890, the day after the tent service

### Narration
Sabra confronts Yancey in private about the killings. She sees the notches carved into his pistol grips. Seven men. She had not known. She had not let herself know.

### Beats
1. Sabra counts the notches. Two on one gun, five on the other, counting Yountis.
2. She asks about Dixie Lee — the conversation from the street, in full view of everyone.
3. Yancey explains his position: "Would you have liked to see Yountis get me?"
4. Sabra presses him on Dixie Lee — the stolen quarter section, the chummy street chat.
5. Yancey: "I can hate a person and still find them interesting." Sabra cannot understand this.

### Choice 1 — The Notches
> "Six men," she said. And then, because she could not help it: "Oh, Yancey. You haven't killed six men."

- **"Was it always necessary? Every time?"**
  - Yancey tells her each story, briefly. She listens.
  - `yancey_relationship += 5` (she tries to understand)
- **"I won't ask. I don't want to know."**
  - `yancey_relationship -= 5` (avoidance breeds distance)
  - Narrator: *She will regret not asking. But not today.*

### Choice 2 — Dixie Lee
> Sabra has chosen her words with care. She is not a woman who screams. But she is also not a woman who lets things pass unnoticed.

- **"You spoke to her in the street like an old friend."**
  - `yancey_relationship -= 5`
  - Yancey: "I can talk to a woman without endorsing what she does." He is not wrong. Sabra hates that he is not wrong.
- **"I don't care about her. I care that you care."**
  - `yancey_relationship += 5`
  - A truer conversation. Yancey goes quiet, then: "You're right. I do find her interesting. I'm sorry that bothers you."
- **"If she sets up her house, I want nothing to do with it — or with anyone who does."**
  - `community_standing += 1` (Sabra aligns with the respectable women of Osage)
  - She is drawing a line. She knows it.

### Journal Entry 9
> *"Seven notches. I have been married to this man for five years and I did not know. What else don't I know?"*

---

## Scene 10 — "The Wigwam Lives"
**Source:** Book Chapters X–XI (early)
**Time:** 1890–1891

### Narration
The Oklahoma Wigwam publishes its second issue — and its hundredth. Sabra is learning typesetting. She writes the society column. She knows every family in a hundred-mile radius. Yancey writes the editorials (when he's there). Doc Valliant appears as a drunk, sardonic, brilliant physician — and an unexpected friend. Dixie Lee's establishment opens at the far end of Pawhuska Avenue; the ladies of Osage pretend not to see it.

### Beats
1. A morning in the print shop. Jesse Rickey is drunk again. Sabra sets type herself.
2. Doc Valliant arrives — Yancey's friend, reliable when sober, a disaster when not.
3. A delegation of Osage's respectable women asks Sabra to write a letter protesting Dixie Lee's establishment.
4. Yancey's position: Dixie Lee pays taxes, she's as legitimate as any of them.

### Choice 1 — The Delegation
> Mrs. Wyatt has brought six wives. They are dressed in their best. They want a public statement in the Wigwam.

- **"I'll write the letter."**
  - `community_standing += 2`, `indian_sympathy += 0` (no effect)
  - Sabra writes a careful, firm editorial. The women of Osage are grateful. Dixie Lee sends a brief note: "Well played."
- **"I can't print it without Yancey's approval — this is his paper."**
  - `community_standing -= 1` (seen as weak)
  - The women leave disappointed. Sabra watches them go and feels like a coward.
- **"The paper is for news, not campaigns. If you want a petition, circulate it yourself."**
  - `sabra_direction += 1` (frontier pragmatism)
  - An independent position that the women dislike but cannot argue with.

### Choice 2 — Doc Valliant
> He has a medical bag, a flask, and opinions about everything. He is the only doctor within thirty miles.

- **"We're glad to have him. The Territory needs a doctor more than it needs a sober one."**
  - `indian_sympathy += 1` (Doc has Osage patients; Sabra's openness extends)
  - Doc Valliant will remember this kindness.
- **"I won't have him in this office when he's been drinking."**
  - `community_standing += 1`
  - A reasonable position. Doc Valliant respects it, mostly.

### Journal Entry 10
> *"I can set eight hundred words an hour now. Jesse Rickey showed me, which is perhaps the most useful thing a drunk has ever done for me."*

---

## Scene 11 — "The Wind and Donna"
**Source:** Book Chapter XI
**Time:** June 1891

### Narration
Sabra's second child is born. A girl. The birth is not the ordeal she feared — it is the Oklahoma wind that nearly breaks her, howling through the house during her labor. She refuses to send for her mother. Arita Red Feather, the quiet Osage girl Yancey hired, is the one who sits with her.

### Beats
1. The labor. Doc Valliant is — miraculously — sober enough to attend.
2. The wind. Sabra, delirious with pain, begs Yancey to shoot it. Seven notches. One more.
3. The baby: a girl. They name her Donna.
4. A quiet moment: Arita Red Feather changes the baby's wrappings with practiced hands. Sabra watches.

### Choice 1 — Donna's Arrival
> The baby is here, red-faced and furious with the world. Sabra holds her and feels something shift.

- **"She won't grow up wild like this place."**
  - `sabra_direction -= 1` (the Refined Lady pulling at her)
  - Narrator: *She has already decided: Donna will have everything Sabra didn't.*
- **"She's a frontier girl. This land made her."**
  - `sabra_direction += 1`
  - Narrator: *Oklahoma clay in her bones from the first breath.*
- **"I'll do whatever she needs. I don't know yet what that is."**
  - Neutral. A wise answer. Parenthood in the Territory is improvisation.

### Choice 2 — Arita Red Feather
> Arita moves around Sabra's bedroom without being asked: water, clean cloth, the quieting of the baby. She has never spoken much. She speaks even less now.

- **"Thank you. Genuinely."** *(Acknowledge her)*
  - `indian_sympathy += 2`
  - Arita nods. For a moment something moves in her dark eyes. Sabra sees it.
- **"She's useful. I'm glad Yancey thought of it."** *(Indifference)*
  - `indian_sympathy -= 1`
  - Narrator: *It does not occur to Sabra to wonder what Arita's own life is like.*

### Journal Entry 11
> *"Her name is Donna. She has black hair and Yancey's gray eyes and she screamed for an hour about the wind. She's mine."*

---

## Scene 12 — "Respectability"
**Source:** Book Chapters XI–XII
**Time:** 1891–1893

### Narration
Osage grows up around the Cravats. Sol Levy's hardware store has a glass front now. There's a school. There's a hotel. There are clubs — the women of Osage are forming clubs. Pete Pitchlyn, the half-Cherokee lawyer, becomes an ally and eventually a friend to Yancey (and a curiosity to Sabra). A visiting photographer comes through and takes portraits of the town.

Yancey is restless. More and more often, he is not there when Sabra needs him.

### Beats
1. Sabra attends the first meeting of a women's civic club.
2. She meets Pete Pitchlyn — half-Cherokee lawyer, sophisticated, cool.
3. A town photographer wants to photograph the newspaper office.
4. Yancey disappears for three days without explanation. Returns with a story about a cattlemen's dispute in the hills.

### Choice 1 — The Women's Club
> The wives of Osage's merchants and professionals are organizing. They need a president or a secretary or both. They need someone who knows how to write a sentence.

- **"I'll join. But I won't be secretary — I'll be president."**
  - `community_standing += 2`
  - Sabra becomes the woman who runs things. She discovers she is good at it.
- **"I'll come when I can. The paper keeps me busy."**
  - `community_standing += 1`
  - A hedge. She's interested but unwilling to commit. It satisfies no one fully.
- **"A wives' club feels premature. Let's build a school first."**
  - `sabra_direction += 1`, `community_standing += 1` (respected for the practicality)
  - She redirects the energy. The school gets built six months earlier than it otherwise would have.

### Choice 2 — Pete Pitchlyn
> Pitchlyn is half-Cherokee, Harvard-educated, and entirely at ease in both worlds. He looks at Sabra with calm, curious eyes.

- **"He makes me uneasy. I don't know why."**
  - `indian_sympathy -= 1`
  - Narrator: *She knows why. She doesn't want to know.*
- **"He's interesting. I want to understand his position."**
  - `indian_sympathy += 1`
  - She asks him what the Cherokee think of the Run. He tells her, precisely and without softening. She listens.
- **"He's Yancey's friend. That's good enough for me."**
  - Neutral. Sabra is generous but not yet curious.

### Choice 3 — Yancey's Disappearance
> Three days. No note. When he comes back he is dusty and apologetic and utterly alive in a way he never quite is when he stays put.

- **"You can't keep doing this to me."**
  - `yancey_relationship -= 5`
  - He promises. He keeps the promise for two months.
- **"Tell me about the hills."** *(Listen)*
  - `yancey_relationship += 5`
  - He tells her about the cattlemen. She realizes: this is who he is. The question is whether she can live with it.
- **"I need you here. The children need you here."**
  - `yancey_relationship -= 5`
  - A fair plea. He hears it and sets it aside. The hills called louder.

### Journal Entry 12
> *"Sol Levy's store has a plate glass window now. I can see my reflection in it when I walk past. I keep looking, a little surprised by what I see."*

---

## Scene 13 — "The Cherokee Strip"
**Source:** Book Chapter XII (late), transition to Ch XIII
**Time:** Summer 1893

### Narration
President Cleveland has proclaimed a new Run — the Cherokee Strip, six million acres. All of Osage is talking about it. Yancey's eyes are blazing. He wants to go. He wants to bring Sabra and the children. He wants to start again on a ranch. She refuses with everything she has.

This scene ends with Yancey riding out on his mare Cimarron. He turns in the saddle and waves his white sombrero. "Five years passed before she saw him again."

### Beats
1. Yancey announces the Cherokee Strip Run at supper.
2. He proposes they sell the Wigwam, make the Run, start a cattle ranch.
3. Sabra refuses violently. A rare and genuine fight.
4. Yancey cannot be stopped. He prepares to go.
5. Sabra runs after the departing cavalcade. One last embrace. He asks her to come with him. She refuses.
6. The wide Oklahoma sky swallows him.

### Choice 1 — The Fight
> She is screaming. She cannot stop. Five years she has fought for this place — this paper, these children, this life — and he wants to throw it all away for another run across open prairie.

- **"You'll leave us for nothing. For a dream."**
  - `yancey_relationship -= 10`
  - Bitter and true. He flinches. He goes anyway.
- **"I understand why you need this. I just can't follow you."**
  - `yancey_relationship -= 5`
  - A sadder conversation. She is not wrong; neither is he.
- **"Take Cim. Leave Donna with me. At least give the boy what he wants."**
  - `yancey_relationship += 0`, `sabra_direction += 1`
  - A compromise that falls apart: Cim howls to go but Sabra keeps him home. She can't let him go too.

### Choice 2 — The Last Goodbye
> He bends from the saddle and lifts her in one arm. He is immense and warm and going away.

- **"Come back. Promise me you'll come back."**
  - `yancey_relationship += 5`
  - He says nothing. He sets her down gently. He rides.
- **"Where are you going? Where are you really going?"**
  - A premonition she can't explain. He doesn't answer. He rides.
  - This flags `yancey_mystery = True` — used in Ch 3 to unlock a new scene option.
- **"Go. But this time, I won't wait."**
  - `sabra_independence += 2` (early, strong signal)
  - She means it. She doesn't know yet what she means.

### Journal Entry 13
> *"He took the mare named Cimarron and rode northwest into the dust. Cim cried for two days. Donna is too young to understand. I have a newspaper to get out by Thursday."*

---

## Chapter 2 Summary Variables

At end of Ch 2, tally and display a brief summary panel:

| Variable | Likely range after Ch 2 |
|---|---|
| `yancey_relationship` | 30–65 |
| `sabra_direction` | -3 to +4 |
| `community_standing` | 0 to +7 |
| `indian_sympathy` | -3 to +5 |

---

## New Backgrounds Summary

```
bg_wigwam_office_interior
bg_osage_street_1890
bg_church_tent_service
bg_bedroom_frontier
bg_osage_homestead_yard
```

---

## Verification

- [x] All five book chapters (VIII–XII) represented across 6 scenes
- [x] `community_standing` has 5+ choice points
- [x] `indian_sympathy` has 4+ choice points
- [x] `yancey_relationship` continues to develop with meaningful swings
- [x] Dixie Lee introduced; trial deferred to Ch 4
- [x] Donna born (scene 11); Ch 1 Cim established
- [x] `yancey_mystery` flag planted in scene 13 for Ch 3 use

---

## Music

| Filename | Used in | Mood |
|---|---|---|
| `osage_sunday.ogg` | Scene 8 (church service), Scene 12 (women's club) | Frontier revival hymn — fiddle and banjo, energetic but raw, slightly chaotic |
| `wigwam_press.ogg` | Scenes 9–10–12 (newspaper work, domestic scenes) | Steady and purposeful — solo guitar or quiet piano, workmanlike |
| `cherokee_strip.ogg` | Scene 13 (Yancey leaves) | Wide and lonely — melancholy fiddle over open drone, no percussion |

**Search terms (freemusicarchive.org / itch.io / opengameart.org):**
- `osage_sunday`: "old time revival" or "shape note singing" / "americana folk RPG OST" / "frontier hymn"
- `wigwam_press`: "acoustic fingerpicking" or "country blues" / "western town ambience" / "western acoustic"
- `cherokee_strip`: "americana elegy" or "solo fiddle" / "melancholy folk" / "sad western"

Place `.ogg` files in `game/audio/`. Convert from `.mp3` using Audacity (free).

---

## Mini Game Spec: The Church Collection (Scene 8)

### Narrative Setup
Yancey declares from the pulpit: "Any miserable tightfisted skinflint putting in less than two bits will be thrown out by me personally." He deputizes Southwest Davis and Ike Bixler to pass two sombreros through the crowd. As Sabra watches from the front pew, she spots several faces that look … shifty.

### Mechanic
- 8 congregation members appear in a row, each holding a coin bag
- A sombrero travels left-to-right across the row over 30 seconds
- Three of the eight will try to drop in a penny or nothing (shown by a subtle tell: eyes averted, hand moving too quickly, coin bag suspiciously flat)
- Player clicks a congregation member to flag them *before* the hat passes them; late flags don't count
- Yancey calls out anyone flagged; they're escorted to the door

### Data Structures
```python
default collection_caught = 0   # number of cheapskates correctly flagged
default collection_total  = 0   # final collection amount (narrative only)
```

### Outcomes
| Result | Effect |
|---|---|
| 3/3 caught | `community_standing += 2`; Yancey: "Best congregation I ever robbed." |
| 2/3 caught | `community_standing += 1`; collection total "a little short of expected" |
| 0–1 caught | `community_standing += 0`; one cheapskate later complains in the Wigwam letters column (sets flag for Ch 3 Letters game) |

### Ren'Py Implementation Notes
- Screen name: `church_collection_minigame`
- Use a `timer` displayable (counts down 30 s) driving a Python variable for hat position
- Congregation row: 8 `imagebutton` or `button` widgets in an `hbox`
- The "tell" for each cheat: a visual state change (e.g. slightly different expression image) that appears briefly then disappears — timed with `renpy.show` / `renpy.hide` or ATL
- The hat's position is an ATL `transform` moving across the hbox; when it passes member N, flagging member N is disabled
- Result returned via `Return(collection_caught)` to the calling label; outcome logic runs in label `scene8_collection_result`
- Implementation file (when built): `minigame_collection.rpy`
