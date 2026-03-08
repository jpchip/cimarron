## script_chapter2.rpy
## Cimarron: Chapter Two — Building Osage
## Based on Cimarron by Edna Ferber (1929), public domain.
##
## Scene structure:
##   scene8_lion_streets    → Church tent shooting; collection minigame
##   scene9_seven_notches   → Yancey's past; the seven men
##   scene10_wigwam_lives   → Newspaper growth; Indian rights editorial
##   scene11_wind_donna     → Donna born; Yancey absent
##   scene12_respectability → Women's club; who belongs
##   scene13_cherokee_strip → Yancey rides out for the Strip

## ─── Entry Point ──────────────────────────────────────────────────────────────

label chapter2_start:
    $ renpy.block_rollback()

    scene black with fade

    "CIMARRON"
    "{i}Based on the novel by Edna Ferber{/i}"
    "Chapter Two: Building Osage"
    " "
    "{i}Osage, Oklahoma Territory. 1890–1893.{/i}"

    jump scene8_lion_streets


## ─── SCENE 8 — The Lion in the Streets ───────────────────────────────────────

label scene8_lion_streets:

    scene bg_tent_church with dissolve
    play music "audio/osage_sunday.ogg" fadein 1.5 loop

    "Sunday morning in Osage. The congregation gathered in a patched canvas tent — the only church the town had yet managed."

    "Oil lamps on bare pine posts. Hymn books held by people who had driven cattle, filed homestead claims, buried children in the hard red earth."

    show sabra ch2 neutral at right with dissolve

    sabra "I did not expect to feel at home here. And yet — I do. Partly."

    "The sermon had barely begun when the tent flap opened."

    "He was a broad-shouldered man with a face like a worn boot-heel. A gambler named Lon Yountis, who had crossed Yancey over a printing bill and had not forgotten it."

    show yancey neutral at left with dissolve

    "Yountis stood in the entrance with his hand near his holster. The congregation went still."

    "Lon Yountis: You still in town, Cravat. I come to collect what you owe me."

    show yancey dangerous
    yancey "Lon. You're standing in a house of God. I'd suggest you remove your hat and take a seat."

    "Lon Yountis: I'll remove your head before I sit in any—"

    "The congregation shifted. Children were pulled close. Sabra felt the cold move through her."

    menu:
        "When the gunman entered, Sabra's first instinct was:"

        "Step forward — put herself between Cim and the door.":
            $ sabra_direction    += 1
            $ sabra_independence += 2
            sabra "Move back, Cim. Stay behind me."
            "The boy pressed against her skirts without argument."
            "She had not thought about it. Her body simply knew."

        "Stay seated, hands folded, and pray.":
            $ sabra_direction -= 1
            sabra "Lord, let this pass."
            "Her mother had taught her that dignity was a form of armor. She wore it now."

    "Yancey did not raise his voice. He stood, slowly, and walked down the center aisle."

    show yancey dangerous
    yancey "You want to leave now, Lon. Before this gets complicated for both of us."

    "For one long moment, Yountis held. Then he read something in Yancey's eyes — something Sabra could not name — and he backed through the tent flap and was gone."

    "The congregation exhaled as one."

    show doc neutral at center with dissolve

    doc "Well. I have attended stranger services."

    menu:
        "After Yancey sat back down — Sabra's response:"

        "Reach across the pew and take his hand, openly.":
            $ yancey_relationship += 5
            show yancey neutral
            show sabra proud
            sabra "I am very proud of you."
            show yancey tender
            yancey "Don't be. He might have been faster."
            "She kept hold of his hand anyway."

        "Say nothing. Bow her head. Let the hymn resume.":
            $ yancey_relationship += 2
            $ sabra_independence  += 1
            "She had learned that some moments were not for words."
            "She let the singing begin again around her."

        "Feel the sickness of it — the nearness of violence.":
            $ yancey_relationship -= 3
            $ yancey_mystery       = True
            sabra "How can you be so calm?"
            yancey "Practice."
            "He said it lightly. She did not find it light."

    ## ── Church collection minigame ────────────────────────────────────────────

    "After the service, the collection hat was passed. Elder Howe asked Sabra to watch — her eyes were sharp, he said. Sharper than his."

    sabra "Watch for what, exactly?"

    "Elder Howe: There are members who give with one hand and take back with the other. You'll know them. You'll see the moment."

    ## Reset minigame state
    $ collection_time_left = 30
    $ collection_caught    = 0
    $ collection_flagged   = []

    call screen church_collection_minigame
    $ scene8_caught = _return

    call screen collection_result(scene8_caught)

    ## Apply community_standing bonus
    $ community_standing += scene8_caught

    if scene8_caught >= 3:
        "Every one of them. Sabra Cravat had caught every one."
        "Word moved through the congregation before they reached the wagon."
        "The town noticed."
    elif scene8_caught >= 1:
        "She caught [scene8_caught] of them. Not a bad eye for a Wichita girl."
        $ community_standing += 1
    else:
        "She had been watching — but the cheaters were practiced. They went home heavier than they came."

    hide doc
    hide yancey
    hide sabra

    $ journal_scene8 = True
    call journal_entry("SCENE 8", "The tent was cold even in July. A man came in wanting trouble and Yancey sent him away with only words — though I think the words were not the whole of it. I held Cim in front of me. I did not decide to. I watched the collection after. There are people here who take from the church as easily as they breathe. I am learning to see them.") from _call_journal_scene8

    jump scene9_seven_notches


## ─── SCENE 9 — Seven Notches ─────────────────────────────────────────────────

label scene9_seven_notches:

    scene bg_wigwam_office with dissolve
    play music "audio/wigwam_press.ogg" fadein 1.5 loop

    "The Oklahoma Wigwam. Evening. The press was quiet for once."

    "A man had come in that afternoon — Pete Pitchlyn, an old acquaintance of Yancey's from before the run. Weathered, quiet, with the kind of eyes that took inventory of a room before he stepped into it."

    show pete neutral at left with dissolve
    show yancey neutral at center with dissolve

    pete "You're doing well here, Yancey. I wouldn't have thought it."

    yancey "The territory agrees with me."

    pete "I heard about Lon Yountis. That makes what — seven? Or have I lost count?"

    "The room went quiet in a particular way."

    show yancey dangerous
    yancey "You always were bad at arithmetic, Pete."

    show pete sardonic with dissolve
    "Pete Pitchlyn smiled without warmth and left. Yancey stood at his type case and did not look at Sabra."

    hide pete

    show sabra ch2 neutral at right with dissolve

    "Seven. She had known he was a man of the frontier — had known, in the abstract, what that meant. But the number had a weight she had not felt before."

    menu:
        "Sabra's approach to what she had just heard:"

        "Ask him directly. \"Is it true? Seven men?\"":
            $ yancey_relationship -= 3
            $ yancey_mystery       = True
            show sabra worried
            sabra "Yancey. Is it true?"
            "He turned slowly."
            yancey "What Pete says and what is true are not always the same thing."
            sabra "That is not an answer."
            "He looked at her for a long moment. Then:"
            yancey "Some of them. Not all of them his way."
            "She had wanted the truth. Now she had a part of it."

            menu:
                "Hearing that —"

                "\"I understand. The territory has its own laws.\"":
                    $ yancey_relationship += 5
                    $ sabra_direction     += 2
                    show sabra determined
                    sabra "I married you knowing what you were. I will not unknow it now."
                    show yancey tender
                    yancey "You're a better woman than I deserve."
                    "She was not sure whether to be glad or frightened that he meant it."

                "\"I need time. Give me that.\"":
                    $ yancey_relationship -= 2
                    sabra "I just — I need time."
                    "He nodded. The press stood between them like a wall of iron type."

        "Say nothing. She had known what she married.":
            $ yancey_relationship += 5
            $ sabra_independence  += 2
            "Her mother had warned her. Her own heart had warned her. She had chosen anyway."
            "She went to the composing table and began resetting a column of type."
            yancey "Sabra."
            sabra "There's a front page to set."
            "He watched her a moment. Something in his face shifted — not quite relief. Something quieter."

        "Make a small joke of it — ease the tension.":
            $ yancey_relationship += 3
            $ sabra_direction     += 1
            sabra "Well. I suppose I married the most dangerous man at the dinner table."
            yancey "You always did have taste."
            "He laughed — a real one. The room breathed again."
            sabra "Pete Pitchlyn has a nerve, coming into my husband's newspaper to do arithmetic."

    hide pete
    hide sabra
    hide yancey

    $ journal_scene9 = True
    call journal_entry("SCENE 9", "Pete Pitchlyn came and went like weather. He said seven. Yancey neither confirmed nor denied it in any way I could call honest. I have set type beside this man every day for a year. I have slept beside him. I am still learning what he is. I think he is learning it too.") from _call_journal_scene9

    jump scene10_wigwam_lives


## ─── SCENE 10 — The Wigwam Lives ─────────────────────────────────────────────

label scene10_wigwam_lives:

    scene bg_wigwam_office with dissolve
    play music "audio/wigwam_press.ogg" fadein 1.5 loop

    "1891. The Oklahoma Wigwam had subscribers in four counties and a reputation that made certain men uncomfortable."

    "Yancey had been writing editorials on the Osage Indian land question — arguing that speculators were using legal instruments to strip the Nations of territory guaranteed by treaty."

    show yancey neutral at left with dissolve
    show yancey passionate

    yancey "If the law is used as a weapon against the people it was written to protect, then the law is not justice. It is theater."

    "The editorial had run. The reaction had been immediate."

    hide yancey

    show sabra ch2 neutral at right with dissolve

    "Three of the town's respectable citizens came to the Wigwam while Yancey was out. They wanted to speak to Sabra."

    "Citizen: Mrs. Cravat. We admire your husband. We admire the Wigwam. But this business about the Indians — it is making enemies where we don't need enemies."

    "Citizen: The territorial legislature. The land office. Men whose goodwill matters to Osage."

    menu:
        "Sabra's response to the pressure:"

        "Defend Yancey — the paper prints what it believes.":
            $ yancey_relationship += 5
            $ community_standing  -= 2
            show sabra determined
            sabra "The Wigwam has always printed what is true and what is right. My husband is not in the habit of adjusting his convictions to suit his advertisers."
            "The men exchanged glances. They left, not entirely empty-handed — they had learned something about Sabra Cravat."

        "Promise to 'speak to him' — buy peace she does not intend to deliver.":
            $ yancey_relationship -= 3
            $ community_standing  += 2
            sabra "I will speak with him. I understand your concerns."
            "She watched them go. She would not speak to him. But she had bought time — and perhaps goodwill."
            sabra "I have told a polite lie to unpleasant men. Mamma would be proud."

        "Give them a composed non-answer — the paper speaks for itself.":
            $ yancey_relationship += 3
            $ community_standing  += 1
            sabra "The Oklahoma Wigwam speaks for itself. I am certain you understand that."
            "The men could not quite argue with this. They withdrew, mildly outmaneuvered."

    ## Arita Red Feather arrives
    show arita neutral at center with dissolve

    "That evening, a Cherokee woman came to the back door of the Wigwam. She introduced herself as Arita Red Feather."

    arita "You are Mrs. Cravat. I have read your husband's editorials."

    sabra "He will be pleased to hear it."

    arita "I have documents. Letters from the land office. They show what he has been arguing — but with names, and dates, and signatures."

    "She set a cloth packet on the composing table."

    arita "I do not know if I can trust you. But I know I cannot trust the men at the land office, and I cannot trust most of the men in this town."

    arita "Can I trust you?"

    menu:
        "Sabra's answer to Arita:"

        "Accept the documents and promise secrecy.":
            $ indian_sympathy    += 3
            $ sabra_independence += 2
            show sabra determined
            sabra "Yes. You can trust me."
            "She held the woman's gaze long enough to mean it."
            "Arita left the documents and left without another word."
            "Sabra locked them in the cashbox until Yancey came home."

        "Politely decline — this is Yancey's affair.":
            $ indian_sympathy -= 2
            sabra "These would be better in my husband's hands. I am only the typesetter."
            "She heard herself say it. She did not quite like the sound of it."
            arita "Then perhaps your husband's hands are the only ones that matter here."
            "She left the documents on the counter anyway, and walked out."

        "Advise Arita to come back when Yancey is in.":
            $ indian_sympathy += 1
            sabra "Mr. Cravat is the one who writes the editorials. He should be the one to receive these."
            "Arita considered her."
            arita "You will tell him I came?"
            sabra "I will tell him exactly."
            "It was the honest answer. It was also the cautious one."

    hide arita
    hide sabra

    $ journal_scene10 = True
    call journal_entry("SCENE 10", "The paper is larger than it was. Yancey writes about the Indians and the town does not thank him for it. I begin to understand that being respected and being right are different things entirely. A Cherokee woman came today and looked at me as though she were deciding something. I am still not sure what she decided.") from _call_journal_scene10

    jump scene11_wind_donna


## ─── SCENE 11 — The Wind and Donna ───────────────────────────────────────────

label scene11_wind_donna:

    scene bg_cravat_home with dissolve
    play music "audio/wigwam_press.ogg" fadein 1.5 loop

    "1892. The Cravat home — a proper frame house now, with glass windows and a cookstove."

    "Yancey had gone to cover a territorial story in Guthrie. He had been gone three days."

    show sabra ch2 neutral at center with dissolve
    show isaiah child neutral at left with dissolve

    "Isaiah appeared in the doorway. He saw the look on her face and said nothing — just went for his coat."

    isaiah "I'll fetch Doc Valliant, Miss Sabra."

    "She started to say no. That was Wichita talking — the house with the good drapes and the expectation that these things were managed properly, with the right people in the right rooms."

    menu:
        "Sabra's decision in this moment:"

        "\"Go. But do not send for Yancey. I am enough.\"":
            $ sabra_independence += 3
            $ sabra_direction    += 2
            $ sabra_stood_alone   = True
            show sabra determined
            sabra "Get the doctor, Isaiah. Don't send for Yancey. We'll manage."
            "The boy ran. Sabra sat down slowly and breathed."
            sabra "We will manage."

        "\"Go — and ride for Yancey as well.\"":
            $ sabra_independence -= 1
            isaiah "Yes ma'am."
            "He went for both. She did not know why she had said it. Yancey would not arrive in time regardless."
            "Something in her still wanted him to know."

        "\"He'll come when he can. That's Yancey.\"":
            $ yancey_relationship += 2
            $ sabra_direction     += 1
            sabra "Fetch Doc Valliant. Yancey's covering the session — he'll come back when he's able."
            "She said it with the flat acceptance she had been building like a wall, one brick at a time, these three years in the territory."

    hide isaiah

    show doc neutral at left with dissolve

    "Doc Valliant arrived. He moved with the efficient calm of a man who had delivered children in dugouts, in wagon beds, in circumstances considerably worse than a frame house on the Oklahoma prairie."

    doc "You're doing fine, Mrs. Cravat. Better than fine."

    "When it was over, he held the child up and the child announced herself to the room."

    doc "A girl. Strong one."

    show doc warm with dissolve
    "He set the baby in Sabra's arms. The baby had dark hair and seemed to be frowning at a private problem."

    show sabra tender
    sabra "Hello. Hello, you."

    menu:
        "What name came to Sabra?"

        "Donna. For the land.":
            $ sabra_direction += 2
            sabra "Donna. Her name is Donna."
            doc "After the territory?"
            sabra "After nobody. After herself."

        "Felice — for her mother.":
            $ sabra_direction -= 2
            sabra "Felice. For my mother."
            doc "She'll have to grow into it."
            "Sabra looked at the child. It was an olive branch. It was also an admission."

        "Yancey — if she'll have it. Donna Yancey Cravat.":
            $ yancey_relationship += 3
            sabra "Donna. Donna Yancey Cravat, if she'll have the middle name."
            doc "She'll do as she pleases, that one."
            "Sabra thought he might be right."

    hide doc
    hide sabra

    $ journal_scene11 = True
    call journal_entry("SCENE 11", "Donna was born on a Tuesday. Yancey was in Guthrie. Isaiah ran for Doc Valliant and then stood outside the door for four hours because he did not know what else to do. Donna has her father's frown. I am already afraid of what she will want.") from _call_journal_scene11

    jump scene12_respectability


## ─── SCENE 12 — Respectability ───────────────────────────────────────────────

label scene12_respectability:

    scene bg_osage_parlor with dissolve
    play music "audio/osage_sunday.ogg" fadein 1.5 loop

    "1892. Osage had a bank, a school, three churches, and the beginnings of a civic conscience."

    "The Osage Women's Improvement Club was being founded. The founding members had agreed: Sabra Cravat should be president. She had the newspaper, the reputation, and what one woman called 'the kind of spine this town needs in a parlor.'"

    show sabra ch2 neutral at center with dissolve

    "The organizational meeting was in Estelle Sipes's front room. Twelve women. Good dresses. The particular energy of women who have decided to improve something."

    "The agenda moved smoothly until it reached the question of membership."

    "Estelle Sipes: We must establish, from the beginning, who belongs. A club is only as respectable as its members."

    "She did not say Dixie Lee's name. She didn't have to."

    menu:
        "On the question of Dixie Lee's membership:"

        "Insist she be considered — membership is for any woman of Osage.":
            $ community_standing -= 2
            $ sabra_independence += 2
            $ sabra_direction    += 2
            show sabra determined
            sabra "Dixie Lee has lived in this town as long as any of us. If we are building a club for the women of Osage, we build it for all of them."
            "Estelle Sipes drew herself up. Several others exchanged glances."
            "They did not vote Dixie in. But they did not vote her out in front of Sabra Cravat, either."

        "Agree to the exclusion — it is not the hill to die on today.":
            $ community_standing -= 2
            $ sabra_direction    -= 2
            "She said nothing. The motion passed."
            sabra "I will not think about this too hard."
            "But she did. Later. In the dark."

        "Abstain — decline to vote either way.":
            $ sabra_direction -= 1
            "She folded her hands in her lap and looked at the window."
            sabra "I abstain."
            "Estelle Sipes noted it in the minutes with a disapproving flourish."

    ## Second question: Arita Red Feather
    "Then Estelle Sipes raised the second name. Arita Red Feather."

    "Estelle Sipes: The Cherokee woman. She is not — she is not of our kind, Mrs. Cravat. You must see that."

    menu:
        "On Arita Red Feather:"

        "\"Arita Red Feather is a finer woman than any of us. She stays.\"":
            $ indian_sympathy      += 3
            $ community_standing   -= 3
            $ sabra_defended_indians = True
            show sabra determined
            sabra "Arita Red Feather is educated, principled, and a landowner of this territory. She is precisely our kind, Mrs. Sipes. She stays."
            "The room was very quiet."
            "Three women left before the meeting adjourned. Two wrote letters to Sabra the following week — thanking her, privately, for saying it."

        "Agree with the exclusion. It is different.":
            $ indian_sympathy    -= 3
            $ community_standing += 2
            "She told herself it was pragmatism. The club could do more good if it held together."
            "She did not tell Arita. She did not know how she would explain it."

        "Propose an Indian women's auxiliary — separate but adjacent.":
            $ indian_sympathy    -= 1
            $ community_standing += 1
            sabra "Perhaps a separate auxiliary — affiliated with the club, for the Native women of the region."
            "It was a compromise. It pleased no one entirely. That was, she supposed, what compromise was."

    hide sabra

    $ journal_scene12 = True
    call journal_entry("SCENE 12", "We have a Women's Club. I am its president. I do not know whether to be proud of this or suspicious of it. The question of who belongs to this town is not settled by a meeting in Estelle Sipes's parlor. I am beginning to think it is not settled at all.") from _call_journal_scene12

    jump scene13_cherokee_strip


## ─── SCENE 13 — The Cherokee Strip ───────────────────────────────────────────

label scene13_cherokee_strip:

    scene bg_wigwam_office with dissolve
    play music "audio/cherokee_strip.ogg" fadein 1.5 loop

    "September 1893."

    "The Cherokee Outlet — eight million acres of prime grassland — was being opened to settlers. Another land run. The last great one."

    "Sabra knew before Yancey spoke. She had seen his hands at the type case, moving faster. His eyes somewhere further west than the pressroom."

    show yancey neutral at left with dissolve
    show yancey restless
    show sabra ch2 neutral at right with dissolve

    yancey "I have to cover it, Sabra. It's the last run. The end of the Territory as a territory."

    sabra "You want to ride in it."

    yancey "I want to cover it. There's a difference."

    sabra "Is there?"

    "He had the grace to be quiet."

    menu:
        "Sabra's response to his announcement:"

        "\"Take me with you.\"":
            $ yancey_relationship += 5
            $ sabra_direction     += 3
            $ sabra_independence  += 2
            sabra "Take me. Cim and Donna can stay with Isaiah. But take me."
            yancey "Sabra —"
            sabra "I have ridden across this territory once already. I can do it again."
            "He looked at her for a long moment. Something in him shifted — something like admiration, and something like relief."
            yancey "All right. All right, then."

        "\"Go. I'll keep the Wigwam running.\"":
            $ yancey_relationship += 3
            $ sabra_independence  += 3
            $ sabra_direction     += 2
            show sabra determined
            sabra "Go. I can run the paper without you for a week. I've done it before."
            yancey "Sabra —"
            show sabra tender
            sabra "The Wigwam will be here when you get back. So will I."
            "He crossed the room and held her face in both hands."
            show yancey tender
            yancey "You are remarkable."
            "She let herself believe it, just for a moment."

        "\"Will you come back?\"":
            $ yancey_relationship -= 2
            $ yancey_mystery       = True
            sabra "Will you come back?"
            "He did not answer immediately. That was its own answer."
            yancey "Sabra. Of course I will come back."
            "She looked at him. At the man who had walked into a room full of settlers with a Prince Albert coat and a speech about destiny."
            sabra "Of course."

        "\"You promised you would stay.\"":
            $ yancey_relationship -= 5
            $ sabra_direction     -= 2
            sabra "You said you were done with runs. You said Osage was enough."
            yancey "Sabra —"
            sabra "You said."
            "He left before dawn, anyway."

    "He left before dawn — with two horses, a bedroll, and a notebook."

    "The pressroom was very quiet."

    show sabra ch2 neutral at center with dissolve
    show sabra weary
    hide yancey

    menu:
        "As she watched him go:"

        "She felt the familiar pride alongside the fear.":
            $ yancey_relationship += 3
            $ sabra_admires_yancey = True
            "It never changed. The sight of him riding — the size of him against the sky — still caught in her chest."
            sabra "Impossible man."
            "She said it the way you say a thing you have made your peace with."

        "She turned back to the press. There was work.":
            $ sabra_independence += 3
            $ sabra_direction    += 2
            "She did not stand at the window long. There was a front page to set."
            "The lever on the press had always felt solid in her hands. More solid, lately, than almost anything else in Osage."

        "She allowed herself to cry, alone, just once.":
            $ sabra_direction    -= 1
            $ yancey_relationship -= 1
            "She had taught herself not to cry where the children could see."
            "She sat in the empty pressroom and let herself grieve something she could not name."
            "Then she set the front page."

    "Days passed. Then a week."

    "Then word came back — a letter, in his sprawling hand, postmarked Enid."

    yancey "I am well. The run was everything. I'll write the piece when I stop moving."

    "He did not say when he would stop moving."

    "Sabra set the next edition without him. Then the one after that."

    "The Oklahoma Wigwam did not miss a week."

    hide sabra

    $ journal_scene13 = True
    call journal_entry("SCENE 13", "He went for the Cherokee Strip. I knew he would. I think I have always known that there is a part of Yancey Cravat that cannot be held by any one place, any one person. I have decided not to need him to be otherwise. The Wigwam ran its edition. The children ate their supper. I am learning what it means to be a woman who manages.") from _call_journal_scene13

    scene black with dissolve

    "— End of Chapter Two —"

    call chapter2_summary from _call_chapter2_summary

    return


## ─── CHAPTER 2 SUMMARY ───────────────────────────────────────────────────────

label chapter2_summary:

    scene black

    "CHAPTER TWO COMPLETE"
    " "
    "— Your Story So Far —"
    " "

    ## Yancey relationship
    if yancey_relationship >= 65:
        "YANCEY & SABRA: Deeply trusting. Even his absences feel like a conversation."
    elif yancey_relationship >= 35:
        "YANCEY & SABRA: Balanced — warm and real, with distances neither has crossed."
    else:
        "YANCEY & SABRA: Strained. She has begun to make a life that does not depend on him."

    " "

    ## Sabra's direction
    if sabra_direction >= 5:
        "SABRA'S PATH: Frontier Woman. She is someone her mother would not recognize, and she is glad."
    elif sabra_direction <= -5:
        "SABRA'S PATH: Refined Lady. She keeps Wichita's standards like a lamp against the dark."
    else:
        "SABRA'S PATH: Between Two Worlds. She has not yet chosen — or the choice is choosing itself."

    " "

    ## Community standing
    if community_standing >= 4:
        "STANDING IN OSAGE: Well-regarded. The town knows her name and means it kindly."
    elif community_standing <= -2:
        "STANDING IN OSAGE: Complicated. She has made enemies by being right."
    else:
        "STANDING IN OSAGE: Respectable. Neither beloved nor resented — yet."

    " "

    ## Indian sympathy
    if indian_sympathy >= 4:
        "ON THE INDIAN QUESTION: Advocate. She has put herself on the side of the treaties and the Nations."
    elif indian_sympathy <= -3:
        "ON THE INDIAN QUESTION: Prejudiced. She has accommodated the prejudices of the town."
    else:
        "ON THE INDIAN QUESTION: Cautious. She has not yet decided what she believes — or acted on it."

    " "

    ## Achievement flags
    if sabra_stood_alone:
        "She brought Donna into the world without sending for Yancey. She did not need to."
    if sabra_defended_indians:
        "In a parlor full of respectable women, she said Arita Red Feather's name out loud and meant it."
    if yancey_mystery:
        "She has glimpsed the part of Yancey that he does not explain. She is learning to live alongside it."
    if sabra_admires_yancey:
        "She still watches him ride away and feels the catch in her chest. She has stopped fighting it."

    " "

    jump chapter3_start
