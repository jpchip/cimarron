# Dialogue Choice Audit — Cimarron Visual Novel

**Date:** 2026-04-26
**Scope:** All five chapters; all `menu:` blocks across the playable script.
**Purpose:** Inventory every player choice — label context, chapter, source novel chapter reference, choices available, and the variables each choice modifies — to support QA, balance review, and narrative design continuity work.

---

## Variable Reference Summary

| Variable | Default | Range / Values | Role |
|---|---|---|---|
| `yancey_relationship` | 50 | 0–100 | Sabra's connection to Yancey |
| `sabra_direction` | 0 | negative = Refined Lady; positive = Frontier Woman | Character arc track |
| `sabra_independence` | 0 | unbounded positive | Self-sufficiency growth |
| `community_standing` | 0 | unbounded | Osage social capital |
| `indian_sympathy` | 0 | unbounded; <-2 prejudiced, >3 advocate | Stance on Indigenous peoples |
| `newspaper_stance` | 0 | negative = conservative; positive = progressive | Wigwam editorial identity |
| `yancey_mystery` | False | bool | Has Sabra glimpsed Yancey's dark side |
| `donna_name` | "Donna" | "Donna" / "Felice" | Daughter's name, set at birth |
| `dixie_lee_editorial` | "none" | "support" / "oppose" / "neutral" | Post-trial editorial stance |
| `statehood_stance` | "none" | "single" / "double" / "consult" | Statehood editorial position |
| `congress_issue` | "none" | "indian" / "oil_law" / "education" | Congressional priority |
| `donna_wedding_advice` | "none" | "chose_well" / "cravat_stock" / "be_happy" | Wedding-day words |
| `ruby_welcomed` | False | bool | Warmth toward Ruby Big Elk |
| `ruby_time_needed` | False | bool | Honest hesitation with Ruby |

**Achievement flags (boolean, once set never unset):**
`sabra_confronted_mother`, `sabra_admires_yancey`, `sabra_helped_frontier_char`, `sabra_stood_firm_danger`, `sabra_shielded_cim`, `sabra_stood_alone`, `sabra_defended_indians`, `sabra_cleared_the_office`, `isaiah_defended`

---

## Chapter 1 — "The Land of the Fair God"
*Source novel: Books I–VII | Game scenes: scene1a through scene7 | Period: Spring 1889*

### Choice Block 1 — Scene 1a: The Mission Visit (Mother Bridget's speech)
**Label:** `scene1a_mission_visit`
**Prompt:** "How does she take this in?"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| "I want to be one of those women." (Frontier spirit) | `sabra_direction += 2` |
| "I want to do Yancey proud." (Marriage first) | *(none)* |
| "I'm frightened." (Honest) | `yancey_relationship += 2` |

---

### Choice Block 2 — Scene 1a: Mother Bridget's farewell
**Label:** `scene1a_mission_visit`
**Prompt:** "Before she goes—"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| "Will I see you again?" | `yancey_relationship -= 1` |
| "Tell me it will be all right." | *(none)* |
| "Thank you." (Take the blanket and go) | `sabra_direction += 1` |

---

### Choice Block 3 — Scene 1: The Venable Dinner (Yancey's retelling)
**Label:** `scene1_venable_home`
**Prompt:** "How does Sabra respond to Yancey's retelling?"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| Wide-eyed admiration — she leans forward | `yancey_relationship += 10`, `sabra_direction += 1` |
| Quiet skepticism — she has heard this too many times | `yancey_relationship -= 5`, `sabra_direction -= 1` |
| Polite reserve — she listens without expression | *(none)* |

---

### Choice Block 4 — Scene 2: The Land Run Flashback (giving away the claim)
**Label:** `scene2_land_run`
**Prompt:** "What does Sabra think of this?"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| She admires the gesture — he is a true romantic | `yancey_relationship += 10`, `sabra_direction += 1`, `sabra_admires_yancey = True` |
| She finds it reckless — beautiful, but reckless | `yancey_relationship -= 5`, `sabra_direction -= 1` |
| She feels a complex mix — admiration and dread together | `yancey_relationship += 5` |

---

### Choice Block 5 — Scene 3: The Decision (mother confrontation)
**Label:** `scene3_the_decision`
**Prompt:** "What does Sabra do?"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| Confront her mother — stand her ground openly | `yancey_relationship += 5`, `sabra_direction += 2`, `sabra_confronted_mother = True` |
| Stand silently behind Yancey — let him speak for her | `yancey_relationship += 10`, `sabra_direction -= 1` |
| Express private doubts while outwardly complying | `yancey_relationship -= 5`, `sabra_direction -= 2` |

---

### Choice Block 6 — Scene 4: The Journey West ("Are you frightened?")
**Label:** `scene4_journey_west`
**Prompt:** "How does Sabra answer?"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| "Not at all" — she opens up to his dream | `yancey_relationship += 10`, `sabra_direction += 2` |
| "Yes" — she stays guarded but truthful | `yancey_relationship += 5`, `sabra_direction -= 1` |
| She deflects — changes the subject to practical matters | `sabra_direction -= 2` |

---

### Choice Block 7 — Scene 5: Arriving at Osage (the grabbing stranger)
**Label:** `scene5_arriving_osage`
**Prompt:** "What does Sabra do?"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| Stand her ground — look him in the eye | `yancey_relationship += 5`, `sabra_direction += 3`, `sabra_helped_frontier_char = True` |
| Call for Yancey — let him handle it | `sabra_direction -= 2` |
| Ignore him completely — walk past | `sabra_direction += 1` |

---

### Choice Block 8 — Scene 6: The Oklahoma Wigwam (gunshot in the street)
**Label:** `scene6_oklahoma_wigwam`
**Prompt:** "What does Sabra do?"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| Go to the tent door and look | `yancey_relationship += 5`, `sabra_direction += 2`, `sabra_stood_firm_danger = True` |
| Stay at the press and keep working | `sabra_direction += 3`, `sabra_stood_firm_danger = True` |
| Go to find Yancey — she will not wait helplessly | `yancey_relationship -= 5`, `sabra_direction += 1` |

**Notes:** Typesetting minigame precedes this block. Success: `sabra_direction += 2`, `sabra_stood_firm_danger = True`. Failure: no variable changes.

---

### Chapter 1 Choice Count: **8 blocks, 24 options total**
**Variables accessible in Ch1:** `yancey_relationship`, `sabra_direction`; flags `sabra_confronted_mother`, `sabra_admires_yancey`, `sabra_helped_frontier_char`, `sabra_stood_firm_danger`

---

## Chapter 2 — "Building Osage"
*Source novel: Books VIII–XII | Game scenes: scene8 through scene13 | Period: 1890–1893*

### Choice Block 9 — Scene 8: The Lion in the Streets (gunman enters church)
**Label:** `scene8_lion_streets`
**Prompt:** "When the gunman entered, Sabra's first instinct was:"
**Number of options:** 2

| Option Text | Variables Changed |
|---|---|
| Step forward — put herself between Cim and the door | `sabra_direction += 1`, `sabra_independence += 2`, `sabra_shielded_cim = True` |
| Stay seated, hands folded, and pray | `sabra_direction -= 1` |

---

### Choice Block 10 — Scene 8: After Yancey sits back down
**Label:** `scene8_lion_streets`
**Prompt:** "After Yancey sat back down — Sabra's response:"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| Reach across the pew and take his hand, openly | `yancey_relationship += 5` |
| Say nothing. Bow her head. Let the hymn resume. | `yancey_relationship += 2`, `sabra_independence += 1` |
| Feel the sickness of it — the nearness of violence | `yancey_relationship -= 3`, `yancey_mystery = True` |

**Notes:** Church collection minigame follows. Each catch: `community_standing += 1` per caught thief (variable: `scene8_caught`).

---

### Choice Block 11 — Scene 9: Seven Notches (Pete Pitchlyn's count)
**Label:** `scene9_seven_notches`
**Prompt:** "Sabra's approach to what she had just heard:"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| Ask him directly. "Is it true? Seven men?" | `yancey_relationship -= 3`, `yancey_mystery = True` *(then sub-menu)* |
| Say nothing. She had known what she married. | `yancey_relationship += 5`, `sabra_independence += 2` |
| Make a small joke of it — ease the tension | `yancey_relationship += 3`, `sabra_direction += 1` |

**Sub-menu (only if "Ask him directly" chosen):**
**Prompt:** "Hearing that —"

| Sub-option Text | Variables Changed |
|---|---|
| "I understand. The territory has its own laws." | `yancey_relationship += 5`, `sabra_direction += 2` |
| "I need time. Give me that." | `yancey_relationship -= 2` |

---

### Choice Block 12 — Scene 10: The Wigwam Lives (citizens pressure Sabra)
**Label:** `scene10_wigwam_lives`
**Prompt:** "Sabra's response to the pressure:"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| Defend Yancey — the paper prints what it believes | `yancey_relationship += 5`, `community_standing -= 2` |
| Promise to "speak to him" — buy peace she doesn't intend to deliver | `yancey_relationship -= 3`, `community_standing += 2` |
| Give them a composed non-answer — the paper speaks for itself | `yancey_relationship += 3`, `community_standing += 1` |

---

### Choice Block 13 — Scene 10: Arita Red Feather's documents
**Label:** `scene10_wigwam_lives`
**Prompt:** "Sabra's answer to Arita:"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| Accept the documents and promise secrecy | `indian_sympathy += 3`, `sabra_independence += 2` |
| Politely decline — this is Yancey's affair | `indian_sympathy -= 2` |
| Advise Arita to come back when Yancey is in | `indian_sympathy += 1` |

---

### Choice Block 14 — Scene 11: The Wind and Donna (labor without Yancey)
**Label:** `scene11_wind_donna`
**Prompt:** "Sabra's decision in this moment:"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| "Go. But do not send for Yancey. I am enough." | `sabra_independence += 3`, `sabra_direction += 2`, `sabra_stood_alone = True` |
| "Go — and ride for Yancey as well." | `sabra_independence -= 1` |
| "He'll come when he can. That's Yancey." | `yancey_relationship += 2`, `sabra_direction += 1` |

---

### Choice Block 15 — Scene 11: Naming the baby
**Label:** `scene11_wind_donna`
**Prompt:** "What name came to Sabra?"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| Donna. For the land. | `sabra_direction += 2`, `donna_name = "Donna"` |
| Felice — for her mother. | `sabra_direction -= 2`, `donna_name = "Felice"` |
| Yancey — if she'll have it. Donna Yancey Cravat. | `yancey_relationship += 3`, `donna_name = "Donna"` |

---

### Choice Block 16 — Scene 12: Respectability (Sol Levy's warning about Dixie Lee)
**Label:** `scene12_respectability`
**Prompt:** "Sabra's response:"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| "Is it true, Sol? Do you know?" | `yancey_mystery = True` |
| "Thank you. I'll manage." | `sabra_independence += 1` |
| Say nothing — just nod | *(none)* |

---

### Choice Block 17 — Scene 12: The Women's Club vote on Dixie Lee
**Label:** `scene12_respectability`
**Prompt:** "On the question of Dixie Lee's membership:"
**Number of options:** 3 standard + 2 conditional

| Option Text | Condition | Variables Changed |
|---|---|---|
| Insist she be considered | always | `community_standing -= 2`, `sabra_independence += 2`, `sabra_direction += 2` |
| Agree to the exclusion | always | `community_standing -= 2`, `sabra_direction -= 2` |
| Abstain | always | `sabra_direction -= 1` |
| "Mrs. Sipes, the question before us is standing…" | `sabra_direction <= -5` | `community_standing += 1`, `sabra_direction -= 1` |
| "If she goes, I go." | `sabra_direction >= 5` | `community_standing -= 3`, `sabra_direction += 2`, `sabra_independence += 1` |

---

### Choice Block 18 — Scene 12: The Women's Club vote on Arita Red Feather
**Label:** `scene12_respectability`
**Prompt:** "On Arita Red Feather:"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| "Arita Red Feather is a finer woman than any of us. She stays." | `indian_sympathy += 3`, `community_standing -= 3`, `sabra_defended_indians = True` |
| Agree with the exclusion. It is different. | `indian_sympathy -= 3`, `community_standing += 2` |
| Propose an Indian women's auxiliary | `indian_sympathy -= 1`, `community_standing += 1` |

---

### Choice Block 19 — Scene 13: The Cherokee Strip (Yancey's announcement)
**Label:** `scene13_cherokee_strip`
**Prompt:** "Sabra's response to his announcement:"
**Number of options:** 4

| Option Text | Variables Changed |
|---|---|
| "Take me with you." | `yancey_relationship += 5`, `sabra_direction += 3`, `sabra_independence += 2` |
| "Go. I'll keep the Wigwam running." | `yancey_relationship += 3`, `sabra_independence += 3`, `sabra_direction += 2` |
| "Will you come back?" | `yancey_relationship -= 2`, `yancey_mystery = True` |
| "You promised you would stay." | `yancey_relationship -= 5`, `sabra_direction -= 2` |

---

### Choice Block 20 — Scene 13: Watching him go
**Label:** `scene13_cherokee_strip`
**Prompt:** "As she watched him go:"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| She felt the familiar pride alongside the fear | `yancey_relationship += 3`, `sabra_admires_yancey = True` |
| She turned back to the press. There was work. | `sabra_independence += 3`, `sabra_direction += 2` |
| She allowed herself to cry, alone, just once. | `sabra_direction -= 1`, `yancey_relationship -= 1` |

---

### Chapter 2 Choice Count: **12 blocks (plus 1 sub-menu), ~34 options total**
**New variables introduced:** `community_standing`, `indian_sympathy`, `sabra_independence`, `yancey_mystery`; flags `sabra_shielded_cim`, `sabra_stood_alone`, `sabra_defended_indians`, `donna_name`

---

## Chapter 3 — "Yancey Leaves; Sabra Rises"
*Source novel: Books XIII–XV | Game scenes: scene14 through scene18 | Period: 1893–1898*

### Choice Block 21 — Scene 14: Five Years (how Sabra held on)
**Label:** `scene14_five_years`
**Prompt:** "In the five years without him, Sabra found her footing:"
**Number of options:** 4

| Option Text | Variables Changed |
|---|---|
| Through the work — the Wigwam became her anchor | `sabra_independence += 3`, `sabra_direction += 2`, `newspaper_stance += 1` |
| Through the children — for Cim and Donna she kept going | `sabra_independence += 2`, `sabra_direction -= 1` |
| Through the community — Osage needed her, and she let it | `sabra_independence += 2`, `community_standing += 3` |
| With difficulty — there were nights she nearly quit | `yancey_relationship -= 3`, `yancey_mystery = True` |

---

### Choice Block 22 — Scene 15: The Kid (Yancey walks through the door)
**Label:** `scene15_the_kid`
**Prompt:** "When Yancey walked through the door:"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| She went to him immediately | `yancey_relationship += 5` |
| She stayed at the press. Let him come to her. | `sabra_independence += 3`, `sabra_direction += 2`, `sabra_cleared_the_office = True` |
| She felt rage, then relief, then nothing she could name | `yancey_relationship -= 2`, `yancey_mystery = True` |

---

### Choice Block 23 — Scene 15: The reward money
**Label:** `scene15_the_kid`
**Prompt:** "What Sabra said about the reward money:"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| "Put it in the paper's account. We have debts." | `sabra_independence += 2`, `newspaper_stance += 1` |
| "Give some to the Kid's family, if he had one." | `yancey_relationship += 3`, `indian_sympathy += 1` |
| Say nothing. The money was his affair. | `sabra_independence += 1` |

---

### Choice Block 24 — Scene 16: Running the Paper (the editorial)
**Label:** `scene16_running_paper`
**Prompt:** "The week's editorial concerned the territorial legislature's vote on Indian allotment:"
**Number of options:** 3 standard + 2 conditional

| Option Text | Condition | Variables Changed |
|---|---|---|
| Write it sharp — defend the Indian Nations openly | always | `newspaper_stance += 3`, `indian_sympathy += 2`, `community_standing -= 1` *(then sub-menu)* |
| Write measured — make the argument without naming names | always | `newspaper_stance += 1`, `indian_sympathy += 1` |
| Write a general civic piece — keep the Wigwam neutral | always | `newspaper_stance -= 1`, `community_standing += 2` |
| Write it sharp — frame in the language of law and property | `sabra_direction <= -5` | `newspaper_stance += 2`, `indian_sympathy += 1`, `community_standing += 1`, `sabra_direction -= 1` |
| Write it sharp, sign it, invite any dissenter to respond | `sabra_direction >= 5` | `newspaper_stance += 3`, `community_standing -= 2`, `sabra_independence += 1`, `sabra_direction += 1` |

**Sub-menu (only if "Write it sharp — defend openly" chosen):**
**Prompt:** "The reaction from the Osage business community:"

| Sub-option Text | Variables Changed |
|---|---|
| Let them cancel their ads. The story is the story. | `newspaper_stance += 2`, `community_standing -= 2` |
| Soften the names — keep the argument, spare the men | `newspaper_stance += 1`, `community_standing += 1` |

---

### Choice Block 25 — Scene 16: Letters policy
**Label:** `scene16_running_paper`
**Prompt:** "Sabra's policy for letters on Indian affairs:"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| Print the argument from both sides, let readers decide | `newspaper_stance += 1`, `community_standing += 1` |
| Favor letters that agree with the paper's editorial line | `newspaper_stance += 2` |
| Print whatever arrived. Make no selection. | `newspaper_stance -= 1` |

**Notes:** Letters minigame follows. Outcome applies: `newspaper_stance += pro_indian_count * 2`, `newspaper_stance -= anti_indian_count * 2`, `indian_sympathy += pro_indian_count`, `indian_sympathy -= anti_indian_count`, `community_standing -= gossip_count * 2`, `yancey_relationship += yancey_count`. Additional penalties: `community_standing -= 1` if any gossip letter printed; `newspaper_stance -= 1` if any oil letter printed.

---

### Choice Block 26 — Scene 17: Isaiah (discovering his literacy)
**Label:** `scene17_isaiah`
**Prompt:** "Sabra's response to discovering Isaiah's literacy:"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| "You should be writing, not just setting type." | `sabra_independence += 2`, `community_standing += 1` |
| Let the moment pass — do not make it more than it is | `sabra_direction -= 1` |
| "I should have asked you to help with the writing long ago." | `sabra_independence += 1`, `isaiah_defended = True` |

---

### Choice Block 27 — Scene 17: The advertiser confrontation (Horace Tubbs)
**Label:** `scene17_isaiah`
**Prompt:** "Sabra's response:"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| "Isaiah stays. You may take your notices elsewhere." | `isaiah_defended = True`, `community_standing -= 2`, `newspaper_stance += 1` |
| Offer a compromise — different hours, different street entrance | `community_standing += 1` |
| Buy time — tell Tubbs she'll "look into it" | *(none)* |

---

### Choice Block 28 — Scene 18: The War (Yancey enlisting)
**Label:** `scene18_war`
**Prompt:** "Sabra's answer:"
**Number of options:** 4

| Option Text | Variables Changed |
|---|---|
| "Go. But know that I will not wait another five years." | `yancey_relationship -= 3`, `sabra_independence += 3`, `sabra_direction += 3` |
| "I have the paper. Go." | `sabra_independence += 2`, `sabra_direction += 2`, `yancey_relationship += 2` |
| "Don't go. For once. Stay." | `yancey_relationship -= 5`, `sabra_direction -= 2` |
| Say nothing. Go to the window. | `sabra_independence += 2`, `yancey_mystery = True` |

---

### Choice Block 29 — Scene 18: Dixie Lee at the door (the night before departure)
**Label:** `scene18_war`
**Prompt:** "Sabra's response to Dixie Lee:"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| "Come in. We'll have coffee before he goes." | `sabra_direction += 2`, `community_standing += 1` |
| A civil nod. No more. | `sabra_direction -= 1` |
| "Thank you. That means something." | `sabra_direction += 1`, `community_standing += 1` |

---

### Chapter 3 Choice Count: **9 blocks (plus 1 sub-menu), ~29 options total**
**New variables introduced:** `newspaper_stance`, `sabra_cleared_the_office`, `isaiah_defended`

---

## Chapter 4 — "War Hero, Statehood, Oil"
*Source novel: Books XVI–XX | Game scenes: scene19 through scene23 | Period: 1898–1907*

### Choice Block 30 — Scene 19: The Rough Rider Returns (public moment in the square)
**Label:** `scene19_rough_rider`
**Prompt:** "The crowd was cheering. Yancey had not yet spoken. What did Sabra do:"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| Stand beside him. Smile. This is his moment. | `yancey_relationship += 5` |
| Step back. Let him have it alone. | `sabra_independence += 1` |
| Wave to the crowd herself — a gesture of partnership | `community_standing += 2` |

---

### Choice Block 31 — Scene 19: Private reunion (first evening alone)
**Label:** `scene19_rough_rider`
**Prompt:** "The first evening alone:"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| "Tell me everything. From the beginning." | `yancey_relationship += 10` |
| "I need to tell you what happened here while you were gone." | `sabra_independence += 2` |
| "I'm glad you're home." | `yancey_relationship += 5` |

---

### Choice Block 32 — Scene 20: Dixie Lee's Trial (private reaction the night before)
**Label:** `scene20_dixie_trial`
**Prompt:** "Sabra's answer, the night before the trial:"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| "I think you're wrong. She is not a victim. She made choices." | `yancey_relationship -= 5`, `newspaper_stance -= 1` |
| "I think you're right. I hate that you're right, but I think you are." | `yancey_relationship += 5`, `indian_sympathy += 1` |
| "Tell me the legal argument. I need to understand it." | `newspaper_stance += 1`, `sabra_independence += 1` |

**Notes:** Trial arguments minigame follows. Variable changes applied in `scene20_trial_result` label: argument #2 selected: `yancey_relationship += 5`; argument #3 selected: `newspaper_stance += 1`; argument #5 selected: `yancey_relationship += 3`, `community_standing -= 1`; argument #6 selected: `newspaper_stance += 1`; arguments #1 and #4 both selected: `newspaper_stance -= 1`, `yancey_relationship -= 3`. Ordering bonuses: closing = #2: `yancey_relationship += 3`; opening = #5: `community_standing -= 1`; opening = #6: `newspaper_stance += 1`.

---

### Choice Block 33 — Scene 20: Post-verdict editorial
**Label:** `scene20_post_verdict`
**Prompt:** "What Osage needed to read:"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| "The verdict was just. The law protected a woman others wanted to punish." | `newspaper_stance += 2`, `community_standing -= 1`, `dixie_lee_editorial = "support"` |
| "This court has failed Osage's women and children." | `newspaper_stance -= 2`, `community_standing += 2`, `dixie_lee_editorial = "oppose"` |
| "Report the facts only. The community will decide." | `sabra_independence += 1`, `dixie_lee_editorial = "neutral"` |

---

### Choice Block 34 — Scene 20: Dixie Lee in the courthouse hallway
**Label:** `scene20_post_verdict`
**Prompt:** "Sabra's response:"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| "I hope you find peace in whatever you do next." | `community_standing += 1` |
| "Your man won. That's all this is." | *(none)* |
| Say nothing. Walk past. | `community_standing -= 1` |

---

### Choice Block 35 — Scene 21: The Statehood Question (editorial stance)
**Label:** `scene21_statehood`
**Prompt:** "The Wigwam's editorial position on statehood:"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| "Oklahoma Territory and Indian Territory must be one state." | `newspaper_stance += 2`, `indian_sympathy += 2`, `statehood_stance = "single"` |
| "Two states is the safer, more stable choice for both peoples." | `newspaper_stance -= 2`, `indian_sympathy -= 1`, `statehood_stance = "double"` |
| "The Wigwam cannot advocate without consultation with the affected communities." | `sabra_independence += 2`, `statehood_stance = "consult"` |

---

### Choice Block 36 — Scene 21: Yancey's letter on statehood
**Label:** `scene21_statehood`
**Prompt:** "Regarding Yancey's letter:"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| "He's right. I'll say so." | `yancey_relationship += 5`, `indian_sympathy += 1` |
| "He's not wrong, but he's not here. I'll decide this myself." | `sabra_independence += 2`, `yancey_relationship -= 5` |
| "I'll print his letter. Let the readers see his argument." | `newspaper_stance += 1` |

---

### Choice Block 37 — Scene 22: The First Oil (Wigwam's approach to oil coverage)
**Label:** `scene22_first_oil`
**Prompt:** "The Wigwam's approach to covering oil:"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| "This is progress. Cover it fully — the good and the risk." | `newspaper_stance += 1`, `community_standing += 1` |
| "Oil brings the wrong kind of people. Be careful what you celebrate." | `newspaper_stance -= 1` |
| "This is the story of the decade. The Wigwam will own it." | `sabra_independence += 1`, `community_standing += 2` |

---

### Choice Block 38 — Scene 22: Cim and Oil (counsel to her son)
**Label:** `scene22_first_oil`
**Prompt:** "Sabra's counsel to her son:"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| "Finish your degree first." | *(none)* |
| "If this is what you want, learn all of it before you commit." | *(none)* |
| "Your father would tell you to stay out of it. I don't know if he's right." | `yancey_relationship += 5` |

---

### Choice Block 39 — Scene 23: What Yancey Left (the letter)
**Label:** `scene23_what_yancey_left`
**Prompt:** "What Sabra did with the letter:"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| "Write back. Tell him about Donna and Cim." | `yancey_relationship += 5` |
| "File it with the others. Don't write back." | `sabra_independence += 2`, `yancey_relationship -= 5` |
| "Read it to the children. Let them decide how they feel." | *(none)* |

---

### Choice Block 40 — Scene 23: Taking stock (how Sabra regards what she has built)
**Label:** `scene23_what_yancey_left`
**Prompt:** "How Sabra regarded what she had built:"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| "I chose this. I'd choose it again." | `sabra_independence += 1`, `community_standing += 1` |
| "It is what it is. Don't romanticize it." | *(none)* |
| "I'm still waiting. I don't think I'll stop." | `yancey_relationship += 5`, `sabra_independence -= 1` |

---

### Chapter 4 Choice Count: **11 blocks, ~33 options total**
**New variables introduced:** `dixie_lee_editorial`, `statehood_stance`

---

## Chapter 5 — "Legacy and Monument"
*Source novel: Books XXI–XXV | Game scenes: scene24 through scene28 + endings | Period: 1910–1931*

### Choice Block 41 — Scene 24: Cim Brings Ruby Home (Sabra's first response)
**Label:** `scene24_cim_ruby`
**Prompt:** "The room is very quiet. What does she say to this young woman?"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| "Welcome to our family." (And mean it) | `indian_sympathy += 3`, `yancey_relationship += 5`, `ruby_welcomed = True` |
| "I need time." (Honest, not cruel) | `ruby_time_needed = True` |
| "My son chose this. I will be civil." (Duty without warmth) | `indian_sympathy -= 1`, `yancey_relationship -= 5` |

---

### Choice Block 42 — Scene 24: Big Elk's formal words
**Label:** `scene24_cim_ruby`
**Prompt:** "How does she respond?"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| "Tell him — I hope to know him better." | `indian_sympathy += 1` |
| "The formalities are appreciated." (Polite, distant) | *(none)* |
| "Tell him he's welcome here whenever he comes to Osage." | `community_standing += 1`, `indian_sympathy += 1` |

**Notes:** If `ruby_time_needed = True`, a scripted follow-up scene with Ruby fires automatically: `indian_sympathy += 1`.

---

### Choice Block 43 — Scene 25: The Congresswoman (whether to run)
**Label:** `scene25_congresswoman`
**Prompt:** "She is fifty-two years old. She has been running something without the title for twenty years."
**Number of options:** 3 standard + 2 conditional

| Option Text | Condition | Variables Changed |
|---|---|---|
| "Yes. I'll run." | always | `community_standing += 3`, `sabra_independence += 2` |
| "Yes. For one term." | always | `community_standing += 2`, `sabra_independence += 1` |
| "Someone else should have this. Someone younger." | always | `community_standing -= 1` |
| "Yes. And I already know which three senators I need to court." | `sabra_direction <= -5` | `community_standing += 3`, `sabra_independence += 2`, `sabra_direction -= 1` |
| "Yes. And I intend to be inconvenient." | `sabra_direction >= 5` | `community_standing += 2`, `newspaper_stance += 1`, `sabra_independence += 2`, `sabra_direction += 1` |

---

### Choice Block 44 — Scene 25: Congressional issue priority
**Label:** `scene25_congresswoman`
**Prompt:** "Her colleagues on the floor are watching. What does she bring to the floor?"
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| "Indian reservation reform. The system is unjust and I'll say so." | `indian_sympathy += 3`, `newspaper_stance += 1`, `congress_issue = "indian"` |
| "Oklahoma needs oil law reform. The fields are lawless." | `newspaper_stance += 1`, `community_standing += 1`, `congress_issue = "oil_law"` |
| "Education. Especially for Indian children leaving the reservation schools." | `indian_sympathy += 2`, `community_standing += 2`, `congress_issue = "education"` |

---

### Choice Block 45 — Scene 26: Donna's Wedding (what Sabra tells Donna)
**Label:** `scene26_donnas_wedding`
**Prompt:** "Five minutes in the back room. She has one thing she wants to say."
**Number of options:** 3

| Option Text | Variables Changed |
|---|---|
| "You've chosen well. You always choose well." | `community_standing += 1`, `donna_wedding_advice = "chose_well"` |
| "Whatever comes — you'll manage it. You're Cravat stock." | `sabra_independence += 1`, `donna_wedding_advice = "cravat_stock"` |
| "I hope he makes you happy." (Quietly) | `yancey_relationship += 5`, `donna_wedding_advice = "be_happy"` |

---

### Choice Block 46 — Scene 27: The Word from Bowlegs (last words to Yancey)
**Label:** `scene27_bowlegs`
**Prompt:** "He is dying. The crowd has gone silent. She is holding his head."
**Number of options:** 2 standard + 1 conditional

| Option Text | Condition | Variables Changed |
|---|---|---|
| "You came back." (If she can mean it) | `yancey_relationship >= 50` | `yancey_relationship += 5` |
| "Sleep. You're safe." | always | `yancey_relationship += 3` |
| "I'm here. I'm here." | always | *(none)* |

---

### Choice Block 47 — Scene 28: The Monument (photographs for Krbecek)
**Label:** `scene28_monument`
**Prompt:** Photograph minigame — player selects 2 of 6 photographs.
**Number of options:** 15 possible pairs (6 choose 2)

| Pair Selected | Variables Changed |
|---|---|
| Photos 1 (Run) + 4 (Rough Rider) | `yancey_relationship += 3` |
| Photos 2 (tent church) + 3 (Sabra at press) | `community_standing += 2` |
| Photos 5 (Kid's burial) + 6 (Cim/Ruby) | `indian_sympathy += 2` |
| Any other pair | `yancey_relationship += 1` |

---

### Chapter 5 Choice Count: **7 blocks (plus minigame), ~22 options total**
**New variables introduced:** `ruby_welcomed`, `ruby_time_needed`, `congress_issue`, `donna_wedding_advice`

---

## Ending Branch Routing

**Label:** `chapter5_summary`
Endings are assigned automatically based on cumulative variable totals. No player choice fires directly; the branching is a consequence of all prior decisions.

| Ending | Label | Condition |
|---|---|---|
| "The Land Belongs to All" | `ending_land_belongs` | `indian_sympathy >= 7` AND (`sabra_independence >= 5` OR `yancey_relationship >= 50`) |
| "She Built It Herself" | `ending_built_herself` | `sabra_independence >= 8` AND `community_standing >= 8` |
| "She Chose the Shadow" | `ending_his_shadow_chosen` | `sabra_independence <= 4` AND `yancey_relationship >= 65` |
| "She Was His Shadow" (default) | `ending_his_shadow` | all other cases |

Each ending also displays `congress_issue`-conditional text, `donna_wedding_advice`-conditional text, `dixie_lee_editorial`-conditional text, and `ruby_welcomed` / `sabra_confronted_mother` flag callbacks.

---

## Aggregate Statistics

| Chapter | Choice Blocks | Options (approx.) | Key Variables Introduced |
|---|---|---|---|
| Chapter 1 (Books I–VII) | 8 | 24 | `yancey_relationship`, `sabra_direction`; 4 flags |
| Chapter 2 (Books VIII–XII) | 12 (+1 sub) | 34 | `community_standing`, `indian_sympathy`, `sabra_independence`, `yancey_mystery`, `donna_name`; 3 flags |
| Chapter 3 (Books XIII–XV) | 9 (+1 sub) | 29 | `newspaper_stance`; 2 flags |
| Chapter 4 (Books XVI–XX) | 11 | 33 | `dixie_lee_editorial`, `statehood_stance` |
| Chapter 5 (Books XXI–XXV) | 7 + minigame | 22 | `ruby_welcomed`, `ruby_time_needed`, `congress_issue`, `donna_wedding_advice` |
| **Total** | **47 blocks** | **~142 options** | **13 numeric variables, 13 boolean flags** |

---

## Minigames Summary

| Minigame | Scene | Outcome Variables |
|---|---|---|
| Typesetting (OSAGE) | scene6 (Ch1) | Success: `sabra_direction += 2`, `sabra_stood_firm_danger = True`. Failure: no change. |
| Church Collection | scene8 (Ch2) | `community_standing += scene8_caught` (0–3+) |
| Letters Selection | scene16 (Ch3) | `newspaper_stance`, `indian_sympathy`, `community_standing`, `yancey_relationship` — weighted by letter tags |
| Trial Arguments | scene20 (Ch4) | `yancey_relationship`, `newspaper_stance`, `community_standing` — based on selection IDs and ordering |
| Photograph Box | scene28 (Ch5) | `yancey_relationship`, `community_standing`, or `indian_sympathy` based on photo pair |

---

## Conditional Choices (Gate-Locked Options)

The following options are only offered when a specific variable threshold has been reached. These represent the game's "late-arc" design — players who have committed strongly in one direction unlock corresponding dialogue.

| Scene | Gate Condition | Unlocked Option |
|---|---|---|
| scene12 (Ch2) | `sabra_direction <= -5` | "Mrs. Sipes, the question before us is standing…" |
| scene12 (Ch2) | `sabra_direction >= 5` | "If she goes, I go." |
| scene16 (Ch3) | `sabra_direction <= -5` | "Write it sharp — frame in the language of law and property" |
| scene16 (Ch3) | `sabra_direction >= 5` | "Write it sharp, sign it, and formally invite any dissenter to respond" |
| scene25 (Ch5) | `sabra_direction <= -5` | "Yes. And I already know which three senators I need to court." |
| scene25 (Ch5) | `sabra_direction >= 5` | "Yes. And I intend to be inconvenient." |
| scene27 (Ch5) | `yancey_relationship >= 50` | "You came back." (If she can mean it) |

**Total gate-locked options:** 7 (all gated on `sabra_direction` extremes or `yancey_relationship` threshold)

---

## Variable Impact Analysis

### Highest-impact single choices (variable delta)

| Choice | Max Single Delta |
|---|---|
| Venable dinner (wide-eyed admiration) | `yancey_relationship +10` |
| Land Run flashback (admires gesture) | `yancey_relationship +10` |
| Mother confrontation (stand behind Yancey) | `yancey_relationship +10` |
| Journey west (opens to his dream) | `yancey_relationship +10` |
| Rough Rider reunion (tell me everything) | `yancey_relationship +10` |
| Cherokee Strip: take me with you | `sabra_direction +3`, `sabra_independence +2`, `yancey_relationship +5` |
| War departure: won't wait five more years | `sabra_independence +3`, `sabra_direction +3` |

### Ending threshold analysis (from variable defaults)

- `ending_land_belongs` requires `indian_sympathy >= 7`: player must pick the pro-indigenous option in most of the 8–10 relevant choice blocks.
- `ending_built_herself` requires both `sabra_independence >= 8` AND `community_standing >= 8`: rare combination — demands sustained independence choices without sacrificing civic engagement.
- `ending_his_shadow_chosen` requires `sabra_independence <= 4` AND `yancey_relationship >= 65`: demands consistent pro-Yancey choices while avoiding the independence-raising options; achievable on a "devoted wife" playthrough.
- `ending_his_shadow` (default): all other cases, including mixed playthroughs.

---

## Design Notes and Potential Issues

1. **`sabra_direction` unused after Chapter 3 (except as gate):** The variable gains and loses throughout Chapters 1–3 but its only functional role in Chapters 4–5 is gating two dialogue pairs in scene16, scene25, and the epilogue tone text. Players who plateau at moderate values never see the gate-locked options and cannot access them regardless of late-game choices.

2. **`community_standing` asymmetry:** Defending Indian rights consistently lowers `community_standing` (Arita exclusion fight: -3; Dixie Lee insistence: -2 to -3; sharp editorial: -1 to -2). The only reliable gains come from civic pragmatism. This creates a structural tension where progressive play penalizes the `ending_built_herself` requirement (`community_standing >= 8`).

3. **`yancey_relationship` ceiling risk:** Multiple Ch1 choices offer `+10`. A player who takes all three highest-value Ch1 options arrives at Ch2 with `yancey_relationship` near 80. This makes `ending_his_shadow_chosen` (`>= 65`) effectively guaranteed unless Ch3–Ch4 choices substantially reverse the trend. Consider whether the `<= 4` independence gate provides sufficient friction.

4. **`donna_name` ("Felice" track) has no downstream consequence:** Setting `donna_name = "Felice"` changes every subsequent string interpolation of the daughter's name but no variable gate, ending branch, or achievement flag checks for `donna_name == "Felice"`. The choice is narratively meaningful but mechanically inert beyond display.

5. **Scene 18 (Dixie Lee at the door) is disconnected from `dixie_lee_editorial`:** The emotional arc of the Sabra/Dixie Lee relationship is split between Ch3 scene18 (the coffee/nod choice, affecting `sabra_direction` and `community_standing`) and Ch4 scene20 (the editorial choice, setting `dixie_lee_editorial`). These are resolved in separate variables and never interact — the scene18 choice does not influence scene20 options or the Ch4/Ch5 Dixie Lee callbacks.

6. **Letters minigame (scene16) outcome text references letter #8 by ID:** The `if 8 in letters_printed:` conditional in `scene16_letters_result` hard-codes an ID reference. Any future reordering of the letters pool will silently break this narrative beat.

7. **Photograph pairs:** Only three pairs of the fifteen possible trigger distinct narrative outcomes. The remaining twelve fall through to the generic `yancey_relationship += 1` branch. This may feel anticlimactic for players who attempt non-obvious combinations.

---

*Audit compiled from full read of: `script_chapter1.rpy`, `script_chapter2.rpy`, `script_chapter3.rpy`, `script_chapter4.rpy`, `script_chapter5.rpy`, `variables.rpy`.*

---

## Verdict Classification

Each choice option receives one of:

| Verdict | Meaning |
|---|---|
| `OK` | Writes state that is meaningfully read downstream in-scene or at endings |
| `EMPTY` | Writes nothing; mechanically identical to silence |
| `THIN` | Writes only to a meter/flag that is never read in-scene (only summaries/endings) |
| `ORPHAN` | Writes to a flag that is set but never read after this chapter |
| `GATE_LOOSE` | Gate threshold is trivially satisfied by most playthroughs |

### Chapter 1 Verdicts

| Block | Option | Verdict |
|---|---|---|
| scene1a M1 | "I want to be one of those women." | OK (`sabra_direction` gates Ch2/3/5 options) |
| scene1a M1 | "I want to do Yancey proud." | OK (`sabra_direction` gates Ch2/3/5 options) |
| scene1a M1 | "I'm frightened." | THIN (`yancey_relationship` read only in summaries/ending) |
| scene1a M2 | "Will I see you again?" | THIN |
| scene1a M2 | "Tell me it will be all right." | THIN |
| scene1a M2 | "Thank you." (take blanket) | OK |
| scene1 M3 | Wide-eyed admiration | OK (`yancey_relationship`, `sabra_admires_yancey`) |
| scene1 M3 | Quiet skepticism | OK |
| scene1 M3 | Polite reserve | OK (`sabra_direction` gates Ch2/3/5 options) |
| scene2 | She admires the gesture | OK |
| scene2 | She finds it reckless | OK |
| scene2 | Complex mix | THIN |
| scene3 | Confront her mother | OK (`sabra_confronted_mother` read in Ch5 summary) |
| scene3 | Stand silently behind Yancey | OK |
| scene3 | Express private doubts | OK |
| scene4 | "Not at all" | OK |
| scene4 | "Yes" — guarded | OK |
| scene4 | Deflect | OK |
| scene5 | Stand her ground | OK (`sabra_helped_frontier_char` → Ch2 callback) |
| scene5 | Call for Yancey | OK |
| scene5 | Ignore him | OK |
| scene6 | Go to door | OK (`sabra_stood_firm_danger` → Ch2 callback) |
| scene6 | Stay at press | OK |
| scene6 | Go find Yancey | OK |

### Chapter 2 Verdicts

| Block | Option | Verdict |
|---|---|---|
| scene8 M1 | Step forward (shield Cim) | OK (`sabra_shielded_cim` → Ch5 callback) |
| scene8 M1 | Stay seated | OK |
| scene8 M2 | Take his hand openly | THIN |
| scene8 M2 | Say nothing, bow head | THIN |
| scene8 M2 | Feel the sickness | THIN (`yancey_mystery` only in Ch5 scene27 + summaries) |
| scene9 | Ask directly | THIN |
| scene9 | Say nothing | THIN |
| scene9 | Small joke | OK (`sabra_direction`) |
| scene9 sub | "I understand" | OK |
| scene9 sub | "I need time" | THIN |
| scene10 M4 | Defend Yancey | THIN |
| scene10 M4 | Promise to speak to him | THIN |
| scene10 M4 | Composed non-answer | THIN |
| scene10 M5 | Accept documents | THIN (`indian_sympathy` never gates in-scene) |
| scene10 M5 | Politely decline | THIN |
| scene10 M5 | Come back for Yancey | THIN |
| scene11 birth | "I am enough." | OK (`sabra_stood_alone` flagged; `sabra_independence` grows) |
| scene11 birth | Ride for Yancey | OK |
| scene11 birth | "He'll come when he can." | OK |
| scene11 naming | Donna | OK |
| scene11 naming | Felice | **ORPHAN** (`donna_name = "Felice"` never gates dialogue) |
| scene11 naming | Donna Yancey Cravat | OK |
| scene12 Sol | "Is it true, Sol?" | OK |
| scene12 Sol | "Thank you, I'll manage." | OK |
| scene12 Sol | Say nothing — just nod | THIN (`yancey_mystery` only in Ch5 scene27 + summaries) |
| scene12 Dixie | Insist she be considered | THIN |
| scene12 Dixie | Agree to exclusion | THIN |
| scene12 Dixie | Abstain | THIN |
| scene12 Arita | "She stays." | OK (`sabra_defended_indians`) |
| scene12 Arita | Agree with exclusion | THIN |
| scene12 Arita | Propose auxiliary | THIN |
| scene13 | "Take me with you." | OK |
| scene13 | "Go. I'll keep the Wigwam." | OK |
| scene13 | "Will you come back?" | THIN |
| scene13 | "You promised." | OK |
| scene13 watching | Pride alongside fear | THIN (`sabra_admires_yancey` only summaries) |
| scene13 watching | Turn back to press | OK |
| scene13 watching | Allow herself to cry | OK |

### Chapter 3 Verdicts

| Block | Option | Verdict |
|---|---|---|
| scene14 | Through the work | OK |
| scene14 | Through the children | OK |
| scene14 | Through the community | OK |
| scene14 | With difficulty | THIN |
| scene15 | Went to him immediately | THIN |
| scene15 | Stayed at the press | OK (`sabra_cleared_the_office` → Ch4 callback) |
| scene15 | Rage, then relief | THIN |
| scene15 reward | Paper's account | OK |
| scene15 reward | Kid's family | THIN |
| scene15 reward | Say nothing | OK |
| scene16 editorial | Sharp — defend openly | OK |
| scene16 editorial | Measured — no names | OK |
| scene16 editorial | General civic | OK |
| scene17 Isaiah | "You should be writing" | OK |
| scene17 Isaiah | Let the moment pass | OK |
| scene17 Isaiah | "I should have asked you long ago" | OK |
| scene17 Tubbs | "Isaiah stays." | OK (`isaiah_defended` → Ch4 callback) |
| scene17 Tubbs | Compromise — back entrance | THIN |
| scene17 Tubbs | Buy time — "look into it" | THIN |
| scene18 war | "Go. But I will not wait." | OK |
| scene18 war | "I have the paper. Go." | OK |
| scene18 war | "Don't go. For once." | OK |
| scene18 war | Say nothing. Go to window. | THIN |
| scene18 Dixie | "Come in. Coffee." | OK |
| scene18 Dixie | A civil nod | OK |
| scene18 Dixie | "Thank you. That means something." | OK |

### Chapter 4 Verdicts

| Block | Option | Verdict |
|---|---|---|
| scene19 parade | Stand beside him. Smile. | THIN |
| scene19 parade | Step back | OK |
| scene19 parade | Wave herself | THIN |
| scene19 alone | "Tell me everything." | THIN |
| scene19 alone | "I need to tell you." | OK |
| scene19 alone | "I'm glad you're home." | THIN |
| scene20 trial | "I think you're wrong." | OK |
| scene20 trial | "I think you're right." | OK |
| scene20 trial | "Tell me the legal argument." | OK |
| scene20 editorial | Verdict was just | OK (`dixie_lee_editorial` → Ch5 reads) |
| scene20 editorial | Court has failed | OK |
| scene20 editorial | Report facts only | OK |
| scene20 hallway | "I hope you find peace…" | THIN |
| scene20 hallway | "Your man won." | OK (`sabra_direction` gates scene25) |
| scene20 hallway | Say nothing. Walk past. | THIN |
| scene21 statehood | Single state | OK (`statehood_stance` → Ch5 reads) |
| scene21 statehood | Two states | OK |
| scene21 statehood | Consult before writing | OK |
| scene21 Yancey's letter | "He's right. I'll say so." | OK |
| scene21 Yancey's letter | "He's not wrong, but not here." | OK |
| scene21 Yancey's letter | "I'll print his letter." | OK |
| scene22 oil | Cover fully | THIN |
| scene22 oil | Oil brings wrong people | THIN |
| scene22 oil | Story of the decade | OK |
| scene22 Cim | "Finish your degree first." | OK (`sabra_direction` gates scene25) |
| scene22 Cim | "Learn all of it before you commit." | THIN |
| scene22 Cim | "Your father would tell you to stay out…" | THIN |
| scene23 letter | Write back | THIN |
| scene23 letter | File it. Don't write back. | OK |
| scene23 letter | Read it to the children | THIN |
| scene23 stock | "I chose this." | THIN |
| scene23 stock | "It is what it is." | THIN |
| scene23 stock | "I'm still waiting." | OK |

### Chapter 5 Verdicts

| Block | Option | Verdict |
|---|---|---|
| scene24 Ruby | "Welcome to our family." | OK (`ruby_welcomed` → ending) |
| scene24 Ruby | "I need time." | OK (`ruby_time_needed`) |
| scene24 Ruby | "My son chose this. I will be civil." | THIN |
| scene24 Big Elk | "I hope to know him better." | THIN |
| scene24 Big Elk | "The formalities are appreciated." | OK (`sabra_direction` gates scene25) |
| scene24 Big Elk | "He's welcome here." | THIN |
| scene25 run | "Yes. I'll run." | OK |
| scene25 run | "Yes. For one term." | OK |
| scene25 run | "Someone else should have this." | THIN |
| scene25 priority | Indian reservation reform | OK (`congress_issue` → endings) |
| scene25 priority | Oklahoma oil law reform | OK |
| scene25 priority | Education for Indian children | OK |
| scene26 Donna | "You've chosen well." | OK (`donna_wedding_advice` → ending) |
| scene26 Donna | "You're Cravat stock." | OK |
| scene26 Donna | "I hope he makes you happy." | OK |
| scene27 Yancey | "You came back." (gate ≥ 50) | **GATE_LOOSE** (default is 50) |
| scene27 Yancey | "Sleep. You're safe." | THIN |
| scene27 Yancey | "I'm here. I'm here." | THIN |

---

## Proposed Corrections

### 1. EMPTY options — bind to a tone-appropriate write ✅ COMPLETE

#### Ch1 scene1a, "I want to do Yancey proud."
Tone: marriage-first, conventional. Moves toward Refined Lady without being skeptical of Yancey.
```renpy
# BEFORE:
"I want to do Yancey proud.":
    pass

# AFTER:
"I want to do Yancey proud.":
    $ sabra_direction -= 1
```
*(No new dialogue needed; the variable mutation is sufficient.)*

#### Ch1 scene1a, "Tell me it will be all right."
Tone: seeking reassurance, orienting toward relationship. Small yancey_relationship bump.
```renpy
# BEFORE:
"Tell me it will be all right.":
    pass

# AFTER:
"Tell me it will be all right.":
    $ yancey_relationship += 1
```

#### Ch1 scene1, "Polite reserve"
Tone: guarded, emotionally closed — moves Refined Lady track slightly.
```renpy
# BEFORE:
"Polite reserve — she listens without expression.":
    pass

# AFTER:
"Polite reserve — she listens without expression.":
    $ sabra_direction -= 1
```

#### Ch2 scene12 Sol, "Say nothing — just nod."
Tone: the silence is a kind of acknowledgment of Yancey's inscrutability.
```renpy
# BEFORE:
"Say nothing — just nod.":
    pass

# AFTER:
"Say nothing — just nod.":
    $ yancey_mystery = True
```
*(Matches the "Is it true, Sol?" option's effect. Two paths to the same flag; both are earned.)*

#### Ch3 scene17 Tubbs, "Buy time — 'look into it'"
Tone: stalling under pressure reads as a small social concession.
```renpy
# BEFORE:
"Buy time — 'look into it'":
    pass

# AFTER:
"Buy time — 'look into it'":
    $ community_standing -= 1
```
*(Advertisers will sense the hedge but take it as implicit retreat.)*

#### Ch4 scene20 Dixie hallway, "Your man won."
Tone: a small, hard, proud remark — Sabra shutting Dixie out, not engaging. Brief flicker of spite, not grace.
```renpy
# BEFORE:
"Your man won.":
    pass

# AFTER:
"Your man won.":
    $ yancey_relationship -= 1
    $ sabra_direction -= 1
```
*(A barbed comment, not a neutral one — it reveals something defensive in Sabra.)*

#### Ch4 scene22 Cim, "Finish your degree first."
Tone: conventional parental caution, slightly at odds with the Frontier Woman track.
```renpy
# BEFORE:
"Finish your degree first.":
    pass

# AFTER:
"Finish your degree first.":
    $ sabra_direction -= 1
```

#### Ch4 scene22 Cim, "Learn all of it before you commit."
Tone: measured, editorial-minded — the responsible journalist's advice.
```renpy
# BEFORE:
"Learn all of it before you commit.":
    pass

# AFTER:
"Learn all of it before you commit.":
    $ newspaper_stance -= 1
```
*(Caution about oil coverage = conservative editorial instinct.)*

#### Ch4 scene23, "Read it to the children."
Tone: keeps Yancey present in the household; a gesture of warmth toward the marriage.
```renpy
# BEFORE:
"Read it to the children.":
    pass

# AFTER:
"Read it to the children.":
    $ yancey_relationship += 3
```

#### Ch4 scene23, "It is what it is."
Tone: stoic, self-contained — independence without sentimentality.
```renpy
# BEFORE:
"It is what it is. Don't romanticize it.":
    pass

# AFTER:
"It is what it is. Don't romanticize it.":
    $ sabra_independence += 1
```

#### Ch5 scene24 Big Elk, "The formalities are appreciated."
Tone: civil distance, not hostility — a diplomatic register, slightly cool.
```renpy
# BEFORE:
"The formalities are appreciated.":
    pass

# AFTER:
"The formalities are appreciated.":
    $ sabra_direction -= 1
```

#### Ch5 scene27, "I'm here. I'm here."
Tone: presence without language — tender, without the complexity of "You came back." Quiet yancey_relationship bump.
```renpy
# BEFORE:
"I'm here. I'm here.":
    pass

# AFTER:
"I'm here. I'm here.":
    $ yancey_relationship += 2
```

---

### 2. ORPHAN flag: donna_name = "Felice" — add downstream gates ✅ COMPLETE

Choosing "Felice — for her mother" names the daughter for Felice Venable (Book Ch XII: *"Your skin! Your hands! Your hair!"*) rather than for the land. This decision deserves two callbacks.

**Ch3 scene14 ("five years alone"), add after reflection block (~line 65):**
```renpy
# ADD:
if donna_name == "Felice":
    n "She thought sometimes of the name she'd given the child: her mother's name, not the land's. She was not sure which of them she was proving wrong."
```
*Source: Book Ch XII, ~line 1727 — Felice Venable's criticism of Sabra's appearance on her return to Wichita; the mother-daughter dynamic is unresolved there. Also Ch XV, ~line 2038 — Sabra becoming the matriarch in her own right.*

**Ch5 scene26 (Donna's wedding), add before menu (~line 365):**
```renpy
# ADD:
if donna_name == "Felice":
    n "Donna. Her mother's name. She had carried it as a kind of argument. Now she was arguing with someone else entirely."
```
*Source: Book Ch XII, ~line 1775 — "The matriarch had lost her crown. Sabra was matriarch now of her own little kingdom." The naming choice loops back at the moment Donna leaves the household.*

---

### 3. ORPHAN flag: sabra_stood_alone — add readbacks ✅ COMPLETE

Flag is set in Ch2 scene11 ("I am enough") but only appears in chapter summaries. It should surface in the narrative.

**Ch3 scene14, add to the "five years alone" reflection (~line 65), after the donna_name check:**
```renpy
# ADD:
if sabra_stood_alone:
    n "She had done it alone once, the hardest thing. She had not forgotten that she was capable of it."
```
*Source: Book Ch XV, ~line 2038 — "It was not until he left her, and the years rolled round without him, that she developed her powers." Ferber frames the birth and the five years as the same transformation.*

**Ch4 scene23, inside the sabra_independence >= 7 flavor block (~line 675):**
```renpy
# ADD alongside the existing independence flavor:
if sabra_stood_alone and yancey_relationship < 50:
    n "There had been a night she had made herself remember on the harder evenings: the one night she had told them not to send for him. She had been right then. Probably she had been right before that, too."
```
*Source: Book Ch XV, ~line 2058 — "She told herself that he was dead." The stoic continuity from birth to the years of rumor.*

---

### 4. ORPHAN flag: sabra_shielded_cim — add Ch3 scene15 readback ✅ COMPLETE

Flag set in Ch2 scene8; only read in Ch5 scene24 (one line). Add a callback when Yancey returns and encounters Cim.

**Ch3 scene15 (Yancey's return), after Yancey and Cim meet (~line 165):**
```renpy
# ADD:
if sabra_shielded_cim:
    n "Cim had stepped forward to greet him without hesitation — without the instinctive flinching she had once seen in him. She did not tell Yancey why that was."
```
*Source: Book Ch XIII, ~line 1839 — Cim running through the crowd to reach Yancey; the boy's easy physical confidence in chaos, which was Sabra's doing, not Yancey's.*

---

### 5. ORPHAN flag: sabra_stood_firm_danger — add Ch3 scene15 readback ✅ COMPLETE

Flag set three ways in Ch1 (typesetting minigame, two menu options); only read in Ch2 scene8 (~line 90). Add one more callback.

**Ch3 scene15 (Yancey's return), after the press/office moment (~line 155):**
```renpy
# ADD:
if sabra_stood_firm_danger:
    n "She had stayed at the press before, while worse things happened in the street. That had been her answer then. It was still her answer."
```
*Source: Book Ch XIII, ~line 1824 — the chaos of the Kid's capture and Sabra returning to find the office full, Yancey leaning against his desk. She is the stable center. The press is her anchor.*

---

### 6. ORPHAN flag: yancey_mystery — add Ch4 scene23 readback ✅ COMPLETE

Flag set repeatedly across Ch2–4; only one in-scene read (Ch5 scene27 narration). Add a readback while Sabra reads Yancey's letter.

**Ch4 scene23 (reading the letter, ~line 640):**
```renpy
# ADD after current yancey_mystery mention in summary — instead, add in-scene:
if yancey_mystery:
    n "She had stopped expecting his letters to explain him. There was a Yancey she had glimpsed, once or twice, that his letters never acknowledged. She read around it, as she always had."
```
*Source: Book Ch XV, ~lines 2042–2056 — the rumors about Yancey (squaw wife, drunk and dead, leader of the Doolin gang). Ferber renders the opacity of Yancey through accumulated rumor, none of which Sabra can confirm or deny.*

---

### 7. ORPHAN flag: sabra_confronted_mother — add Ch5 scene26 callback ✅ COMPLETE

Flag set Ch1 scene3; read only in Ch1 summary and Ch5 chapter5_summary. Should echo at Donna's wedding.

**Ch5 scene26, after Donna's wedding menu, before end (~line 390):**
```renpy
# ADD:
if sabra_confronted_mother:
    n "She had done this herself, once — stood in a parlor and said the thing that changed everything. She had not been forgiven quickly. She did not expect Donna to forgive quickly either."
```
*Source: Book Ch XII, ~line 1775 — "Sabra was matriarch now of her own little kingdom." The generational handoff is Ferber's explicit thematic turn.*

---

### 8. Meter: community_standing — add in-scene readbacks ✅ COMPLETE

`community_standing` is written by ~14 choices across five chapters but never gates a single in-scene line. Add three minimal readbacks.

**Ch3 scene17, before Tubbs delivers his ultimatum (~line 490):**
```renpy
# ADD before the Tubbs confrontation:
if community_standing >= 5:
    n "She had made something here. The women's club knew it. Even Sol knew it. Tubbs, who had been complaining about the Wigwam since the second issue, would know it too."
elif community_standing <= 0:
    n "She was not well liked, exactly. But she was known. That was different."
```
*Source: Book Ch XV, ~line 2026 — "The Oklahoma Wigwam had flourished in these last five years of her proprietorship." The narration ties standing to proprietorship; the advertisers' campaign is muted or loud depending on her established reputation.*

**Ch5 scene25 (congresswoman scene), after the endorsement (~line 230):**
```renpy
# ADD after receiving the endorsement:
if community_standing >= 8:
    n "There was a room full of people who had watched her work for thirty years. She had not expected it to feel like this."
elif community_standing <= 2:
    n "She was not the obvious choice. She suspected she was not anyone's first choice. She accepted the nomination anyway."
```
*Source: Book Ch XXII — Sabra receiving the nomination is rendered through the lens of accumulated civic authority, not personal warmth. Her standing is what earns it.*

---

### 9. Meter: yancey_relationship — tighten the Ch5 scene27 gate ✅ COMPLETE

The gate `yancey_relationship >= 50` is the default starting value. Almost every playthrough satisfies it, making the gating meaningless. Raise to 65.

```renpy
# BEFORE (script_chapter5.rpy ~line 491):
menu:
    "You came back." if yancey_relationship >= 50:
        $ yancey_relationship += 5

# AFTER:
menu:
    "You came back." if yancey_relationship >= 65:
        $ yancey_relationship += 5
```

*This reserves the line for players who have actively sustained closeness across four chapters — earned, not default. A player who let the relationship erode will find this word unavailable, which is the dramatically correct outcome.*

---

### 10. INCONSISTENCY: Ch4 missing journal_scene flags

Ch1–3 and Ch5 each set `journal_sceneN = True` after calling `journal_entry(...)`. Ch4 calls `journal_entry(...)` five times but never sets the corresponding flags, and those flags are not declared in `variables.rpy`.

**variables.rpy — add after `journal_scene18`:**
```renpy
# ADD:
default journal_scene19 = False
default journal_scene20 = False
default journal_scene21 = False
default journal_scene22 = False
default journal_scene23 = False
```

**script_chapter4.rpy — after each `journal_entry` call, add flag:**
```renpy
# After Scene 19 journal_entry (~line 164):
$ journal_scene19 = True

# After Scene 20 journal_entry (~line 365):
$ journal_scene20 = True

# After Scene 21 journal_entry (~line 479):
$ journal_scene21 = True

# After Scene 22 journal_entry (~line 587):
$ journal_scene22 = True

# After Scene 23 journal_entry (~line 725):
$ journal_scene23 = True
```

---

### 11. INCONSISTENCY: donna_wedding_advice default produces silent branch

Ch5 chapter5_summary reads `donna_wedding_advice` with three explicit values but no `else`. If the game is ever reached without scene26 firing (via skip or save-state import), the `"none"` default produces nothing.

**script_chapter5.rpy, chapter5_summary (~line 945):**
```renpy
# ADD after the three donna_wedding_advice branches:
else:  # donna_wedding_advice == "none" (skip or import)
    n "She had not had the chance to say anything to Donna. Or she had chosen not to."
```

---

## Ending Dispatch Verification

**Dispatch logic (chapter5_summary ~line 954–964):**
```
if indian_sympathy >= 7 and (sabra_independence >= 5 or yancey_relationship >= 50):
    ending_land_belongs
elif sabra_independence >= 8 and community_standing >= 8:
    ending_built_herself
elif sabra_independence <= 4 and yancey_relationship >= 65:
    ending_his_shadow_chosen
else:
    ending_his_shadow
```

### Path A: "The Land Belongs to All" (ending_land_belongs)

Requires `indian_sympathy >= 7`. On a full advocate run:

| Scene | Choice | indian_sympathy delta | Running total |
|---|---|---|---|
| scene10 M5 | Accept Arita's documents | +3 | 3 |
| scene12 Arita | "She stays." | +3 | 6 |
| scene15 reward | Give to Kid's family | +1 | 7 |
| scene16 letters | 2 pro-Indian letters printed | +2 | 9 |
| scene21 statehood | Single state | +2 | 11 |
| scene24 Ruby | "Welcome to our family." | +3 | 14 |

Threshold of 7 is reached before scene15. This path is comfortable. `sabra_independence >= 5` is easily satisfied on a parallel independence track; `yancey_relationship >= 50` is essentially always satisfied. **Verified.**

### Path B: "She Built It Herself" (ending_built_herself)

Requires `sabra_independence >= 8` AND `community_standing >= 8`. This is the tightest ending because several high-independence choices lower community_standing (especially Indian advocacy choices). A community-focused path:

| Scene | Choice | sabra_independence | community_standing |
|---|---|---|---|
| (start) | — | 0 | 0 |
| scene8 M1 | Step forward for Cim | +2 | — |
| scene8 collection | 3 catches | — | +3 |
| scene11 birth | "I am enough." | +3 | — |
| scene12 Dixie | Abstain | — | -1 (abstain: direction -1 only) |
| scene12 Arita | Propose auxiliary | — | +1 |
| scene14 | Through the community | +2 | +3 |
| scene15 | Stayed at press | +3 | — |
| scene16 editorial | General civic | — | +2 |
| scene17 Isaiah M6 | "You should be writing" | +2 | +1 |
| scene18 war | "I have the paper. Go." | +2 | — |
| scene19 parade | Wave herself | — | +2 |
| scene20 hallway | "I hope you find peace…" | — | +1 |
| scene22 oil | Story of the decade | +1 | +2 |
| scene23 stock | "I chose this." | +1 | +1 |
| scene25 run | "Yes. I'll run." | +2 | +3 |

Running totals: `sabra_independence` ≈ 18, `community_standing` ≈ 18. Both thresholds easily met on this path. **Verified.** (The structural tension noted in Design Note #2 is real, but a player who moderates their Indian advocacy can reach this ending.)

### Path C: "She Chose the Shadow" (ending_his_shadow_chosen)

Requires `sabra_independence <= 4` AND `yancey_relationship >= 65`. On a devoted-wife run:

| Scene | Choice | sabra_independence | yancey_relationship |
|---|---|---|---|
| (start) | — | 0 | 50 |
| scene8 M2 | Take his hand openly | — | +5 |
| scene9 | Say nothing | +2 | +5 |
| scene11 birth | "Go — and ride for Yancey." | -1 | — |
| scene13 | "Take me with you." | +2 | +5 |
| scene15 | She went to him immediately | — | +5 |
| scene15 reward | Give to Kid's family | — | +3 |
| scene19 alone | "Tell me everything." | — | +10 |
| scene21 letter | "He's right. I'll say so." | — | +5 |
| scene23 letter | Write back | — | +5 |
| scene23 stock | "I'm still waiting." | -1 | +5 |

Running totals: `sabra_independence` ≈ 2, `yancey_relationship` ≈ 98 (capped at 100). Both thresholds met. **Verified.** A pure devoted-wife path easily satisfies this ending's gates.

### Path D: "She Was His Shadow" (default)

All mixed or moderate playthroughs fall here — players who are moderately independent, moderately close to Yancey, and without a strong Indian-sympathy or community-building run. This is the most common outcome for a first playthrough without strong directional choices. **No reachability concern.**

---

## Prose Voice Reference

For all proposed new dialogue lines, the register models are the existing journal entries in `script_chapter1.rpy` (labels `_call_journal_scene1a` through `_call_journal_scene7`). Key characteristics:

- **Concrete and physical:** "My fingers are black with ink and my back aches." Never abstract. Objects, bodies, weather.
- **Wry brevity:** "Cim has decided he is an Indian." One sentence does the work of three.
- **Reserved interiority:** Emotions are named obliquely, not stated. "I find I do not mind at all" rather than "I was pleased."
- **Period diction:** "I confess," "I suspect," "in spite of," "I ought to." No contemporary phrasing.
- **No pioneer mythology:** Sabra doesn't romanticize. She notes, sometimes mordantly. The land is a fact, not a symbol.

The proposed readbacks above have been drafted to match this register. Each new line is one or two sentences, in Sabra's interior voice, grounded in a specific object or action from the scene context.
