## script_chapter4.rpy
## Cimarron: Chapter Four — War Hero, Statehood, Oil
## Based on Cimarron by Edna Ferber (1929), public domain.
##
## Scene structure:
##   scene19_rough_rider      → Yancey returns from Cuba in Rough Rider uniform
##   scene20_dixie_trial      → Dixie Lee's trial; trial arguments minigame
##   scene20_trial_result     → applies minigame bonuses
##   scene20_post_verdict     → verdict, hallway, editorial
##   scene21_statehood        → statehood debate; Yancey's letter
##   scene22_first_oil        → first oil strikes; Cim and oil
##   scene23_what_yancey_left → Yancey's absence; Donna leaves east; Sabra takes stock


## ─── Entry Point ──────────────────────────────────────────────────────────────

label chapter4_start:
    $ renpy.block_rollback()

    scene black with fade

    "CIMARRON"
    "{i}Based on the novel by Edna Ferber{/i}"
    "Chapter Four: War Hero, Statehood, Oil"
    " "
    "{i}Osage, Oklahoma Territory. 1898–1907.{/i}"

    play music "audio/hero_return.ogg" fadein 1.5 loop

    jump scene19_rough_rider


## ─── SCENE 19 — The Rough Rider Returns ──────────────────────────────────────

label scene19_rough_rider:

    scene bg_osage_street_1900 with dissolve

    play sound "sfx/horse_gallop_single.ogg"
    "He came back in September."

    "Word ran ahead of him — of course it did, with Yancey Cravat — carried by riders from Guthrie and then from Enid: the Rough Rider, home from Cuba, wearing the hat."

    "The town of Osage, which now had sidewalks and a hotel and one electric streetlamp at the corner of Pawhuska and Second, turned out to see him."

    show yancey roughrider neutral at left with dissolve
    show sabra ch4 neutral at right with dissolve

    "He rode in on the grey, broad-brimmed khaki hat with the crossed sabers pinned on one side, the brown canvas coat over his shoulders like a mantle."

    "Sol Levy was in the front row. Doc Valliant was beside him."

    "Yancey Cravat stood on the wagon bed that someone had driven into the square for the purpose, and the setting sun was exactly behind him, and the crowd was completely his."

    "Sabra stood at the edge of the platform. She was part of the pageant."

    ## ── Choice 1: The Public Moment ────────────────────────────────────────────

    menu:
        "The crowd was cheering. Yancey had not yet spoken. What did Sabra do:"

        "Stand beside him. Smile. This is his moment.":
            $ yancey_relationship += 5
            show sabra ch4 tender
            "She stepped forward onto the wagon bed and stood beside him."
            "She gave him this freely. She knew what it cost and she gave it."
            sabra "{i}He deserves this. And I am glad to be beside him for it.{/i}"
            "The crowd cheered for them both."

        "Step back. Let him have it alone.":
            $ sabra_independence += 1
            "She moved to the edge of the platform and let the crowd's attention find him without her in the way."
            "She was glad he was safe. But she was also, irrevocably, her own person now."
            sabra "{i}He has always known how to fill a room. I am learning not to need to.{/i}"

        "Wave to the crowd herself — a gesture of partnership.":
            $ community_standing += 2
            show sabra ch4 proud
            "She raised one hand to the crowd — a small wave, deliberate and confident."
            "The crowd cheered for her too."
            "That was new."
            sabra "{i}They know my name. That, too, is new.{/i}"

    ## ── The speech ─────────────────────────────────────────────────────────────

    "He spoke for twenty minutes."

    "He spoke about the men who had died at San Juan — their names, their faces, where they were from. He spoke about Roosevelt with the particular admiration of a man who had found, for once, someone as genuinely enormous as himself."

    yancey "Cuba taught me one thing I already knew: this country is bigger and stranger and better than anyone in Washington believes it to be."

    "The crowd roared."

    "Sabra watched him and thought: I have run a newspaper for eight months. I have made payroll three times without him. I have written twelve editorials, six of which he would have disagreed with, and I sent every one of them to press."

    show sabra ch4 proud
    "She watched him and was proud."

    if sabra_direction >= 5:
        "She watched him work the crowd and felt, against her better judgment, the pull of it — the showman in the saddle, the country at his stirrup. She had married that, once. She had also, in his absence, become it."
    elif sabra_direction <= -5:
        "She watched the spectacle as one watches weather: with an interest that did not include approval. Eight months of running the paper had taught her the difference between a headline and a man."
    else:
        "She watched, and did not yet know what she felt."

    if sabra_cleared_the_office:
        "She had stood at the press when he came back last time — from the Kid, bloody and returned. She had not crossed the floor. She had let him find her there. She did not cross it now."

    ## ── Private reunion ────────────────────────────────────────────────────────

    scene bg_wigwam_modern with dissolve
    play music "audio/oil_derricks.ogg" fadein 1.5 loop

    show sabra ch4 neutral at right with dissolve
    show yancey roughrider weary at left with dissolve

    "That evening, alone at last."

    "He was thinner. New lines around his eyes. He was thirty-eight and looked like a man who had been to war, which he had."

    yancey "I hear you didn't miss an edition."

    sabra "Not one."

    yancey "I knew it."

    sabra "Did you."

    ## ── Choice 2: The Private Reunion ──────────────────────────────────────────

    menu:
        "The first evening alone:"

        "\"Tell me everything. From the beginning.\"":
            $ yancey_relationship += 10
            sabra "Tell me everything. I want to hear it from you, not the newspapers."
            "He talked until midnight."
            "She listened without interruption. He told her about the heat, the mud, the men who had come from every state in the union to die on a Cuban hillside for a cause they understood imperfectly."
            "He told her about a moment, near the top, when he had thought he might not come back."
            show yancey roughrider tender
            "She listened to that part without moving."
            "It was one of the best nights of their marriage."

        "\"I need to tell you what happened here while you were gone.\"":
            $ sabra_independence += 2
            sabra "I want to tell you what has happened here. Eight months is a long time."
            "He listened."
            "She told him about the school board vote, about the editorial on Indian allotment that had cost them two advertisers and gained them thirty subscribers, about the night the press had jammed at ten o'clock and she had fixed it herself with a hairpin and a piece of baling wire."
            "He listened to all of it."
            "This, too, was new."

        "\"I'm glad you're home.\"":
            $ yancey_relationship += 5
            sabra "I'm glad you're home, Yancey."
            "She meant it without qualification."
            show yancey roughrider tender
            "He looked at her a long moment."
            yancey "Sabra."
            "He said her name like it was a complete sentence. Tonight, that was enough."

    hide yancey
    hide sabra

    call journal_entry("Scene 19", "He came home in a soldier's hat with the brim pinned up on one side. He still has both six-shooters. I counted: eight notches now.") from _call_journal_scene19

    jump scene20_dixie_trial


## ─── SCENE 20 — Dixie Lee's Trial ────────────────────────────────────────────

label scene20_dixie_trial:

    scene bg_courthouse_interior with dissolve
    play music "audio/courthouse_quiet.ogg" fadein 1.5 loop

    "1899."

    "Dixie Lee had been charged under a new ordinance pushed by the Philomathean Club and two of the town's three ministers."

    "The charge: operating a disorderly house."

    "The evidence was, by any fair reading, overwhelming."

    "Yancey took her case. Pro bono. Because — he said — the law must be the same for everyone."

    show sabra ch4 neutral at right with dissolve
    show yancey neutral at left with dissolve

    sabra "I need to understand what you are doing."

    yancey "I'm defending a woman who can't get a fair hearing any other way."

    sabra "Half this town will read it as you defending — the other thing."

    yancey "Half this town can come to the courtroom and listen to the argument. That's what courts are for."

    ## ── Choice 1: Sabra's Private Reaction ─────────────────────────────────────

    menu:
        "Sabra's answer, the night before the trial:"

        "\"I think you're wrong. She chose this.\"":
            $ yancey_relationship -= 5
            $ newspaper_stance -= 1
            show sabra ch4 neutral
            sabra "I think you're wrong, Yancey. She is not a victim. She made choices."
            yancey "Most of those women didn't choose anything. They arrived with nothing and this was what the territory offered."
            "The argument went nowhere. They slept on opposite sides of the bed."

        "\"I think you're right. I hate that you're right.\"":
            $ yancey_relationship += 5
            $ indian_sympathy += 1
            show sabra ch4 tender
            sabra "I think you're right. I hate that you're right, but I think you are."
            "He looked at her steadily."
            "He had been waiting years for her to say something like this."
            yancey "That took something."
            sabra "Don't make more of it than it is."

        "\"Tell me the legal argument. I need to understand it.\"":
            $ newspaper_stance += 1
            $ sabra_independence += 1
            sabra "Explain the legal argument to me. If I'm going to write the editorial, I need to understand the case."
            "He explained. She listened. She asked four questions he hadn't expected."
            "She was not conceding. She was preparing."
            "The editorial would be the hardest she had written."

    hide yancey

    ## ── Minigame setup ─────────────────────────────────────────────────────────

    "The night before the trial, Yancey spread six slips of paper across the kitchen table."

    show yancey neutral at left with dissolve

    yancey "I can't use them all. Three is the number. Opening, middle, close. You know a good argument, Sabra. Which three?"

    "He was asking her. She couldn't decide if it was an insult or a compliment."

    hide yancey
    hide sabra

    $ trial_sel   = []
    $ trial_ord   = [None, None, None]
    $ trial_phase = 1
    $ result = renpy.call_screen("trial_arguments_minigame")
    $ _sel, _ord = result
    jump scene20_trial_result


## ─── SCENE 20 — Trial Result ─────────────────────────────────────────────────

label scene20_trial_result:

    ## Selection bonuses
    if 2 in _sel:
        $ yancey_relationship += 5
    if 3 in _sel:
        $ newspaper_stance += 1
    if 5 in _sel:
        $ yancey_relationship += 3
        $ community_standing -= 1
    if 6 in _sel:
        $ newspaper_stance += 1
    if 1 in _sel and 4 in _sel:
        $ newspaper_stance -= 1
        $ yancey_relationship -= 3

    ## Ordering bonuses
    if len(_ord) >= 3:
        if _ord[2] == 2:
            $ yancey_relationship += 3
        if _ord[0] == 5:
            $ community_standing -= 1
        if _ord[0] == 6:
            $ newspaper_stance += 1

    jump scene20_post_verdict


## ─── SCENE 20 — Post Verdict ─────────────────────────────────────────────────

label scene20_post_verdict:

    scene bg_courthouse_interior with dissolve

    show sabra ch4 neutral at right with dissolve

    "The courtroom was full. The Philomathean Club occupied one entire pine bench."

    "Yancey argued for two hours. He named no one by name. He made the case in clean, careful language that even Sabra's most skeptical readers would have had difficulty dismissing."

    "The jury deliberated for forty minutes."

    show sabra ch4 worried
    "She was not sure, until the foreman stood, whether she wanted them to say guilty or not."

    "Not guilty."

    show sabra ch4 neutral
    play sound "sfx/courtroom_reaction.ogg"
    "The room erupted. Half of it cheered. The other half sat in stunned silence."

    ## ── Choice 2: The Editorial ─────────────────────────────────────────────────

    "She was at her desk that night. The Wigwam went to press Thursday."

    menu:
        "What Osage needed to read:"

        "\"The verdict was just. The law protected a woman others wanted to punish.\"":
            $ newspaper_stance += 2
            $ community_standing -= 1
            $ dixie_lee_editorial = "support"
            sabra "{i}This verdict does not celebrate the trade. It protects the person. Those are not the same thing, and the Wigwam will not pretend they are.{/i}"
            "Yancey read it and said nothing. He looked at her a long time."
            yancey "You didn't have to do that."
            sabra "I know."

        "\"This court has failed Osage's women and children.\"":
            $ newspaper_stance -= 2
            $ community_standing += 2
            $ dixie_lee_editorial = "oppose"
            sabra "{i}Whatever the law says, the community that allows this trade to stand unremarked has decided something about what it values. The Wigwam does not share that decision.{/i}"
            "Half the town nodded. Dixie Lee sent no note."

        "\"Report the facts only. The community will decide.\"":
            $ sabra_independence += 1
            $ dixie_lee_editorial = "neutral"
            sabra "{i}The jury returned a verdict of not guilty. The Wigwam reports this finding. The Wigwam declines to instruct its readers on what to feel.{/i}"
            "The most journalistic choice. Also the loneliest."

    ## ── Choice 3: Dixie Lee in the Hallway ─────────────────────────────────────

    scene bg_courthouse_interior with dissolve
    show dixie neutral at center with dissolve
    show sabra ch4 neutral at right with dissolve

    "In the hallway after the verdict."

    "Dixie Lee was wearing dove gray. She looked at Sabra directly. It was the first time she had done so without flinching."

    menu:
        "Sabra's response:"

        "\"I hope you find peace in whatever you do next.\"":
            $ community_standing += 1
            sabra "I hope you find peace in whatever you do next, Dixie."
            "Dixie Lee: 'Thank you, Mrs. Cravat.' That was all. It was enough."

        "\"Your man won. That's all this is.\"":
            sabra "Your man won. That's all this is."
            "A closed door."
            "Neutral."

        "Say nothing. Walk past.":
            $ community_standing -= 1
            "Sabra walked past."
            "She knew, walking away, that she was the smaller person."
            "She kept walking."

    hide dixie
    hide sabra

    call journal_entry("Scene 20", "Not guilty. I sat in the gallery and watched the jury file in and I was not sure, until the foreman spoke, whether I wanted them to say guilty or not. I still don't know.") from _call_journal_scene20

    jump scene21_statehood


## ─── SCENE 21 — The Statehood Question ───────────────────────────────────────

label scene21_statehood:

    scene bg_civic_hall with dissolve
    play music "audio/state_seal.ogg" fadein 1.5 loop

    "1901–1906."

    "The great question: would the Indian Territory and the Oklahoma Territory be joined into one state, or two?"

    show sabra ch4 neutral at center with dissolve

    "A delegation from the Double Statehood party came to the Wigwam on a Tuesday morning — three men in good suits, carrying a petition."

    "Two days later, a delegation from the Single Statehood party came — two lawyers and a minister, carrying different arguments."

    "Sabra listened to all of them."

    "Then she sat alone at her desk with the arguments in front of her and Yancey's letter — forwarded from somewhere in the Cimarron country — on top of the pile."

    ## ── Choice 1: The Editorial Stance ─────────────────────────────────────────

    menu:
        "The Wigwam's editorial position on statehood:"

        "\"Oklahoma Territory and Indian Territory must be one state. The people cannot be divided.\"":
            $ newspaper_stance += 2
            $ indian_sympathy += 2
            $ statehood_stance = "single"
            show sabra ch4 determined
            sabra "The people of these territories have lived beside one another for seventeen years. The law that divides them now was the law of a different century."
            "She wrote it in three hours."
            "It was a bold position. It cost her some subscribers. She believed it was correct."

        "\"Two states is the safer, more stable choice for both peoples.\"":
            $ newspaper_stance -= 2
            $ indian_sympathy -= 1
            $ statehood_stance = "double"
            show sabra ch4 determined
            sabra "The interests of the Indian Nations and of the Oklahoma settlers are not identical. Two states allows each people to govern itself."
            "She wrote carefully, without cruelty. The position was defensible. She was not entirely satisfied with it."

        "\"The Wigwam cannot advocate without consultation with the affected communities.\"":
            $ sabra_independence += 2
            $ statehood_stance = "consult"
            show sabra ch4 determined
            sabra "I am going to the Osage Reservation before I write a word."
            "She went to Pete Pitchlyn. She went to the women's club. She went to the men who would be subject to whatever the state became."
            "Then she wrote."

    ## ── Choice 2: Yancey's Letter ───────────────────────────────────────────────

    "His handwriting was large and slanted and full of underlines, as always."

    "He had written at length about the Indian's right to be part of the new state as equals — passionately, characteristically, from wherever he was in the Cimarron country."

    menu:
        "Regarding Yancey's letter:"

        "\"He's right. I'll say so.\"":
            $ yancey_relationship += 5
            $ indian_sympathy += 1
            sabra "{i}He is right about this. I have my own reasons now, but he was right first.{/i}"
            "She said so in the editorial."

        "\"He's not wrong, but he's not here. I'll decide this myself.\"":
            $ sabra_independence += 2
            $ yancey_relationship -= 5
            sabra "{i}He is not wrong. But he is also not here. He does not get to make this decision from the Cimarron country.{/i}"
            "She decided for herself."

        "\"I'll print his letter. Let the readers see his argument.\"":
            $ newspaper_stance += 1
            sabra "The Wigwam will print his letter alongside the editorial. Let the readers hear both voices."
            "She ran it in the left column, her editorial in the right."

    ## ── Statehood Day ───────────────────────────────────────────────────────────

    "November 16, 1907."

    play sound "sfx/celebration_bells.ogg"
    "They rang the church bell at noon. Someone fired a cannon in the square."

    show sabra ch4 proud
    show doc neutral at left with dissolve

    "Doc Valliant came to the Wigwam with a bottle of whisky."

    doc "Well, Sabra. We made it."

    sabra "We did."

    if sabra_direction >= 5:
        "It tasted of dust and powder and printer's ink, the way every honest thing in Oklahoma had ever tasted."
    elif sabra_direction <= -5:
        "She accepted the glass with the same composure she had once accepted teacups in her mother's parlor. The composure, she had discovered, traveled."

    hide doc

    sabra "{i}We made it without him. I didn't say that part aloud. I thought it.{/i}"

    if newspaper_stance >= 5:
        "The Wigwam had been the closest thing to a conscience the territory had. She did not know yet what it would be to a state."
    elif newspaper_stance <= -3:
        "The Wigwam had been the safest paper in the territory — reasonable, trusted, careful. States needed such papers too, she supposed. Someone had to be reasonable."

    hide sabra

    call journal_entry("Scene 21", "November 16, 1907. Oklahoma is a state. They rang the church bell at noon and fired a cannon in the square and Doc Valliant came to the office with a bottle of whisky and said, 'Well, Sabra, we made it.' I said we did. I didn't say what I was thinking: that we made it without him.") from _call_journal_scene21

    jump scene22_first_oil


## ─── SCENE 22 — The First Oil ────────────────────────────────────────────────

label scene22_first_oil:

    scene bg_oil_derrick_distant with dissolve
    play music "audio/oil_derricks.ogg" fadein 1.5 loop
    play sfx "sfx/oil_drill.ogg" fadein 2.0 loop

    "1905."

    "A rancher near the Osage Reservation noticed a rainbow sheen on the surface of his stock pond."

    "Someone brought a geologist. The geologist brought investors."

    show sabra ch4 neutral at center with dissolve

    "The word began to appear in the Wigwam's pages."

    "Sabra wrote it with increasing frequency and uncertainty."

    sabra "{i}Oil. That is the word. It means money — more money than I have ever imagined — and it means something else, something I can't quite name yet.{/i}"

    "The derricks went up on the horizon. At night you could see the flare-off fires from the bedroom window."

    ## ── Choice 1: The Oil Story ─────────────────────────────────────────────────

    menu:
        "The Wigwam's approach to covering oil:"

        "\"This is progress. Cover it fully — the good and the risk.\"":
            $ newspaper_stance += 1
            $ community_standing += 1
            sabra "The Wigwam will cover the oil economy the way it covers everything: completely and honestly."
            "Even-handed journalism. The town respected it."
            "She was not sure she respected herself for how much she enjoyed the story."

        "\"Oil brings the wrong kind of people. Be careful what you celebrate.\"":
            $ newspaper_stance -= 1
            sabra "The men who follow oil are not the men who built Osage. I will not pretend otherwise."
            "She was not entirely wrong. She was also not entirely right."

        "\"This is the story of the decade. The Wigwam will own it.\"":
            $ sabra_independence += 1
            $ community_standing += 2
            sabra "I am writing to papers in New York and Chicago. The Wigwam will be the paper of record on Oklahoma oil."
            "Aggressive, ambitious journalism. Letters came back from editors she had never imagined reading her work."

    ## ── Cim and Oil ─────────────────────────────────────────────────────────────

    scene bg_wigwam_modern with dissolve
    show sabra ch4 neutral at right with dissolve
    show cim neutral at left with dissolve

    "Cim was twenty. Home for the summer from Colorado, where he had been studying geology."

    "The oil companies had already found him."

    "He had his father's magnetism and his mother's practicality. The combination, she had noticed, made him dangerous to himself."

    "Yancey had named him Cimarron — after the wild country, the unruly river, the land that couldn't be tamed. She had argued against it at the time. Too much to carry, she had said. And Yancey had laughed."

    "Standing in the Wigwam doorway watching her son calculate survey coordinates in his head, she thought perhaps the name had been a prophecy."

    cim "There's a company out of Tulsa that wants to talk to me, Mother. About the surveys east of the reservation."

    ## ── Choice 2: Cim and Oil ───────────────────────────────────────────────────

    menu:
        "Sabra's counsel to her son:"

        "\"Finish your degree first.\"":
            sabra "Finish the degree, Cim. The oil will still be there in two years."
            "He listened. He went back to Colorado."
            "She knew, watching him go, that he would not stay in Colorado."

        "\"If this is what you want, learn all of it before you commit.\"":
            sabra "If this is the path, learn everything about it before you sign anything. The men who do well in oil are the ones who understood it before anyone else did."
            cim "Yes, ma'am."
            "He was already making calculations in his head."

        "\"Your father would tell you to stay out of it. I don't know if he's right.\"":
            $ yancey_relationship += 5
            sabra "Your father always said the oil men were the new railroad men. That they would eat the territory alive. I don't know if he was right."
            "Cim looked at the window."
            cim "Where is he?"
            sabra "Somewhere in the Cimarron country. He writes."
            "She did not add: not often."

    hide cim with dissolve
    show tracy neutral at left with dissolve

    "A young man appeared in the Wigwam's doorway that afternoon — Tracy Wyatt, home from an Eastern school, carrying his father's oil money and his own considerable ambitions."

    "He was there to buy advertising space."

    "He looked, briefly, at [donna_name]'s photograph on Sabra's desk."

    "She did not notice."

    hide tracy
    hide cim
    hide sabra

    call journal_entry("Scene 22", "The derricks on the horizon look like enormous iron insects. At night you can see the flare-off fires from the bedroom window. The smell of crude oil drifts into town when the wind blows from the northeast. I keep writing it up as progress. I'm not sure I believe myself.") from _call_journal_scene22

    jump scene23_what_yancey_left


## ─── SCENE 23 — What Yancey Left ────────────────────────────────────────────

label scene23_what_yancey_left:

    scene bg_wigwam_modern with dissolve
    stop sfx fadeout 1.5

    "1907."

    "He had been somewhere for most of the last nine years. He sent letters occasionally. He appeared rarely."

    "When he appeared, the town stopped to watch."

    show sabra ch4 neutral at center with dissolve

    "Sabra did not stop to watch anymore."

    "A letter came. He was in the Cimarron country, he said. Working for something or other. Coming home soon."

    show sabra ch4 weary
    "He always said he was coming home soon."

    ## ── Choice 1: The Letter ────────────────────────────────────────────────────

    menu:
        "What Sabra did with the letter:"

        "\"Write back. Tell him about [donna_name] and Cim.\"":
            $ yancey_relationship += 5
            sabra "{i}I will write him a letter. A careful one. Kinder than my feelings.{/i}"
            "She wrote him about [donna_name]'s plans for Miss Dignum's school on the Hudson. About Cim and the oil surveys. About the new telephone on the office wall."
            "She sealed it and addressed it to the last return address, knowing he might not be there when it arrived."

        "\"File it with the others. Don't write back.\"":
            $ sabra_independence += 2
            $ yancey_relationship -= 5
            sabra "{i}I have dozens of his letters. I have kept them all. I have answered fewer and fewer.{/i}"
            "She put it in the drawer with the others."
            "It was not cruelty. It was accuracy."

        "\"Read it to the children. Let them decide how they feel.\"":
            sabra "Come sit down, both of you. Your father has written."
            show cim neutral at left with dissolve
            show donna ch4 neutral at right with dissolve
            "She read it aloud."
            "Cim's face was careful, as always. [donna_name] rolled her eyes at a specific sentence and then caught herself."
            "Sabra removed herself as interpreter of Yancey. That was the most generous thing she knew how to do."
            hide cim
            hide donna

    ## ── A family supper ────────────────────────────────────────────────────────

    scene bg_wigwam_modern with dissolve

    show cim neutral at left with dissolve
    show donna ch4 neutral at right with dissolve
    show sabra ch4 neutral at center with dissolve

    "Supper that week."

    donna "Mother. Miss Dignum's has a place for me in January."

    sabra "I know. I arranged it."

    "[donna_name] blinked."

    donna "You knew I wanted to go?"

    sabra "You have never made a secret of your feelings about the frontier."

    "[donna_name], to her credit, laughed."

    cim "I'm going back east too. Tulsa, anyway. The oil survey."

    "He said it quietly, as a statement of fact."

    "Sabra looked at her two children and thought: I raised them to leave. That is what raising children is."

    if sabra_independence >= 7:
        "She noted this without grief. She had raised them on a frontier, and the frontier's first lesson was that staying was not the point."
    elif sabra_independence <= 3:
        "She noted this with a complicated feeling she did not have time, yet, to fully sort out."

    hide cim
    hide donna

    ## ── Choice 2: Taking Stock ──────────────────────────────────────────────────

    show sabra ch4 neutral at center with dissolve
    "Alone at the desk, after they'd gone."

    "She was the editor of a newspaper. President of two civic organizations. Mother of two grown children. The most recognizable woman in a hundred miles."

    "What she was not: the wife of a man who stayed."

    if sabra_direction >= 5:
        "She set the ledger down without ceremony. The list was, on balance, a victory; she did not need to dress it up to know it."
    elif sabra_direction <= -5:
        "She closed the ledger and aligned its edge with the desk. The list was, by any decent reckoning, a creditable one — and creditable, in her mother's vocabulary, had always been the highest praise."

    if sabra_stood_alone:
        "She had brought [donna_name] into the world without him. She had done that, and then kept going."
    if isaiah_defended:
        "Isaiah had learned to set type in this room. She thought about him sometimes — what he might have become, if the town had let him."

    menu:
        "How Sabra regarded what she had built:"

        "\"I chose this. I'd choose it again.\"":
            $ sabra_independence += 1
            $ community_standing += 1
            show sabra ch4 determined
            sabra "{i}I chose this. All of it — the press, the town, the absence, the presence. I would choose it again.{/i}"
            "She meant it. The freedom was real, even if it had cost something she hadn't planned to pay."

        "\"It is what it is. Don't romanticize it.\"":
            show sabra ch4 weary
            sabra "{i}It is what it is. Don't make it a tragedy and don't make it a triumph. It is just what happened. It is a life.{/i}"
            "The most honest thing she could say. She said it to herself and meant it."

        "\"I'm still waiting. I don't think I'll stop.\"":
            $ yancey_relationship += 5
            $ sabra_independence -= 1
            show sabra ch4 tender
            sabra "{i}I am still waiting. I have built everything I have built and I am still — after all of it — still waiting for him.{/i}"
            "A quiet admission. Not weakness. Just truth."

    hide sabra

    scene black with dissolve

    "— End of Chapter Four —"

    call journal_entry("Scene 23", "[donna_name] leaves for Miss Dignum's on the Hudson on Monday. She packed three times and was still dissatisfied. She has absolutely no aptitude for the frontier and I could not be more proud of her.") from _call_journal_scene23

    call chapter4_summary from _call_chapter4_summary

    return


## ─── CHAPTER 4 SUMMARY ───────────────────────────────────────────────────────

label chapter4_summary:

    stop music fadeout 1.5
    scene bg_journal with fade
    play music "audio/state_seal.ogg" fadein 2.5 loop
    play sound "sfx/paper_rustle.ogg"
    "CHAPTER FOUR COMPLETE"
    "— from Sabra's ledger —"

    ## Yancey relationship
    show yancey neutral at left with dissolve
    if yancey_relationship >= 65:
        "YANCEY & SABRA: Deeply trusting, even across the silences. She knows what he is. He knows what she has become."
    elif yancey_relationship >= 35:
        "YANCEY & SABRA: Balanced — real and complicated, with distances that have grown familiar."
    else:
        "YANCEY & SABRA: Strained. She has built something he cannot quite reach, and she is no longer sure she minds."

    ## Sabra's direction + newspaper stance + community standing
    hide yancey with dissolve
    show sabra ch4 neutral at right with dissolve
    if sabra_direction >= 8:
        "SABRA'S PATH: Frontier Woman. The person who arrived in a silk dress from Wichita is a distant memory."
    elif sabra_direction <= -5:
        "SABRA'S PATH: Refined Lady. She has kept the old standards. They have kept her."
    else:
        "SABRA'S PATH: Her Own. Neither Wichita nor the frontier entirely owns her now."

    if newspaper_stance >= 5:
        "THE WIGWAM: Progressive — advocate for the Indian Nations, women's voice, oil watchdog. It has made enemies. It has also made history."
    elif newspaper_stance <= -3:
        "THE WIGWAM: Conservative — careful, community-minded, advertiser-safe. It is trusted by the right people."
    else:
        "THE WIGWAM: Balanced — it prints what it believes, mostly. The rest, it is learning."

    if community_standing >= 6:
        "STANDING IN OSAGE: Beloved. The town would not be what it is without Sabra Cravat."
    elif community_standing <= -3:
        "STANDING IN OSAGE: Complicated. She has made the right enemies."
    else:
        "STANDING IN OSAGE: Respected. They know her name and mean it."

    ## Indian sympathy
    show arita neutral at right with dissolve
    if indian_sympathy >= 5:
        "ON THE INDIAN QUESTION: Advocate — her name is known in the Nations as someone who could be trusted."
    elif indian_sympathy <= -3:
        "ON THE INDIAN QUESTION: Accommodating — she has bent with the town's prejudices more than she would like to admit."
    else:
        "ON THE INDIAN QUESTION: Cautious, but changing."

    ## Dixie Lee editorial flag
    show dixie neutral at right with dissolve
    if dixie_lee_editorial == "support":
        "She stood on the right side of that verdict and she knew it."
    elif dixie_lee_editorial == "oppose":
        "She wrote against the verdict. The town's women thanked her for it. Dixie Lee did not."
    elif dixie_lee_editorial == "neutral":
        "She printed the facts and let the community decide. It was the hardest kind of restraint."

    ## Statehood stance + newspaper high-water mark
    hide dixie with dissolve
    if statehood_stance == "single":
        "She published for one Oklahoma — one state, both peoples."
    elif statehood_stance == "double":
        "She published for two states. It was the careful choice. She is not sure it was the right one."
    elif statehood_stance == "consult":
        "She went to the reservation before she wrote a word. Some editors thought that was weakness. She thought it was journalism."

    if newspaper_stance >= 3:
        "The Wigwam she runs is not the paper Yancey founded. It is something more."

    play sound "sfx/paper_rustle.ogg"
    scene black with fade
    jump chapter5_start
