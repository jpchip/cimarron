## script_chapter3.rpy
## Cimarron: Chapter Three — Yancey Leaves; Sabra Rises
## Based on Cimarron by Edna Ferber (1929), public domain.
##
## Scene structure:
##   scene14_five_years     → Five-year absence; Sabra holds Osage together
##   scene15_the_kid        → Yancey returns; aftermath of the Kid
##   scene16_running_paper  → Sabra as editor; letters minigame
##   scene17_isaiah         → Isaiah reads type; defended against advertiser
##   scene18_war            → Yancey enlists for Spanish-American War; departs

## ─── Entry Point ──────────────────────────────────────────────────────────────

label chapter3_start:
    $ renpy.block_rollback()

    scene black with fade

    "CIMARRON"
    "{i}Based on the novel by Edna Ferber{/i}"
    "Chapter Three: Yancey Leaves; Sabra Rises"
    " "
    "{i}Osage, Oklahoma Territory. 1893–1898.{/i}"

    play music "audio/five_years.ogg" fadein 1.5 loop

    jump scene14_five_years


## ─── SCENE 14 — Five Years ────────────────────────────────────────────────────

label scene14_five_years:

    scene bg_wigwam_office_daytime with dissolve

    "He did not come back from the Cherokee Strip."

    "Not that week. Not that month. A letter came from Tulsa — then one from Tahlequah — then silence."

    "Sabra Cravat ran the Oklahoma Wigwam."

    show sabra ch3 neutral at center with dissolve

    "She set the type. She wrote the editorials. She paid Sol Levy for the newsprint and argued with the territorial mail office about distribution rates."

    "She did not tell the children their father was gone. She told them he was covering the territory. He was always covering the territory."

    "She believed it, on good days."

    show sabra ch3 sad

    ## ── How Sabra Held On ─────────────────────────────────────────────────────

    menu:
        "In the five years without him, Sabra found her footing:"

        "Through the work — the Wigwam became her anchor.":
            $ sabra_independence += 3
            $ sabra_direction    += 2
            $ newspaper_stance   += 1
            sabra "{i}The press is loud enough to fill a room. That is useful.{/i}"
            "She learned to love the smell of ink the way you learn to love a difficult country — by living in it long enough."
            "The Wigwam did not miss a single edition. Five years. Not one."

        "Through the children — for Cim and Donna she kept going.":
            $ sabra_independence += 2
            $ sabra_direction    -= 1
            sabra "{i}They need me to be steady. So I am steady.{/i}"
            "She told Cim stories about his father. The good ones."
            "Donna was too young for stories. She needed supper on the table and a mother who did not cry."

        "Through the community — Osage needed her, and she let it.":
            $ sabra_independence += 2
            $ community_standing += 3
            sabra "{i}The town has work for me. That is not nothing.{/i}"
            "The Women's Club. The school board. The Indian affairs committee she'd started with Arita Red Feather."
            "Osage grew around her while she was not looking."

        "With difficulty — there were nights she nearly quit.":
            $ yancey_relationship -= 3
            $ yancey_mystery       = True
            sabra "{i}I will not tell anyone how many times I sat at that press and could not move.{/i}"
            "She had nearly sold the Wigwam twice. Both times she had been stopped by something she could not name."
            "Pride, perhaps. Or the knowledge that she had nowhere else to be."

    ## ── Interlude narration ───────────────────────────────────────────────────

    "The children grew. Cim was serious and tall, with his father's eyes and his grandfather Venable's quiet manner."

    "Donna was loud and opinionated and had a talent for arithmetic that no one in the family could account for."

    show isaiah neutral at left with dissolve

    "Isaiah had grown, too. He ran errands, set type, and had — without anyone quite deciding it — become the Wigwam's assistant press operator."

    isaiah "Miss Sabra. You got two errors on page three, left column."

    sabra "I see them, Isaiah. I see them."

    isaiah "Just saying."

    "She let him say."

    hide isaiah
    hide sabra

    $ journal_scene14 = True
    call journal_entry("SCENE 14", "Five years. I have not written it plainly before: five years without Yancey Cravat. Letters, occasionally. The sense that he is alive, somewhere, because the alternative is a thing I will not consider. I have run his newspaper. I have raised his children. I have made something in this town that will not disappear when he comes back — if he comes back. I am no longer certain which I would prefer.") from _call_journal_scene14

    jump scene15_the_kid


## ─── SCENE 15 — The Kid ───────────────────────────────────────────────────────

label scene15_the_kid:

    scene bg_osage_street_1895 with dissolve
    play music "audio/kid_return.ogg" fadein 1.5 loop

    "He came back in October."

    "Not quietly. Yancey Cravat never did anything quietly."

    "Word ran ahead of him: he'd shot a man in Enid. A young gunman named the Kid — barely twenty, they said, and mean with it — who had tracked Yancey for eighteen months over a slight that predated Osage."

    "Yancey had walked the main street of Enid, alone, at noon, and the Kid had come at him from the hardware-store doorway."

    "The Kid was in the ground. Yancey was riding home."

    show sabra ch3 neutral at right with dissolve

    "Sabra was at the Wigwam composing table when she heard the horse."

    "She knew the sound."

    ## ── Choice 1: Seeing him ──────────────────────────────────────────────────

    menu:
        "When Yancey walked through the door:"

        "She went to him immediately.":
            $ yancey_relationship += 5
            show sabra ch3 happy
            "She did not think. She crossed the floor and put her arms around him."
            sabra "You're here."
            yancey "I'm here."
            "He held her longer than she expected. His coat smelled of the road."

        "She stayed at the press. Let him come to her.":
            $ sabra_independence  += 3
            $ sabra_direction     += 2
            $ sabra_cleared_the_office = True
            "She did not look up. She set the next line of type."
            "He stood in the doorway. She heard the creak of his boots."
            sabra "You'll need to wash before I show you what you missed."
            "He laughed — sudden, genuine. She kept setting type."
            yancey "Lord, Sabra."
            sabra "Five years, Yancey."

        "She felt rage, then relief, then nothing she could name.":
            $ yancey_relationship -= 2
            $ yancey_mystery       = True
            "She stood very still and let the feelings move through her like weather."
            sabra "I don't know what to say to you."
            yancey "Then don't say anything."
            "He crossed the room and sat heavily in the editor's chair — her chair, she noticed — and said nothing."
            "She made coffee. It was something to do."

    show yancey neutral at left with dissolve
    show yancey weary

    "He was thinner. There were lines around his eyes she had not seen before."

    yancey "I hear the Wigwam has not missed an edition."

    sabra "Not one."

    yancey "I knew it wouldn't."

    sabra "Did you."

    ## ── Choice 2: The reward money ────────────────────────────────────────────

    "There was a reward. The territorial government had put two hundred dollars on the Kid for a string of robberies. It was Yancey's by right."

    menu:
        "What Sabra said about the reward money:"

        "\"Put it in the paper's account. We have debts.\"":
            $ sabra_independence += 2
            $ newspaper_stance   += 1
            sabra "There's a reward from the territory. Two hundred dollars. Put it toward the press costs."
            yancey "Practical."
            sabra "Someone has to be."
            "He looked at her steadily. Something in his expression shifted — respect, perhaps, and something more complicated."

        "\"Give some to the Kid's family, if he had one.\"":
            $ yancey_relationship += 3
            $ indian_sympathy     += 1
            sabra "Did the Kid have family?"
            yancey "Mother in Kansas. Young."
            show sabra ch3 tender
            sabra "Send her something. Not all of it, but something."
            "He was quiet a moment."
            show yancey tender
            yancey "You are a better person than I am, Sabra Cravat."

        "Say nothing. The money was his affair.":
            $ sabra_independence += 1
            "She let it alone. He would do with it as he chose."
            "He always did."

    "He stayed three weeks. It was not like the old days — it was something else, harder and quieter and more honest."

    "Then he began to itch."

    show yancey restless
    "She saw it in the way he stood at the door in the evenings, looking west."

    hide yancey

    ## ── Journal beat ─────────────────────────────────────────────────────────

    scene bg_hefner_window with dissolve
    show kid dead at center with dissolve

    "She saw it and she did not pretend otherwise."

    sabra "There will be a next time. Won't there."

    "It was not a question."

    hide kid
    hide sabra

    $ journal_scene15 = True
    call journal_entry("SCENE 15", "He came back. I did not know until the moment I heard his horse whether I would be glad or furious. I was both. He killed the Kid — a young man I never met, whose name I do not know — and rode home like it was weather. He is here. He is himself. And I can already see the door calling him.") from _call_journal_scene15

    jump scene16_running_paper


## ─── SCENE 16 — Running the Paper ────────────────────────────────────────────

label scene16_running_paper:

    scene bg_wigwam_office_daytime with dissolve
    play music "audio/five_years.ogg" fadein 1.5 loop

    "1895. Yancey was gone again — covering the new oil surveys in the hills east of Osage."

    "He had been gone six months."

    "Sabra was the editor of the Oklahoma Wigwam. Not in the way she had been during his absences — that was management by necessity. This was something else."

    show sabra ch3 neutral at center with dissolve

    sabra "I am writing my own editorial this week."

    "It was a Thursday. She had a front page to fill, a letters column to edit, and a decision to make."

    ## ── Choice 1: The editorial ────────────────────────────────────────────────

    menu:
        "The week's editorial concerned the territorial legislature's vote on Indian allotment:"

        "Write it sharp — defend the Indian Nations openly.":
            $ newspaper_stance += 3
            $ indian_sympathy  += 2
            $ community_standing -= 1
            sabra "I have the documents. I have Arita's testimony. I am going to print it."
            "She sat down and wrote for three hours."
            "The editorial named three legislators by name and called their allotment votes 'a quiet robbery conducted in the language of law.'"
            sabra "{i}Yancey will either love this or never forgive me for printing it without him.{/i}"
            "She sent it to press."

            menu:
                "The reaction from the Osage business community:"

                "Let them cancel their ads. The story is the story.":
                    $ newspaper_stance   += 2
                    $ community_standing -= 2
                    sabra "If they pull their advertisements because I told the truth, then the Wigwam does not need their advertisements."
                    "Four advertisers pulled. Two wrote letters of support. One subscriber sent flowers."

                "Soften the names — keep the argument, spare the men.":
                    $ newspaper_stance   += 1
                    $ community_standing += 1
                    sabra "I can make the argument without making enemies of the men who print our notices."
                    "She revised. The piece was strong. It was also survivable."

        "Write measured — make the argument without naming names.":
            $ newspaper_stance += 1
            $ indian_sympathy  += 1
            sabra "I can make the same case without turning the town against us."
            "She wrote carefully. Each sentence tested before it was set."
            "The piece was quieter than the documents deserved — but it ran. And it was read."

        "Write a general civic piece — keep the Wigwam neutral.":
            $ newspaper_stance   -= 1
            $ community_standing += 2
            sabra "The Wigwam is not a weapon. It is a newspaper."
            "She wrote about water rights and the school bond instead."
            "The advertisers were pleased. She was not sure she was."

    ## ── Choice 2: The Indian question in letters ─────────────────────────────

    "The letters that week ran thick. Statehood talk, oil rumors, the usual civic complaints."

    "And then: the Indian question. Everyone had an opinion."

    menu:
        "Sabra's policy for letters on Indian affairs:"

        "Print the argument from both sides, let readers decide.":
            $ newspaper_stance += 1
            $ community_standing += 1
            sabra "A paper that only prints what it agrees with is a pamphlet."
            "She selected letters from each side. She wrote a brief editor's note: 'The Wigwam prints both.'"

        "Favor letters that agree with the paper's editorial line.":
            $ newspaper_stance += 2
            sabra "The Wigwam has a position. The letters should support the argument."
            "She selected accordingly. The column was more coherent. Also more one-sided."

        "Print whatever arrived. Make no selection.":
            $ newspaper_stance -= 1
            sabra "I haven't time to curate. Print what came."
            "The letters ran without comment. The results were mixed."

    ## ── Letters minigame ──────────────────────────────────────────────────────

    "That week's mailbag was heavier than usual. Eight letters, all demanding space."

    sabra "I have room for four. Something will have to go."

    "She spread them across the composing table and read."

    $ letters_printed = []
    $ letters_spiked  = []
    call screen letters_minigame
    $ letters_printed = _return

    jump scene16_letters_result


label scene16_letters_result:

    ## Outcome: count by tag
    $ pro_indian_count  = sum(1 for lid in letters_printed if get_letter(lid) and get_letter(lid)["tag"] == "pro-indian")
    $ anti_indian_count = sum(1 for lid in letters_printed if get_letter(lid) and get_letter(lid)["tag"] == "anti-indian")
    $ gossip_count      = sum(1 for lid in letters_printed if get_letter(lid) and get_letter(lid)["tag"] == "gossip")
    $ oil_count         = sum(1 for lid in letters_printed if get_letter(lid) and get_letter(lid)["tag"] == "oil")
    $ yancey_count      = sum(1 for lid in letters_printed if get_letter(lid) and get_letter(lid)["tag"] == "yancey")

    ## Apply variable changes based on letters printed
    $ newspaper_stance   += pro_indian_count * 2
    $ newspaper_stance   -= anti_indian_count * 2
    $ indian_sympathy    += pro_indian_count
    $ indian_sympathy    -= anti_indian_count
    $ community_standing -= gossip_count * 2
    $ yancey_relationship += yancey_count

    ## Narrative reaction
    if pro_indian_count >= 2:
        "The letters column ran heavily in favor of the Nations. Arita Red Feather sent a note: 'Thank you for the space.'"
        sabra "It is only fair."
    elif anti_indian_count >= 2:
        "The letters column ran against the land-grant advocates. Several of Osage's more conservative citizens approved."
        "Sabra was not sure whether to be glad or troubled."
    elif gossip_count >= 1:
        "She had printed the anonymous letter about Dixie Lee."
        sabra "{i}I should not have done that.{/i}"
        "She knew it before the ink was dry."
        $ community_standing -= 1
    elif oil_count >= 1:
        "The oil company letter ran. It looked like news. It was advertising."
        sabra "{i}Yancey would have spiked it.{/i}"
        $ newspaper_stance -= 1

    if 8 in letters_printed:
        "The letter from the unnamed settler — the one grateful for law after the Kid — ran in the lower left column."
        "Three people stopped Sabra on the street that week to say they'd read it."
        sabra "That is what the Wigwam is for."

    hide sabra

    $ journal_scene16 = True
    call journal_entry("SCENE 16", "I chose four letters. I will not pretend the choice was neutral. Everything I print is a choice. I understand that now in a way I did not when I was only setting Yancey's type. This is my paper too. I am learning what I think it should say.") from _call_journal_scene16

    jump scene17_isaiah


## ─── SCENE 17 — Isaiah ────────────────────────────────────────────────────────

label scene17_isaiah:

    scene bg_wigwam_office_daytime with dissolve
    play music "audio/five_years.ogg" fadein 1.5 loop

    "1896."

    "Isaiah was fifteen. He had been with the Cravats since the first run — since before Donna was born, before the Wigwam had a proper building, before Sabra had learned to work the press."

    show isaiah neutral at left with dissolve
    show sabra ch3 neutral at right with dissolve

    "He was reading."

    "Not the type he was setting — he knew the type. He was reading the editorial she'd written, silently, running his finger along the lines."

    sabra "You read well."

    "He looked up. A little startled."

    isaiah "My mama taught me before she — before I came here."

    sabra "I know."

    "She had not known. She realized, with a small shame, that she had never asked."

    ## ── Choice 1: His reading ─────────────────────────────────────────────────

    menu:
        "Sabra's response to discovering Isaiah's literacy:"

        "\"You should be writing, not just setting type.\"":
            $ sabra_independence += 2
            $ community_standing += 1
            sabra "Isaiah. Have you ever written anything? For yourself, I mean. Not copy."
            isaiah "I write things down. Not for printing."
            sabra "Bring them. Next week. I want to read them."
            "He looked at her steadily for a moment."
            isaiah "Yes, ma'am."
            "She heard in those two words everything that was complicated about the situation. She did not look away."

        "Let the moment pass — do not make it more than it is.":
            $ sabra_direction -= 1
            "She returned to her work. So did he."
            "But something had shifted, quietly, in the room."

        "\"I should have asked you to help with the writing long ago.\"":
            $ sabra_independence += 1
            $ isaiah_defended     = True
            sabra "I have been wasting a perfectly good mind on the press crank."
            isaiah "The press crank needs someone."
            sabra "It does. But so does the copy desk."
            "He did not smile exactly. But something in his face opened."

    ## ── The advertiser confrontation ─────────────────────────────────────────

    "Three days later, the trouble came."

    "Horace Greeley Tubbs — no relation, despite the name — was the Wigwam's largest advertiser. He ran three hardware notices a month."

    "He came in on a Wednesday afternoon, hat in hand, with the specific politeness of a man who intends to be impolite."

    "Horace Tubbs: Mrs. Cravat. I want that boy off the street when my customers are coming in."

    sabra "I beg your pardon?"

    "Horace Tubbs: The colored boy. I have customers who don't care to — they find it — it is a preference, Mrs. Cravat. A business preference."

    ## ── Choice 2: Defense ────────────────────────────────────────────────────

    menu:
        "Sabra's response:"

        "\"Isaiah stays. You may take your notices elsewhere.\"":
            $ isaiah_defended    = True
            $ community_standing -= 2
            $ newspaper_stance   += 1
            show sabra ch3 angry
            sabra "Isaiah has worked for this paper since we opened. He goes where he is needed and does his job. I suggest you do the same, Mr. Tubbs."
            "Horace Tubbs went red."
            "Horace Tubbs: I'll pull my notices."
            sabra "I know the way to the door."
            "He left. She sat down and shook."
            "Isaiah was at the press. He had heard everything. He did not look up."
            "She did not ask him to."

        "Offer a compromise — different hours, different street entrance.":
            $ community_standing += 1
            sabra "Isaiah uses the back entrance in the mornings when your deliveries come. I'll ask him to keep to that."
            "It was a compromise. It felt like a defeat."
            "She told herself she was being practical. She did not fully believe it."

        "Buy time — tell Tubbs she'll 'look into it'.":
            "She told Tubbs she would look into it."
            "She did not look into it. Isaiah kept working."
            "Tubbs kept his notices. She kept her discomfort."

    "Some months later, Isaiah was struck by a runaway wagon on the main street of Osage."

    "He lingered three days. He died on a Sunday."

    "He was seventeen."

    hide isaiah

    show sabra ch3 weary
    sabra "He was learning to write."

    hide sabra

    $ journal_scene17 = True
    call journal_entry("SCENE 17", "Isaiah died. I have written those words and I cannot add to them. He was seventeen years old and he could read and he was learning to write and he is gone. I did not know his mother's name until I had to send her a letter. That is the kind of failure that does not leave you.") from _call_journal_scene17

    jump scene18_war


## ─── SCENE 18 — The War ───────────────────────────────────────────────────────

label scene18_war:

    scene bg_editorial_office_night with dissolve
    play music "audio/war_march.ogg" fadein 1.5 loop

    "1898."

    "Yancey had been back eight months — the longest stretch in Osage since the early days."

    "The Spanish-American War had broken out in April. The newspapers were full of it."

    "Sabra watched him read. She knew."

    show yancey neutral at left with dissolve
    show yancey passionate
    show sabra ch3 neutral at right with dissolve

    yancey "Roosevelt is raising a regiment. Rough Riders. Volunteers."

    sabra "I know."

    yancey "Cuba, Sabra. The last —"

    sabra "I know, Yancey."

    "She had said it twice. She would not say it a third time."

    ## ── Choice 1: Sabra's response ────────────────────────────────────────────

    menu:
        "Sabra's answer:"

        "\"Go. But know that I will not wait another five years.\"":
            $ yancey_relationship -= 3
            $ sabra_independence  += 3
            $ sabra_direction     += 3
            show sabra ch3 angry
            sabra "Go. You're going to go. But I am telling you plainly: I am not going to hold this paper and this family together for another five years on the chance that you come back."
            "He looked at her."
            yancey "What are you saying?"
            sabra "I am saying that I have made a life here. I am saying that when you come back — if you come back — you come back to my Osage, not yours."
            "He was quiet a long time."
            yancey "All right."

        "\"I have the paper. Go.\"":
            $ sabra_independence  += 2
            $ sabra_direction     += 2
            $ yancey_relationship += 2
            sabra "The Wigwam will be here. The children will be here. Go, Yancey."
            yancey "Sabra —"
            sabra "You'd be unbearable if you stayed."
            "He laughed, and the laugh broke something open between them that had been sealed a long time."

        "\"Don't go. For once. Stay.\"":
            $ yancey_relationship -= 5
            $ sabra_direction     -= 2
            show sabra ch3 tender
            sabra "Don't go, Yancey. I am asking you. Stay here."
            "He looked at her with genuine anguish."
            show yancey weary
            yancey "I can't."
            "She had known. It did not make it less true."

        "Say nothing. Go to the window.":
            $ sabra_independence  += 2
            $ yancey_mystery       = True
            "She turned to the window. The main street of Osage at night — gas lamps and the smell of horses and her whole life, laid out in front of her."
            "She did not turn back."

    ## ── Dixie Lee at the door ─────────────────────────────────────────────────

    "The evening before Yancey left, a knock came at the Wigwam door."

    "It was Dixie Lee."

    show dixie neutral at center with dissolve

    "She had aged — she had always been in the territory's teeth — but there was something steady in her now."

    "Dixie Lee: I heard he's going. I wanted — I wanted to say something."

    "She looked at Sabra."

    show dixie direct with dissolve
    "Dixie Lee: You're a good woman, Mrs. Cravat. I know you don't think I know that. But I do."

    ## ── Choice 2: Dixie Lee ───────────────────────────────────────────────────

    menu:
        "Sabra's response to Dixie Lee:"

        "\"Come in. We'll have coffee before he goes.\"":
            $ sabra_direction    += 2
            $ community_standing += 1
            sabra "Come in, Dixie. Sit down."
            "Dixie Lee looked startled. Then she came in."
            "They sat together for an hour — three of them around the composing table — talking about nothing in particular."
            "It was the most honest evening Sabra could remember."

        "A civil nod. No more.":
            $ sabra_direction -= 1
            "She nodded. She did not invite her in."
            "Dixie Lee seemed to have expected this. She nodded back and walked away."
            "Sabra did not know how to feel about that. She tried not to."

        "\"Thank you. That means something.\"":
            $ sabra_direction     += 1
            $ community_standing  += 1
            sabra "That means something, Dixie. Thank you."
            "She was surprised to find that she meant it."
            "Dixie Lee went, and Sabra stood in the doorway a moment longer than she needed to."

    hide dixie
    hide yancey

    "He left before dawn."

    show sabra ch3 neutral at center with dissolve
    show sabra ch3 determined

    "Sabra Cravat stood in the pressroom of the Oklahoma Wigwam and looked at the cases of type."

    "Her type, now. Her paper."

    "Donna's footsteps on the stairs above. The smell of ink and newsprint and the particular dust of Osage in summer."

    sabra "All right."

    "She crossed to the press and began."

    hide sabra

    scene black with dissolve

    "— End of Chapter Three —"

    call chapter3_summary from _call_chapter3_summary

    return


## ─── CHAPTER 3 SUMMARY ───────────────────────────────────────────────────────

label chapter3_summary:

    scene black

    "CHAPTER THREE COMPLETE"
    " "
    "— Your Story So Far —"
    " "

    ## Yancey relationship
    if yancey_relationship >= 65:
        "YANCEY & SABRA: Deeply trusting, even across the silences. She knows what he is. He knows what she has become."
    elif yancey_relationship >= 35:
        "YANCEY & SABRA: Balanced — real and complicated, with distances that have grown familiar."
    else:
        "YANCEY & SABRA: Strained. She has built something he cannot quite reach, and she is not sure she minds."

    " "

    ## Sabra's direction
    if sabra_direction >= 8:
        "SABRA'S PATH: Frontier Woman. The person who arrived in a silk dress from Wichita is a distant memory."
    elif sabra_direction <= -5:
        "SABRA'S PATH: Refined Lady. She has kept the old standards. They have kept her."
    else:
        "SABRA'S PATH: Her Own. Neither Wichita nor the frontier entirely owns her now."

    " "

    ## Newspaper stance
    if newspaper_stance >= 5:
        "THE WIGWAM: Progressive — advocate for the Indian Nations, women's voice, reform. It has made enemies. It has also made history."
    elif newspaper_stance <= -3:
        "THE WIGWAM: Conservative — careful, community-minded, advertiser-safe. It is trusted by the right people."
    else:
        "THE WIGWAM: Balanced — it prints what it believes, mostly. The rest, it is learning."

    " "

    ## Community standing
    if community_standing >= 6:
        "STANDING IN OSAGE: Beloved. The town would not be what it is without Sabra Cravat."
    elif community_standing <= -3:
        "STANDING IN OSAGE: Complicated. She has made the right enemies."
    else:
        "STANDING IN OSAGE: Respected. They know her name and mean it."

    " "

    ## Indian sympathy
    if indian_sympathy >= 5:
        "ON THE INDIAN QUESTION: Advocate — her name is known in the Nations as someone who could be trusted."
    elif indian_sympathy <= -3:
        "ON THE INDIAN QUESTION: Accommodating — she has bent with the town's prejudices more than she would like to admit."
    else:
        "ON THE INDIAN QUESTION: Cautious, but changing."

    " "

    ## Achievement flags
    if sabra_cleared_the_office:
        "When Yancey came home from the Kid, she was at the press. She did not stop for him. He had to come to her."
    if isaiah_defended:
        "She defended Isaiah against a man with money and she knew the cost and she did it anyway."
    if sabra_stood_alone:
        "She brought Donna into the world without sending for Yancey. She has not forgotten it."
    if sabra_defended_indians:
        "She said Arita Red Feather's name out loud in a parlor of respectable women and meant every word."
    if yancey_mystery:
        "She has seen the part of Yancey that cannot be explained. She has decided to live alongside it."
    if newspaper_stance >= 3:
        "The Wigwam she runs is not the paper Yancey founded. It is something more."

    " "
    "Chapter Four: Coming."
    " "

    jump chapter4_start


