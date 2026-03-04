# Chapter 5 Plan — Legacy & Monument
## Book Chapters XXI–XXV | c. 1907–1930 | ~23 years

---

## Overview

The final chapter. Oklahoma is a state, oil has made some people rich beyond imagination and left others in the dirt, and Sabra Cravat is a Congresswoman. Cim has married an Osage woman named Ruby Big Elk. Donna has married an oil baron. Yancey still roams. Then — quietly, in an oil field — he dies.

The chapter ends with the unveiling of a monument to the Oklahoma Pioneer. The sculptor has made it look like Yancey. Sabra decides, in the last moment, how she feels about that. The player's accumulated choices determine which of three endings she arrives at.

---

## New Characters (add to characters.rpy)

```renpy
define ruby = Character("Ruby Big Elk", color="#8B6914")
define tracy_wyatt = Character("Tracy Wyatt", color="#5F4F3B")
define krbecek = Character("Masja Krbecek", color="#888888")
```

---

## New Backgrounds Needed

| Filename | Description |
|---|---|
| `bg_osage_modern_1920` | Osage, 1920: automobiles, electric lights, oil money everywhere |
| `bg_kihekah_house_parlor` | The Cravat house on Kihekah Street, now comfortable: old mahogany, DeGrasse silver |
| `bg_washington_dc_hall` | A congressional hallway — marble, hushed |
| `bg_oil_field_bowlegs` | The raw, desperate Bowlegs oil field: mud, derricks, tin shacks, workers |
| `bg_monument_ceremony` | The ceremony square; a covered statue; a crowd; Oklahoma sky |

---

## Scene 24 — "Cim Brings Ruby Home"
**Source:** Book Chapter XXII
**Time:** c. 1910

### Narration
On a Saturday, a large limousine pulls up in front of the house on Kihekah Street. Big Elk and his wife sit in the parlor — formal, ceremonial. Cim has not been home for months. Sabra enters.

Cim has married Ruby Big Elk, daughter of an Osage headman. She is twenty years old, quietly beautiful, entirely composed.

This is the choice Sabra has been approaching for twenty years, without knowing it. Every conversation about Indians — every moment of sympathy or contempt — has been practice for this room, this afternoon, this daughter-in-law.

### Beats
1. Sabra enters the parlor and sees Big Elk and his wife.
2. Cim enters from the hallway with Ruby. "Mother, this is my wife."
3. Big Elk's formal speech of greeting (through Ruby, who translates).
4. Sabra's response — the central choice of the chapter.
5. Yancey's reaction (via letter): "Of course. Who else would Cim marry?"

### Choice 1 — Sabra's Response to Ruby
> The room is very quiet. Cim is watching his mother. Ruby is watching nothing in particular, with the Indian patience that Sabra has never understood.

- **"Welcome to our family." *(And mean it)*
  - `indian_sympathy += 3`
  - `yancey_relationship += 5` (she hears Yancey in herself)
  - Narrator: *She takes Ruby's hands. Ruby's grip is firm and brief. Big Elk nods once. Cim exhales.*
  - Unlocks: ending path "The Land Belongs to All"

- **"I need time."** *(Honest but not cruel)*
  - No immediate meter change; flagged for later
  - Narrator: *She steps forward. She shakes Ruby's hand formally. She says the words. But Ruby sees through them — Ruby would always see through her.*
  - Sabra grows into acceptance over the next scenes.

- **"My son chose this. I will be civil."** *(Duty without warmth)*
  - `indian_sympathy -= 1`, `yancey_relationship -= 5`
  - Narrator: *She keeps the smile in place. It is the exact smile her mother Felice used on people she considered beneath her. She recognizes it only later.*
  - Closes off: "The Land Belongs to All" ending unless recovered in later scenes

### Choice 2 — Big Elk's Formal Speech
> He has brought three words through Ruby: *We are glad.* He means: *We hope you will be worthy of our daughter.* Sabra hears: *We accept this.*

- **"Tell him — I hope to know him better."**
  - `indian_sympathy += 1`
- **"The formalities are appreciated." *(Polite but distant)*
  - Neutral.
- **"Tell him he's welcome here whenever he comes to Osage."**
  - `community_standing += 1`, `indian_sympathy += 1`
  - The door, open.

### Journal Entry 24
> *"Cim's wife has his same quality of stillness — the ability to be entirely present without pushing. I don't know what to do with that. I'm trying."*

---

## Scene 25 — "The Congresswoman"
**Source:** Book Chapters XXIII–XXIV
**Time:** c. 1920

### Narration
Osage. The Wigwam. Sabra's life has grown into something she couldn't have designed in 1889 — too large, too full of public weight. She has been asked to run for Congress. Not by the women's clubs this time: by the state party.

A compressed scene of Sabra's congressional career: the campaign, the issues she chooses to champion, her advocacy for Indian rights on the floor of the House.

### Beats
1. The nomination offer. The party asks her to run.
2. Sabra's platform: two choices she will advocate for.
3. A brief montage of Washington: marble corridors, Senators who underestimate her.
4. She introduces a bill for further protection of Osage oil rights.

### Choice 1 — Whether to Run
> She is fifty-two years old and has been the best argument for women in public life that Oklahoma has ever produced, without trying. Now they are asking her to try.

- **"Yes. I'll run."**
  - `community_standing += 3`, `sabra_independence += 2`
  - She wins. Of course she wins.
- **"Yes. For one term."**
  - `community_standing += 2`, `sabra_independence += 1`
  - A modest yes. She will stay longer than she planned.
- **"Someone else should have this. Someone younger."**
  - `community_standing -= 1`
  - The women's club talks her back into it. She allows herself to be talked back.

### Choice 2 — Her Primary Issue in Congress
> She has a seat at the table. She can spend it on what Osage needs, or what Oklahoma needs, or what she believes in.

- **"Indian reservation reform. The system is unjust and I'll say so."**
  - `indian_sympathy += 3`, `newspaper_stance += 1`
  - Radical enough to make enemies. She makes them.
  - Unlocks: "The Land Belongs to All" ending path (boosts requirement)
- **"Oklahoma needs oil law reform. The fields are lawless."**
  - `newspaper_stance += 1`, `community_standing += 1`
  - Practical, popular, and necessary.
- **"Education. Especially for Indian children leaving the reservation schools."**
  - `indian_sympathy += 2`, `community_standing += 2`
  - A bridge position. She builds coalitions. Some things actually change.

### Journal Entry 25
> *"A Senator from Pennsylvania told me Oklahoma needed a woman Governor. He said it as a joke. I wrote it down."*

---

## Scene 26 — "Donna's Wedding / The Oil Baron"
**Source:** Book Chapter XXIII
**Time:** c. 1916

### Narration
Donna Cravat, now twenty-five and everything her mother made her, marries Tracy Wyatt — oil money, old money, the kind of settled prosperity that Sabra dreamed of in Wichita and gave up for a tent on the Oklahoma prairie. It is a beautiful wedding. It is also, Sabra recognizes quietly, the victory of everything she was afraid of.

A short, bittersweet scene.

### Beats
1. The wedding ceremony.
2. Tracy Wyatt: wealthy, handsome, reliable. Everything Yancey was not.
3. A private moment: Donna in her wedding dress, alone with Sabra for five minutes.
4. Sabra gives Donna the coverlet Mother Bridget gave her on the morning they left Wichita.

### Choice 1 — What Sabra Tells Donna
> Five minutes in a back room. Donna is composed, as she always is. She is her grandmother Felice's grandchild, and her mother's daughter, which means she has both the armor and the nerve.

- **"You've chosen well. You always choose well."**
  - `community_standing += 1`
  - Narrator: *It is true. But Sabra wonders, briefly, whether choosing well and living fully are the same thing.*
- **"Whatever comes — you'll manage it. You're Cravat stock."**
  - `sabra_independence += 1`
  - She means: *You don't need anyone to save you.* Donna already knows.
- **"I hope he makes you happy." *(Quietly)*
  - `yancey_relationship += 5`
  - Narrator: *She is thinking, unexpectedly, of her own wedding morning. The white sombrero. The impossible man.*

### Journal Entry 26
> *"Donna's wedding was beautiful and organized and Tracy Wyatt arrived exactly on time. I cried once, briefly, in the back room. Then I came out and ran the reception."*

---

## Scene 27 — "The Word from Bowlegs"
**Source:** Book Chapter XXV
**Time:** 1930

### Narration
Sabra is in the new oil town of Bowlegs on a congressional fact-finding trip. The town is everything old Osage was — raw, violent, desperate — except worse. A Harvard boy in bone-rimmed glasses is showing her group around.

Then: an eruption in the field. Nitroglycerin shoots upward with the oil pressure. A man — an old man — runs out from the crowd and catches the can on his chest before it hits the ground. He saves forty lives. He is dying.

They carry him to the dirt. The crowd parts for Sabra's white hair.

### Beats
1. Sabra in Bowlegs — the trial of the dance-hall girl; the man in the pen; the Harvard boy.
2. The eruption. A man runs back like an outfielder.
3. He catches it.
4. The crowd parts.
5. Yancey is on the ground.

This scene is narration-forward with minimal choices. The player watches. The weight of all previous choices gathers here.

### Narration Beat
*He opens his eyes — those ocean-gray eyes, the long curling lashes like a girl's. She has thought of them often. Glazed, now. Then: they clear.*

*His lips move. He is quoting something she doesn't recognize. She has never heard of Peer Gynt.*

> **"Wife and mother — you stainless woman — hide me — hide me in your love."**

*She doesn't know it is a play. She only knows what he is asking.*

### Choice — Her Last Words to Him
> He is dying in the oil-soaked dirt and she is holding his head and the crowd has gone silent. She doesn't know what she knows, only that she is here and he is here and this is the last time.

- **"You came back."** *(Forgiveness)*
  - `yancey_relationship` checked: if ≥ 50, this choice is available
  - She says it like she means it: *You always came back.* He hears it.

- **"Sleep. You're safe."** *(The words of Solveig)*
  - Available always; the truest response
  - She becomes, without knowing it, Solveig. The play ends as it must.

- **"I'm here. I'm here."** *(Just presence)*
  - Available always; the simplest and the most complete

*His eyes close.*

*"Sleep, my boy, my dearest boy."*

### Journal Entry 27 — not a journal entry; a silence.
*The scene ends without narration. The lights fade on Sabra alone.*

---

## Scene 28 — "The Monument" (Ending Scene)
**Source:** Book Chapter XXIV (closing)
**Time:** 1930, one year after Yancey's death

### Narration
The ceremony. Five hundred thousand dollars. The sculptor Krbecek — a quiet snuffy little Pole in glasses — has used Yancey's photographs. The statue shows a man with a great buffalo head, stepping forward in high-heeled boots and a Prince Albert coat, one hand on his holster. Behind him, a blanketed Indian stumbles for support.

Sabra stands at the unveiling and looks at it. All the meters, all the choices, all the years — they determine how she sees herself in this moment.

---

## Ending Branch Logic

### Branch 1 — "She Was His Shadow"
**Condition:** `sabra_independence <= 4` AND `yancey_relationship >= 65`

The statue is revealed. It is Yancey — magnificent, perfectly right. Sabra looks at it and feels something like peace. She spent her life beside this man, and it was a life worth living.

**Closing Narration:**
> "She stood at the foot of the statue and looked up at his face — the great menacing head, the long coat, the brilliant boots — and felt, for the first time in many years, that she was exactly where she was supposed to be. Beside him. As she had always been."

**Journal Entry 28:**
> *"They made it look like him. It's the right thing. He was what this land was — impossible, larger than life, more beautiful than practical. I was the one who kept the books."*

---

### Branch 2 — "She Built It Herself"
**Condition:** `sabra_independence >= 8` AND `community_standing >= 8`

The statue is revealed. Yancey's face. Yancey's boots. Sabra looks at it and — for a long moment — sees it from the outside, the way a visitor would. A magnificent man. Not the whole story. Not even the most important part of the story. She knows what she built. This territory knows it too.

**Closing Narration:**
> "The sculptor said it was the Spirit of the Pioneer. She supposed he was right. She looked at the statue for a long time. Then she turned and spoke to the Senators, the editors, the oil men. She spoke for twenty minutes without notes. Afterward, a young woman from the Tulsa paper asked who had taught her to write. 'No one,' Sabra said. 'I had a newspaper and no choice.'"

**Journal Entry 28:**
> *"They built a monument to the Pioneer. They should have built two. But I have the paper, and the paper will say what needs saying. It always has."*

---

### Branch 3 — "The Land Belongs to All"
**Condition:** `indian_sympathy >= 7` AND (`sabra_independence >= 5` OR `yancey_relationship >= 50`)

The statue is revealed. Yancey, stepping forward — and the blanketed Indian behind him, reaching for his shoulder. Cim and Ruby are in the front row. Their daughter — Sabra's granddaughter, who has her grandfather's gray eyes and her grandmother's black hair and Osage blood — looks up at the statue.

**Closing Narration:**
> "The Indian behind him reaches out, she saw now. Not stumbling. Reaching. She looked at her son's daughter, who was looking at the statue with the Indian patience that Sabra had spent forty years learning to see. 'What do you think?' Sabra asked her. The girl tilted her head. 'He's big,' she said. 'And he's holding on.'"

**Journal Entry 28:**
> *"Her name is Sabra, after me — but she has Cim's face and Ruby's stillness. She will outlast us all. The land belongs to her. It always did."*

---

## If No Branch Condition Is Met

Fallback to Branch 1 (the most forgiving path). This should be nearly impossible with normal play, but is included for safety.

---

## Chapter 5 Summary

| Variable | Threshold for Branch |
|---|---|
| `sabra_independence` | Low (≤4) → Branch 1; High (≥8) → Branch 2; Mid with high sympathy → Branch 3 |
| `yancey_relationship` | High (≥65) → Branch 1 available; Mid (≥50) → Branch 3 available |
| `community_standing` | High (≥8) → required for Branch 2 |
| `indian_sympathy` | High (≥7) → required for Branch 3 |

---

## Verification

- [x] Book chapters XXI–XXV all represented
- [x] Three ending branches each reachable from plausible playthroughs
- [x] Branch 1 accessible by high-yancey / low-independence path (pure romantic player)
- [x] Branch 2 accessible by civic leadership / editorial independence path
- [x] Branch 3 accessible by consistent pro-Indian sympathy choices across all chapters
- [x] Yancey's death handled with full source fidelity (Peer Gynt quote, nitroglycerin catch)
- [x] Cim/Ruby marriage (scene 24) is the pivotal gate for Branch 3
- [x] All journal entries written or noted as silence
- [x] New characters (Ruby, Tracy Wyatt, Krbecek) listed for characters.rpy
