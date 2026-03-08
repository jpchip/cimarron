## script_chapter4.rpy
## Cimarron: Chapter Four — War Hero, Statehood, Oil (1898–1907)
## Based on Cimarron by Edna Ferber (1929), public domain.
##
## Scene structure:
##   scene19_rough_rider     → Yancey returns from Cuba in Rough Rider uniform
##   scene20_dixie_trial     → Dixie Lee's trial; Yancey defends her; minigame
##   scene21_statehood       → The statehood question; Yancey's letter
##   scene22_first_oil       → The first oil derricks; Cim's future
##   scene23_what_yancey_left → Statehood Day 1907; Yancey absent; taking stock


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


## ─── SCENE 19 — The Rough Rider ───────────────────────────────────────────────

label scene19_rough_rider:

    scene bg_osage_street_1900 with dissolve

    "He came back from Cuba in September."

    "Word ran ahead of him on the telegraph wire: ROUGH RIDER CRAVAT RETURNING STOP WOUNDED STOP NOT SERIOUS STOP."

    "Osage turned out. Of course it did."

    show sabra neutral at right with dissolve

    "Sabra had been at the Wigwam composing table when the wire came. She read it twice, folded it, put it in her apron pocket, and went back to the type."

    "She had finished the page before she let herself feel anything."

    ## ── Choice 1: The Public Moment ─────────────────────────────────────────

    "The whole of Main Street was out when he rode in. The Rough Rider hat. The sun on the brass buttons. Eight — she counted — eight notches cut into the hat band."

    show yancey neutral at left with dissolve
    show yancey weary

    "Yancey Cravat, grinning at the crowd like a man who has never been afraid of anything in his life."

    menu:
        "Sabra's choice in the crowd:"

        "Stand beside him — let the town see them together.":
            $ yancey_relationship += 5
            $ community_standing  += 2
            "She stepped out of the doorway and walked toward him."
            "He saw her and the grin changed into something else — something quieter and more honest."
            yancey "Sabra."
            sabra "You're late."
            "He laughed. The crowd laughed with him. She let them."
            "She took his arm and they walked the street together and she held her head exactly as she had been taught and felt, underneath that, something enormous and complicated."

        "Step back — let him have his moment, his way.":
            $ sabra_independence += 1
            "She stayed in the doorway of the Wigwam."
            "He scanned the crowd for her. Found her. The grin softened."
            "She raised a hand, just barely. He understood."
            "She let the town have him for an hour."

        "Wave from the crowd — be a face in it, like anyone.":
            $ sabra_independence += 2
            $ sabra_direction    += 1
            "She was standing with Sol Levy and two women from the school board when he passed."
            "She waved like a neighbor."
            "He caught her eye and she saw him see it — that she was not performing, was not playing the hero's wife — and something flickered in his expression. Appreciation, she thought. Or recognition."

    ## ── Private reunion ─────────────────────────────────────────────────────

    scene bg_wigwam_office_daytime with dissolve

    "That evening, when the town had gone home and the children were in bed, they were alone in the pressroom."

    "He was thinner. There were new lines at the corners of his eyes. The hat sat on the composing table between them."

    sabra "Eight."

    yancey "Cuba moves fast."

    "She looked at him steadily."

    sabra "Are you all right."

    yancey "Mostly."

    "It was more than he usually said."

    ## ── Choice 2: The Private Reunion ───────────────────────────────────────

    menu:
        "Sabra's response:"

        "\"Tell me everything. I want to know.\"":
            $ yancey_relationship += 5
            show sabra tender
            sabra "Tell me everything. Not for the paper. For me."
            "He looked at her for a moment as if checking whether she meant it."
            "Then he told her."
            "She sat on the press stool and listened for two hours. The good parts and the terrible parts."
            "She did not interrupt."
            show yancey tender
            yancey "You're the only person I can tell it to."
            "She put her hand over his and said nothing."

        "\"I need to tell you what you missed. Five months of it.\"":
            $ sabra_independence += 2
            sabra "I have things to tell you too. The statehood movement. The school expansion. Isaiah's grave."
            "He listened. She talked."
            "It was the most she had said to him in one sitting in years. She had not known she was saving it up."
            yancey "Lord. You've been busy."
            sabra "Someone had to be."

        "\"I'm glad you're home.\"":
            $ yancey_relationship += 10
            "She said it simply. She had not planned to."
            sabra "I'm glad you're home."
            "He was quiet a long time. Then:"
            yancey "So am I."
            "It was, she thought afterward, one of the truest things he had ever said to her."

    hide yancey
    hide sabra

    $ journal_scene19 = True
    call journal_entry("SCENE 19", "He came back from Cuba wearing a hat with eight notches. I counted. There are men who do not count such things — I am no longer one of them. He is alive. He is Yancey. The hat sits on the bedpost now. I do not know whether I am glad of that or frightened.") from _call_journal_scene19

    jump scene20_dixie_trial


## ─── SCENE 20 — Dixie Lee's Trial ────────────────────────────────────────────

label scene20_dixie_trial:

    scene bg_courthouse_interior with dissolve
    play music "audio/courthouse_quiet.ogg" fadein 1.5 loop

    "1899."

    "The charge against Dixie Lee was keeping a disorderly house."

    "Half of Osage had conducted business on her premises. The half that was prosecuting her would rather not have that recalled."

    show sabra neutral at right with dissolve

    "Yancey Cravat had volunteered his services as her defense counsel."

    "Sabra had learned of this from Sol Levy, not from Yancey."

    sabra "He said nothing to me."

    "Sol had looked at her with the particular patience of a man who knows the answer to the next question."

    hide sabra

    ## ── Choice 1: Night before ───────────────────────────────────────────────

    scene bg_editorial_office_night with dissolve

    show sabra neutral at center with dissolve

    "The night before the trial, Sabra sat at the editor's desk and thought."

    menu:
        "Sabra's private judgment:"

        "She was wrongly prosecuted. It is a matter of justice.":
            $ yancey_relationship += 5
            $ newspaper_stance    += 1
            $ indian_sympathy     += 1
            sabra "The law is being used selectively. That is a corruption of the law."
            "She thought of Isaiah. Of the advertiser who had come to her door."
            "She understood, in some way she had not articulated before, exactly why Yancey had taken the case."
            sabra "He is right. Whatever else he is, he is right about this."

        "The law is the law. She knew what she was doing.":
            $ yancey_relationship -= 5
            sabra "She made her choices. The law makes its."
            "She was not proud of the thought. She held it anyway."
            "Then she thought of the women in her Women's Club — the ones who had come to the territory with nothing — and she was less certain."

        "It is about equal enforcement, not sympathy.":
            $ newspaper_stance    += 1
            $ sabra_independence  += 1
            sabra "The argument is not that she is innocent by virtue of circumstance. It is that the statute is not applied to everyone equally."
            "That was a cleaner argument. She could hold that one."
            sabra "Yancey never makes the clean argument when the dramatic one is available."

    ## ── Minigame setup ──────────────────────────────────────────────────────

    hide sabra

    scene bg_courthouse_interior with dissolve

    show yancey neutral at left with dissolve

    "The morning of the trial. The courthouse was full."

    show sabra neutral at right with dissolve

    "Sabra sat in the gallery. She had a notebook."

    "She had not told Yancey she was coming."

    "He saw her and a complicated expression moved across his face. He nodded once."

    "She opened her notebook."

    show yancey passionate
    yancey "Your Honor. Before we begin."

    "He surveyed the room. He always began by surveying the room."

    "Sabra looked at the gallery — at the faces of Osage, at the judge, at Dixie Lee seated very still at the defense table. At Yancey."

    sabra "What would I use."

    "It was a reporter's thought. But it was also a lawyer's thought. And it was, she realized, the thought of a woman who understood more about this territory's law than she had when she arrived."

    "She looked at her notes."

    $ trial_sel   = []
    $ trial_ord   = [None, None, None]
    $ trial_phase = 1
    call screen trial_arguments_minigame
    $ trial_sel = _return[0]
    $ trial_ord = _return[1]

    jump scene20_trial_result


label scene20_trial_result:

    ## ── Apply selection bonuses ───────────────────────────────────────────────

    if 2 in trial_sel:
        $ yancey_relationship += 5
    if 3 in trial_sel:
        $ newspaper_stance += 1
    if 5 in trial_sel:
        $ yancey_relationship += 3
        $ community_standing  -= 1
    if 6 in trial_sel:
        $ newspaper_stance += 1
    if (1 in trial_sel) and (4 in trial_sel):
        $ newspaper_stance    -= 1
        $ yancey_relationship -= 3

    ## ── Apply order bonuses ───────────────────────────────────────────────────

    if trial_ord[2] == 2:
        $ yancey_relationship += 3
    if trial_ord[0] == 5:
        $ community_standing -= 1
    if trial_ord[0] == 6:
        $ newspaper_stance += 1

    ## ── Narrative reaction ────────────────────────────────────────────────────

    "He presented the arguments."

    "She had heard Yancey speak a hundred times — at camp meetings, at rallies, at the street corner after a killing. She had never heard him in a courtroom."

    "It was different. It was focused."

    if yancey_relationship >= 60:
        "He was brilliant. She had known he would be. She wrote it down anyway."
        show yancey passionate
        yancey "The law is not a weapon to be aimed at the inconvenient. It is the common protection of every person in this territory — or it is nothing."
        "The gallery was very quiet."
    elif yancey_relationship >= 40:
        "He was good. Some of the arguments landed harder than others."
        yancey "This court has the choice between justice and appearances. I trust it will choose correctly."
        "The judge's expression gave nothing away."
    else:
        "He was himself — too dramatic, too long, too convinced of his own genius."
        yancey "Let the record show that this prosecution is an embarrassment to the territory and a disgrace to this bench."
        "The judge looked unimpressed."

    "The jury was out forty minutes."

    show dixie neutral at center with dissolve

    "Not guilty."

    "Dixie Lee sat very still for a long moment. Then she looked at the gallery and found Sabra's face."

    "The look between them said something neither of them would ever put into words."

    jump scene20_post_verdict


label scene20_post_verdict:

    ## ── Choice 2: The Editorial ──────────────────────────────────────────────

    "That afternoon, Sabra wrote the Wigwam's account of the trial."

    "She wrote it four times before she was satisfied."

    menu:
        "The Wigwam's editorial on the verdict:"

        "Support the verdict — Yancey was right to take the case.":
            $ newspaper_stance    += 2
            $ community_standing  -= 1
            $ dixie_lee_editorial  = "support"
            sabra "The jury found her not guilty because the prosecution's case was, as Mr. Cravat demonstrated, an exercise in selective application of the law. This paper supports that verdict."
            "Three subscribers cancelled. Two new ones wrote in."

        "Oppose publicly — the verdict sends the wrong message.":
            $ newspaper_stance    -= 2
            $ community_standing  += 1
            $ yancey_relationship -= 5
            $ dixie_lee_editorial  = "oppose"
            sabra "Whatever one believes about the law's application, the verdict does not reflect credit on this community."
            "She filed it. It was not the piece she was proudest of."
            "Yancey did not speak to her for three days."

        "Report facts only — the verdict, the arguments, nothing more.":
            $ newspaper_stance    += 1
            $ community_standing  += 2
            $ sabra_independence  += 1
            $ dixie_lee_editorial  = "neutral"
            sabra "The Wigwam reports: Dixie Lee was acquitted. These were the arguments presented. The jury deliberated forty minutes."
            "The piece ran four paragraphs. It was the most-read edition of the month."

    ## ── Choice 3: Dixie Lee in the hallway ───────────────────────────────────

    "Dixie Lee was waiting in the courthouse hallway."

    "She was not waiting for Yancey. Yancey was already surrounded by admirers."

    "She was waiting for Sabra."

    menu:
        "Sabra's response:"

        "Grace — stop and speak to her.":
            $ community_standing += 1
            sabra "Congratulations, Dixie."
            "Dixie Lee looked at her steadily."
            "Dixie Lee: I know what it cost you to be in that gallery."
            sabra "I was covering the trial."
            "A small smile."
            "Dixie Lee: Of course you were."

        "Cool — nod and walk past.":
            $ community_standing -= 1
            "She nodded. She did not stop."
            "She told herself she was busy. She probably was."

        "Walk past without acknowledgment.":
            "She looked straight ahead."
            "She felt Dixie Lee's eyes on her back all the way down the courthouse steps."
            "She did not turn around."

    hide dixie
    hide yancey
    hide sabra

    $ journal_scene20 = True
    call journal_entry("SCENE 20", "Not guilty. I sat in that gallery and watched my husband make the argument I would have made if I had been the lawyer, and the jury came back with the only verdict that was right. I do not know what I feel about Dixie Lee. I know what I feel about the law. They are not entirely the same feeling.") from _call_journal_scene20

    jump scene21_statehood


## ─── SCENE 21 — The Statehood Question ───────────────────────────────────────

label scene21_statehood:

    scene bg_civic_hall with dissolve
    play music "audio/state_seal.ogg" fadein 1.5 loop

    "1901."

    "The Territory was growing up. Everyone could feel it."

    "The question was no longer whether Oklahoma would become a state. The question was what kind."

    show sabra neutral at left with dissolve
    show sol neutral at right with dissolve

    "Sol Levy had opinions. He always had opinions. He expressed them quietly, which was why people listened."

    sol "One state combines the territories. It is efficient. It is also the end of everything the Indian Nations were promised."

    sabra "I know."

    sol "Two states — an Oklahoman state and an Indian state, Sequoyah, as they're calling it — honors the treaties. But Congress will never allow it."

    sabra "Congress has never allowed anything for the Nations without being forced."

    sol "Yes."

    "They stood with that for a moment."

    ## ── Choice 1: Editorial Stance ──────────────────────────────────────────

    menu:
        "The Wigwam's editorial position:"

        "One state — it is coming regardless, and Oklahoma must be ready.":
            $ newspaper_stance   -= 2
            $ indian_sympathy    -= 2
            $ sabra_independence += 2
            $ statehood_stance    = "single"
            sabra "Congress will not divide it. Writing editorials against arithmetic is vanity."
            "She wrote it clearly: Oklahoma statehood, combined, was the practical and inevitable path."
            "The piece made allies in Guthrie. It troubled her in the night."

        "Two states — the treaty obligations must be honored.":
            $ newspaper_stance += 2
            $ indian_sympathy  += 2
            $ sabra_independence += 2
            $ statehood_stance   = "double"
            sabra "The Wigwam will not advocate for the violation of a legal obligation simply because violating it is convenient."
            "She wrote the argument. Arita Red Feather sent a note: 'The Wigwam has said it plainly. Thank you.'"
            sol "It will not change the outcome."
            sabra "Perhaps not. But the Wigwam will have said it."

        "Consult the communities first — this affects people who must be heard.":
            $ newspaper_stance   += 1
            $ indian_sympathy    += 2
            $ community_standing += 1
            $ sabra_independence += 2
            $ statehood_stance    = "consult"
            sabra "Before the Wigwam takes a position, I want statements from the Cherokee Nation, the Osage, and the Choctaw. Let them speak. Then we'll have an argument."
            "She ran the series over four weeks. Readers wrote in from across the territory."
            "The Wigwam had not taken a final position, but it had made people think."

    hide sol

    ## ── Yancey's Letter ──────────────────────────────────────────────────────

    "A letter came from Yancey. He was in Guthrie covering the constitutional convention."

    "She read it at the composing table."

    "His argument was characteristically Yancey: eloquent, sweeping, and entirely certain."

    "He believed two states was right — the Indian Nations had a right to their own sovereignty — but he believed it was a lost cause and the Wigwam should get out in front of the single-state argument before less principled editors framed it."

    ## ── Choice 2: Yancey's Letter ────────────────────────────────────────────

    menu:
        "Sabra's response to Yancey's letter:"

        "He's right. Adjust the Wigwam's position accordingly.":
            $ yancey_relationship += 5
            sabra "He is correct on the practical argument, whatever I think of the principle."
            "She did not like it. She made the adjustment."
            "She told herself it was pragmatism."

        "I'll decide for myself. He can write his own paper.":
            $ sabra_independence  += 2
            $ yancey_relationship -= 5
            sabra "He is three hundred miles away covering a convention. I am here. I will make the editorial decisions of this paper."
            "She filed his letter in the drawer and did not change a word."

        "Print his letter as a contributed piece — let readers judge.":
            $ newspaper_stance   += 1
            $ sabra_independence += 2
            sabra "The Wigwam will print Yancey Cravat's argument on the statehood question as a contributed opinion. The editor's view may differ."
            "She added a one-line editor's note: 'The Wigwam's full editorial position will follow.'"
            "Yancey wrote back: 'I am proud of you and irritated.'"

    hide sabra

    "November 16, 1907."

    "Oklahoma became the forty-sixth state of the Union."

    show sabra neutral at center with dissolve

    "Sabra stood at the Wigwam window and watched the street."

    "Doc Valliant came in with a bottle of whisky and two glasses."

    "Doc Valliant: Well, Mrs. Cravat. We are Oklahomans."

    sabra "We always were."

    "He poured. She raised the glass."

    "They did not say anything else. There was not anything else to say."

    hide sabra

    $ journal_scene21 = True
    call journal_entry("SCENE 21", "Oklahoma. I have lived in a territory my whole life here, and now it is a state. I should feel something neat and definite about that. I feel instead that the territory I came to — the raw and difficult and possible place — is receding. What is arriving in its place is something more ordered, and I cannot tell yet whether I will love it.") from _call_journal_scene21

    jump scene22_first_oil


## ─── SCENE 22 — The First Oil ─────────────────────────────────────────────────

label scene22_first_oil:

    scene bg_oil_derrick_distant with dissolve
    play music "audio/oil_derricks.ogg" fadein 1.5 loop

    "1905."

    "The derricks had been going up east of Osage for two years."

    "From the Wigwam window, on a clear morning, Sabra could count seven of them — skeletal iron structures against the sky, pumping with a rhythmic, patient violence."

    show sabra neutral at right with dissolve
    show cim neutral at left with dissolve

    "Cim was seventeen. He had his father's frame and his grandfather Venable's eyes, and he spent every afternoon he could down at the lease office talking to the survey men."

    cim "There are formations under the Osage hills that they haven't even mapped yet."

    sabra "You have a geometry exam on Friday."

    cim "The formations don't care about my geometry exam."

    "She looked at him. He was not wrong."

    hide sol

    ## ── Choice 1: The Oil Story Headline ────────────────────────────────────

    show sol neutral at right with dissolve

    "Sol Levy had the same expression he always wore when he was about to point out something she already knew."

    sol "Tracy Wyatt is in town."

    sabra "I know."

    sol "He is talking to three lease holders and the deputy territorial treasurer."

    sabra "I know."

    sol "Are you going to cover it?"

    menu:
        "The Wigwam's headline on the oil story:"

        "Progress — lead with the economic opportunity.":
            $ newspaper_stance   -= 1
            $ community_standing += 1
            sabra "OKLAHOMA OIL: The Future Arrives in Osage County."
            "She wrote it with energy. It was a good story. It was also, she knew, the story Tracy Wyatt wanted told."
            sol "The lease companies will appreciate that."
            sabra "The lease companies are not who I'm writing for."
            "She believed it. She was also not entirely certain."

        "Caution — note the leases before celebrating the boom.":
            $ newspaper_stance += 1
            $ community_standing += 1
            sabra "OIL IN THE HILLS: What the Lease Terms Mean for Osage County."
            "She spent a week on it. She read three lease documents, two federal filings, and Yancey's notes from Guthrie."
            "The piece was not romantic. It was read by everyone."
            sol "That is the piece that needed writing."

        "Own the story — run it before Tracy Wyatt can shape it himself.":
            $ newspaper_stance   += 1
            $ community_standing += 2
            $ sabra_independence += 1
            sabra "We run it tomorrow. First. Before the Guthrie papers."
            sol "You don't have all the facts yet."
            sabra "I have enough. I'll get the rest in the follow-up."
            "The Wigwam broke the story. Every paper in the territory followed."
            "It was the best day she had had as an editor."

    hide sol

    ## ── Choice 2: Cim and Oil ────────────────────────────────────────────────

    "Tracy Wyatt came to the Wigwam that afternoon. He was charming, modern, and very interested in everything."

    show tracy neutral at right with dissolve

    tracy "Mrs. Cravat. I've been reading your paper for two years."

    sabra "Then you know the Wigwam's editorial positions."

    tracy "I do. That's why I'm here."

    "He left her with a card and a proposition: a standing column, sponsored, on the oil industry."

    "She put the card in her drawer."

    hide tracy

    "Cim had watched the whole exchange from the corner of the pressroom."

    menu:
        "Sabra's conversation with Cim about his future:"

        "\"Finish your degree first. Then whatever you want.\"":
            $ sabra_independence += 1
            sabra "I will not have a Cravat leave school before he's ready. Your father does enough of that for all of us."
            cim "He didn't finish school either."
            sabra "I know. And what has it cost him?"
            "Cim thought about it. He did not have a ready answer."

        "\"Learn everything you can about it — oil, law, the whole thing.\"":
            $ sabra_independence += 1
            $ community_standing += 1
            sabra "If you're going to be part of this, understand it. Read the leases. Talk to the Osage mineral council. Understand what is at stake for everyone."
            "Cim's face opened up."
            cim "That is what I'm trying to do."
            sabra "Then do it properly."

        "\"Your father would say — follow what you can't stop thinking about.\"":
            $ yancey_relationship += 5
            sabra "Your father would tell you that if you can't stop thinking about something, that's the answer."
            "A pause."
            cim "Is that what you think?"
            sabra "I think your father is right about more things than I give him credit for."
            "The admission surprised her as much as it surprised Cim."

    hide cim
    hide sabra

    $ journal_scene22 = True
    call journal_entry("SCENE 22", "The derricks rise like iron insects against the Osage sky. Cim watches them the way Yancey once watched the horizon west. I know what that watching means. It means he is going to leave me for something — not unkindly, not permanently, but inevitably. I am learning to call that a good thing.") from _call_journal_scene22

    jump scene23_what_yancey_left


## ─── SCENE 23 — What Yancey Left ─────────────────────────────────────────────

label scene23_what_yancey_left:

    scene bg_wigwam_modern with dissolve

    "1907. November."

    "Statehood had come and Yancey was gone."

    "He had been gone fourteen months. The last letter was from Tulsa — oil fields, he said. A story worth telling."

    show sabra neutral at center with dissolve

    "Donna was sixteen and going east to Miss Dignum's school in the spring."

    show donna neutral at right with dissolve

    donna "I'm only going for the year."

    sabra "I know."

    donna "I'll come back."

    sabra "I know that too."

    "She did not say: your father said the same thing, about almost everything."

    "She did not need to."

    ## ── A letter arrives ─────────────────────────────────────────────────────

    "The morning post brought a letter."

    "His handwriting."

    "She held it a moment before opening it."

    menu:
        "Sabra's choice:"

        "Write back immediately — keep the correspondence alive.":
            $ yancey_relationship += 5
            sabra "Donna. I have to write a letter."
            "She wrote four pages. About the paper. About Cim and the oil surveys. About statehood day and Doc Valliant's whisky."
            "She did not know if he would receive it before he moved on again. She sent it anyway."
            "Some letters are for the writing, not the reading."

        "File it with the others — this is who he is.":
            $ sabra_independence += 2
            "She read it twice. She put it in the drawer with the others."
            "There were twenty-three letters in the drawer now."
            "Each one said, in its own way: I am alive. I am somewhere. I am sorry."
            sabra "I know."

        "Read it aloud to the children.":
            $ yancey_relationship -= 5
            $ sabra_independence  += 2
            sabra "Donna. Cim. Come down. Your father has written."
            show cim neutral at left with dissolve
            "They gathered at the composing table. She read."
            "Cim was expressionless in the way he had learned from her."
            "Donna cried a little, quietly."
            "They went back to what they were doing."
            hide cim

    hide donna

    ## ── Choice 2: Taking Stock ────────────────────────────────────────────────

    "She sat alone in the pressroom after the children were asleep."

    "The type cases. The press. The smell of ink that had been in her nose for seventeen years."

    menu:
        "Sabra's reckoning:"

        "I chose this. Every day I stayed, I chose.":
            $ sabra_independence += 1
            $ community_standing += 1
            sabra "I have not been abandoned here. I have been here."
            "It was the kind of thought that either meant everything or nothing."
            "Tonight it meant something."
            "She crossed to the press and laid her hands flat on the chase, feeling the cold of the iron."
            sabra "My paper. My town. My life."

        "Pragmatism — this is what is, and I have made something of it.":
            $ sabra_independence -= 1
            $ community_standing += 1
            sabra "I did not get the life I imagined from the parlor in Wichita. I got this one."
            "She looked around at the pressroom — at what she had built and what had been left to her and what she had made, through will, into the same thing."
            "It was not romantic. It was true."

        "I'm still waiting. Not for him — for what comes next.":
            $ sabra_independence += 1
            $ yancey_relationship += 5
            sabra "I am not waiting for Yancey Cravat."
            "A pause."
            sabra "I am waiting for whatever this becomes."
            "She didn't know, yet, what that was."
            "She had learned that not knowing was survivable."

    hide sabra

    scene black with dissolve

    "— End of Chapter Four —"

    call chapter4_summary from _call_chapter4_summary

    return


## ─── CHAPTER 4 SUMMARY ───────────────────────────────────────────────────────

label chapter4_summary:

    scene black

    "CHAPTER FOUR COMPLETE"
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
    if newspaper_stance >= 6:
        "THE WIGWAM: Progressive and outspoken — advocate for the Indian Nations, women's voice, reform. Oklahoma knows its name."
    elif newspaper_stance <= -4:
        "THE WIGWAM: Conservative — careful, community-minded, advertiser-safe. It is trusted by the right people."
    else:
        "THE WIGWAM: Balanced — it prints what it believes, mostly. The rest it is still learning."

    " "

    ## Community standing
    if community_standing >= 8:
        "STANDING IN OSAGE: Beloved. Oklahoma is a state now. It was built, in part, by Sabra Cravat."
    elif community_standing <= -3:
        "STANDING IN OSAGE: Complicated. She has made the right enemies."
    else:
        "STANDING IN OSAGE: Respected. They know her name and mean it."

    " "

    ## Indian sympathy
    if indian_sympathy >= 5:
        "ON THE INDIAN QUESTION: Advocate — her name is known in the Nations as someone who told the truth."
    elif indian_sympathy <= -3:
        "ON THE INDIAN QUESTION: Accommodating — she has bent with the current more than she would like to admit."
    else:
        "ON THE INDIAN QUESTION: Cautious, but her record speaks."

    " "

    ## Sabra's independence
    if sabra_independence >= 12:
        "SABRA'S INDEPENDENCE: Absolute. She does not wait for permission and has not for years."
    elif sabra_independence >= 6:
        "SABRA'S INDEPENDENCE: Substantial. She has learned to act on her own judgment."
    else:
        "SABRA'S INDEPENDENCE: Growing. Each absence has taught her something she could not have learned otherwise."

    " "

    ## Achievement flags
    if dixie_lee_editorial == "support":
        "She supported the not-guilty verdict in print. It cost her subscribers. She kept printing."
    elif dixie_lee_editorial == "oppose":
        "She opposed the verdict. Yancey did not speak to her for three days."
    elif dixie_lee_editorial == "neutral":
        "She reported the trial without comment. The most-read edition of the year."

    if statehood_stance == "double":
        "The Wigwam argued for two states — for the honor of the treaty obligations — when most editors would not."
    elif statehood_stance == "single":
        "She chose the practical argument on statehood. She has not entirely forgiven herself."
    elif statehood_stance == "consult":
        "She ran four weeks of testimony from the Nations before taking a position. People heard voices they had not heard before."

    if isaiah_defended:
        "She defended Isaiah against a man with money and she knew the cost and she did it anyway."

    if yancey_relationship >= 50 and sabra_independence >= 8:
        "She has managed to love Yancey Cravat and to need him less. Both things are true. She has stopped trying to resolve the contradiction."

    " "

    jump chapter5_start
