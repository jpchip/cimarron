## script_chapter5.rpy
## Cimarron: Chapter Five — Legacy & Monument (1910–1930)
## Based on Cimarron by Edna Ferber (1929), public domain.
##
## Scene structure:
##   scene24_cim_ruby       → Cim brings Ruby Big Elk home (c. 1910)
##   scene25_congresswoman  → Sabra runs for and serves in Congress (c. 1920)
##   scene26_donnas_wedding → Donna marries Tracy Wyatt (c. 1916)
##   scene27_bowlegs        → Yancey's death in the oil fields (1930)
##   scene28_monument       → The Pioneer monument unveiling; photograph minigame; endings


## ─── Entry Point ──────────────────────────────────────────────────────────────

label chapter5_start:
    $ renpy.block_rollback()

    scene black with fade

    "CIMARRON"
    "{i}Based on the novel by Edna Ferber{/i}"
    "Chapter Five: Legacy and Monument"
    "{i}Osage, Oklahoma. 1910–1931.{/i}"

    play music "audio/kihekah_parlor.ogg" fadein 1.5 loop

    jump scene24_cim_ruby


## ─── SCENE 24 — Cim Brings Ruby Home ─────────────────────────────────────────

label scene24_cim_ruby:

    scene bg_kihekah_house_parlor with dissolve

    play music "audio/kihekah_parlor.ogg" fadein 1.0 loop

    play sound "sfx/car_engine_1910.ogg"
    "On a Saturday, a large automobile pulled up in front of the house on Kihekah Street."

    "Sabra had been told. She had had three weeks to think about it. She had thought about it every morning and then put it away and thought about it again."

    show big_elk neutral at left with dissolve

    "Big Elk and his wife sat formally in the parlor chairs, as if waiting in a bank. His wife wore a blanket shawl and kept her hands folded. He was very large and very still, the way the old headmen were still — a stillness that was not patience but something beyond patience."

    show sabra ch5 neutral at right with dissolve

    "Sabra entered from the hallway."

    sabra "Good afternoon."

    "She said it to the room. She was not sure yet where to put her eyes."

    hide big_elk

    show cim neutral at left with dissolve

    "Then Cim came in from the kitchen with a young woman at his side."

    cim "Mother, this is my wife."

    "She was twenty years old, perhaps. Dark-haired, composed, with the straight back and the measuring eyes that Sabra associated with the older Osage women — the ones who had seen the treaty negotiations and had stopped expecting much."

    show ruby neutral at center with dissolve

    ruby "Mrs. Cravat."

    "Her voice was low and clear. She waited."

    "The room was very quiet. Cim was watching his mother. Ruby was watching nothing in particular, with the Indian patience that Sabra had never quite understood — the capacity to simply be present without pushing."

    ## ── Choice 1: Sabra's Response to Ruby ──────────────────────────────────

    menu:
        "The room is very quiet. What does she say to this young woman?"

        "\"Welcome to our family.\" (And mean it)":
            $ indian_sympathy    += 3
            $ yancey_relationship += 5
            $ ruby_welcomed       = True

            show sabra ch5 happy
            sabra "Welcome to our family, Ruby."

            show big_elk acknowledging at left
            "She said it and meant it — or tried to mean it — and found, to her own surprise, that it was not entirely performance. She took Ruby's hands. Ruby's grip was firm and brief. Big Elk nodded once. Cim exhaled."

            "She heard Yancey in herself, then. {i}Of course. Who else would Cim marry?{/i} She could almost hear the teasing satisfaction in it."

        "\"I need time.\" (Honest, not cruel)":
            $ ruby_time_needed = True

            "She stepped forward. She shook Ruby's hand formally."

            sabra "I hope we'll come to know each other well."

            "She said the words carefully, choosing them the way she chose type — for accuracy, not warmth. But Ruby saw through them. She would always see through her. There was no hiding from that quality of attention."

            "It was honest, at least. Not her mother's smile. Not Felice's performance of graciousness as a form of condescension."

        "\"My son chose this. I will be civil.\" (Duty without warmth)":
            $ indian_sympathy    -= 1
            $ yancey_relationship -= 5

            "She kept the smile in place. It was the exact smile her mother Felice had used on people she considered beneath her — that particular brightness, all surface."

            sabra "Cim has spoken of you."

            "She recognized the smile only later. Standing at the kitchen window after Big Elk and his wife had gone, she recognized it, and felt ashamed."

    ## ── Big Elk's Formal Words (through Ruby) ────────────────────────────────

    show big_elk neutral at left with dissolve

    "Big Elk spoke. Ruby translated, her voice careful and neutral: three words, but from the way he had taken the time to compose them, they carried more weight than three words."

    ruby "My father says: we are glad."

    "He meant more. He meant: {i}We hope you will be worthy of our daughter. We have considered this. We accept it now, and we expect you to live up to what that means.{/i}"

    "Sabra heard: {i}We accept this.{/i} She supposed that was close enough."

    menu:
        "How does she respond?"

        "\"Tell him — I hope to know him better.\"":
            $ indian_sympathy += 1

            sabra "Tell your father — I hope to know him better."

            show big_elk acknowledging at left
            "Ruby translated. Big Elk inclined his head. The formality closed like a door, gently."

        "\"The formalities are appreciated.\" (Polite, distant)":
            sabra "Please tell him the formalities are appreciated."

            "Ruby translated without expression. Big Elk looked at Sabra for a moment, then at Cim, then nodded. Appropriate distance maintained on all sides."

        "\"Tell him he's welcome here whenever he comes to Osage.\"":
            $ community_standing += 1
            $ indian_sympathy    += 1

            sabra "Tell him he is welcome in this house whenever he is in Osage. Both of them are."

            show big_elk acknowledging at left
            "She meant it. Ruby translated. Something shifted in Big Elk's face — not warmth, exactly, but a recalibration. He spoke again, briefly."

            ruby "He says: thank you."

    ## ── Recovery arc ─────────────────────────────────────────────────────────

    hide big_elk with dissolve

    if ruby_time_needed:
        "After Big Elk and his wife had risen and the formal goodbyes were done, Ruby came back to the parlor alone while Cim walked his father to the automobile."

        "She sat across from Sabra without being invited. Not rude — simply practical. She had a thing to say."

        show ruby direct at center with dissolve

        ruby "I didn't expect it to be easy."

        sabra "No."

        ruby "It won't always be uncomfortable."

        "She said it without consolation, the way you would state a weather pattern. Sabra found herself — unexpectedly — believing her."

        $ indian_sympathy += 1

    ## ── Journal Entry 24 ─────────────────────────────────────────────────────

    scene bg_journal with dissolve

    $ journal_scene24 = True

    sabra "{i}October, 1910.{/i}"

    sabra "{i}Cim's wife has his same quality of stillness — the ability to be entirely present without pushing. I don't know what to do with that. I'm trying.{/i}"

    play music "audio/kihekah_parlor.ogg" fadein 1.0 loop

    jump scene25_congresswoman


## ─── SCENE 25 — The Congresswoman ────────────────────────────────────────────

label scene25_congresswoman:

    scene bg_washington_dc_hall with dissolve

    play music "audio/congress_hall.ogg" fadein 1.5 loop

    "Twenty years compressed into narration: the Wigwam, the town council, the women's federation, the oil land hearings. Osage had grown past Sabra's ability to fully contain it, and so had Sabra."

    "She was fifty-two years old when they asked her to run."

    show sabra ch5 neutral at right with dissolve

    "Not the women's club this time. The state party. They had looked at her record — twenty-odd years of editorial advocacy, her work on the Osage mineral rights dispute, the testimony she had given at the Federal hearing — and they had made a practical calculation."

    "Sol Levy had written from his shop on Main Street: {i}'Go. The territory owes you this. You have already been doing the work.'  {/i}"

    ## ── Choice 1: Whether to Run ──────────────────────────────────────────────

    menu:
        "She is fifty-two years old. She has been running something without the title for twenty years."

        "\"Yes. I'll run.\"":
            $ community_standing += 3
            $ sabra_independence  += 2

            show sabra ch5 determined
            sabra "Yes. I'll run."

            "She said it before she had time to think better of it. The party man shook her hand with both of his. She won. Of course she won. She had been winning Osage over for two decades, and this was just a larger version of Osage."

        "\"Yes. For one term.\"":
            $ community_standing += 2
            $ sabra_independence  += 1

            sabra "Yes. One term. Someone younger should take it after."

            "A modest yes, and she meant it. She would stay longer than she planned. One term became two. The second one surprised her more than anyone."

        "\"Someone else should have this. Someone younger.\"":
            $ community_standing -= 1

            sabra "I think there are younger women better suited—"

            "She got no further. The women's club descended on her in shifts over three days. She allowed herself to be talked back into it. She had known she would allow it. She was not sorry."

    ## ── Choice 2: Primary Issue ───────────────────────────────────────────────

    "Washington. Marble corridors. Senators who met her eyes with the particular expression of men calculating how much trouble she intended to cause."

    "She had a seat. She could spend it on what Osage needed, or what Oklahoma needed, or what she believed."

    menu:
        "Her colleagues on the floor are watching. What does she bring to the floor?"

        "\"Indian reservation reform. The system is unjust and I'll say so.\"":
            $ indian_sympathy  += 3
            $ newspaper_stance += 1
            $ congress_issue    = "indian"

            "She introduced the bill on her third week. It was radical enough to make enemies. She made them."

            "The Osage mineral rights protections, the land allotment fraud, the delayed federal rations — she named them, in order, into the Congressional Record. Senators from western states watched her with the careful attentiveness of men deciding whether to be amused or alarmed."

            "She was neither amusing nor alarming. She was simply accurate."

        "\"Oklahoma needs oil law reform. The fields are lawless.\"":
            $ newspaper_stance  += 1
            $ community_standing += 1
            $ congress_issue      = "oil_law"

            "Practical, popular, necessary. The wildcatters had been running ahead of the law for fifteen years and the federal surface rights framework was, as she told the committee, 'a polite fiction worn down to transparency.'"

            "She built a coalition. She got two provisions into the revision. It was less than she wanted and more than she expected."

        "\"Education. Especially for Indian children leaving the reservation schools.\"":
            $ indian_sympathy    += 2
            $ community_standing += 2
            $ congress_issue      = "education"

            "A bridge position — contentious enough to mean something, practical enough to pass. She built coalitions with unusual partners: a Senator from Massachusetts who had visited the Carlisle school and come home troubled by what he had seen."

            "Three things actually changed. She counted them in her journal on the last night of the session."

    ## ── Closing beat ─────────────────────────────────────────────────────────

    "The corridors of Congress were marble and hushed, and the Senators who had underestimated her had been numerous enough to keep her company."

    "At a reception in the third year, a Senator from Pennsylvania — large, affable, the kind of man who told the same four stories — caught her eye across the room."

    "\"Oklahoma,\" he said, with the expansive goodwill of a man on his fourth bourbon. \"You know what Oklahoma needs? A woman Governor.\" He said it as a joke. He was surprised when she didn't laugh."

    "She wrote it down."

    ## ── Journal Entry 25 ─────────────────────────────────────────────────────

    scene bg_journal with dissolve

    $ journal_scene25 = True

    sabra "{i}1923.{/i}"

    sabra "{i}A Senator from Pennsylvania told me Oklahoma needed a woman Governor. He said it as a joke. I wrote it down.{/i}"

    play music "audio/kihekah_parlor.ogg" fadein 1.0 loop

    jump scene26_donnas_wedding


## ─── SCENE 26 — Donna's Wedding ──────────────────────────────────────────────

label scene26_donnas_wedding:

    scene bg_kihekah_house_parlor with dissolve

    play music "audio/kihekah_parlor.ogg" fadein 1.0 loop
    play sound "sfx/wedding_march.ogg"

    "[donna_name] Cravat married Tracy Wyatt in the spring of 1916."

    "Tracy Wyatt arrived exactly on time. He was prosperous, handsome in an amiable way, entirely reliable, and constitutionally incapable of the kind of magnificent unreliability that had defined the last thirty years of Sabra's life."

    show donna neutral at center with dissolve

    "He was, in short, everything Yancey was not."

    show sabra ch5 neutral at right with dissolve

    "[donna_name] was composed, as she always was. She was her grandmother Felice's grandchild and her mother's daughter, which meant she had both the armor and the nerve."

    "Before the ceremony, five minutes in the back room. [donna_name] in her wedding dress, Sabra with the coverlet Mother Bridget had pressed into her hands on the morning they had left Wichita."

    sabra "This was given to me on my wedding morning. I've kept it thirty years."

    donna "I know. I've seen it in the chest."

    sabra "Take it with you."

    "[donna_name] folded it into her hands without ceremony. She had her mother's practicality about gifts."

    show tracy charming at left with dissolve

    ## ── Choice 1: What Sabra Tells Donna ────────────────────────────────────

    menu:
        "Five minutes in the back room. She has one thing she wants to say."

        "\"You've chosen well. You always choose well.\"":
            $ community_standing += 1
            $ donna_wedding_advice = "chose_well"

            sabra "You've chosen well. You always choose well."

            "It was true. [donna_name] had always known exactly what she wanted and had moved toward it without apology. Sabra wondered, briefly, whether choosing well and living fully were the same thing. She decided this was not the moment to raise that question."

        "\"Whatever comes — you'll manage it. You're Cravat stock.\"":
            $ sabra_independence += 1
            $ donna_wedding_advice = "cravat_stock"

            sabra "Whatever comes — you'll manage it. You're Cravat stock."

            "She meant: {i}You don't need anyone to save you.{/i} [donna_name] gave her a long look."

            donna "I know, Mother."

            "She already knew."

        "\"I hope he makes you happy.\" (Quietly)":
            $ yancey_relationship  += 5
            $ donna_wedding_advice = "be_happy"

            sabra "I hope he makes you happy."

            "She was thinking, unexpectedly, of her own wedding morning. The white sombrero. The impossible man. The fact that she had not, at twenty years old, had the wisdom to hope for happiness before hoping for everything else."

            "[donna_name] looked at her for a moment, and then did something she rarely did: she put her arms around her mother and held on for a second."

    ## ── Journal Entry 26 ─────────────────────────────────────────────────────

    scene bg_journal with dissolve

    $ journal_scene26 = True

    sabra "{i}April, 1916.{/i}"

    sabra "{i}[donna_name]'s wedding was beautiful and organized and Tracy Wyatt arrived exactly on time. I cried once, briefly, in the back room. Then I came out and ran the reception.{/i}"

    play music "audio/bowlegs_field.ogg" fadein 2.0 loop

    jump scene27_bowlegs


## ─── SCENE 27 — The Word from Bowlegs ────────────────────────────────────────

label scene27_bowlegs:

    scene bg_oil_field_bowlegs with dissolve

    play music "audio/bowlegs_field.ogg" fadein 1.0 loop
    play sfx "sfx/oil_drill.ogg" fadein 2.0 loop

    "Bowlegs, Oklahoma. 1930."

    "She had come on a congressional fact-finding trip. The town was everything old Osage had been in 1889 — raw, violent, desperate, full of men who had arrived from somewhere else in search of something they couldn't name — except that now the mud was black and the money was bigger and the violence moved faster."

    show sabra ch5 neutral at right with dissolve

    "A Harvard boy in bone-rimmed spectacles was showing her delegation around the field. He had the slightly injured expression of a man who had expected adventure and received instead the smell of crude oil and the sound of machinery."

    "There was a trial that morning. A dance-hall girl. The town's one judge held court in the back room of a hardware store. The defendant was nineteen and scared and guilty of nothing Osage hadn't seen in 1890."

    "There was a man in the holding pen for debt. Bill Somebody. He had drilled three dry holes and owed money to four companies and looked out through the wire with the specific expression of a man who has run out of ideas."

    "She wrote down what she saw. She had been writing down what she saw for forty years."

    "And then—"

    play sound "sfx/oil_blowout.ogg"
    "A sound from across the field. Not an explosion — something more pressurized than that, a column of oil and gas and released earth going up with a sound like the world tearing. The nitroglycerin canister shot upward with it."

    play sound "sfx/canister_whistle.ogg"
    "Forty lives in a single tin container."

    play sound "sfx/clipboard_drop.ogg"
    "The Harvard boy dropped his clipboard. The senators scattered."

    "And then a man ran out from the crowd — an old man, she saw even from that distance — and he ran the way an outfielder runs: not toward the canister but {i}to where it would come down,{/i} calculating it by some instinct that had nothing to do with thought."

    "He spread his arms. He caught it on his chest."

    "He went down with it."

    "The crowd parted for Sabra's white hair."

    "She did not know how she crossed the field. She only knew that she was running."

    "He was on his back in the oil-soaked dirt. Men stood in a ring. She pushed through them."

    show sabra ch5 sad

    "His face was older. The gray at the temples gone to white, the great chest diminished, the long coat muddy and torn. But the jaw was the same. The cheekbones. The ridiculous lashes."

    "Those ocean-gray eyes opened."

    "Glazed, then: they cleared."

    "His lips moved. He was saying something she didn't recognize — she had never heard of Peer Gynt, had never read Ibsen, knew nothing of Solveig or the Button Moulder or the play's long resolution. She only heard the words."

    show yancey dying at left with dissolve
    yancey "Wife and mother — you stainless woman — hide me — hide me in your love."

    "She didn't know it was a play. She only knew what he was asking."

    ## ── Choice: Her Last Words to Him ────────────────────────────────────────

    menu:
        "He is dying. The crowd has gone silent. She is holding his head."

        "\"You came back.\" (If she can mean it)" if yancey_relationship >= 50:
            $ yancey_relationship += 5

            sabra "You came back."

            "She said it the way she had wanted to say it for forty years: {i}You always came back. Always. Whatever you left behind, you always came back.{/i} He heard it. She was certain of that."

        "\"Sleep. You're safe.\"":
            $ yancey_relationship += 3

            show sabra ch5 tender
            sabra "Sleep. You're safe."

            "She became, without knowing it, Solveig. The play ended as it must."

        "\"I'm here. I'm here.\"":
            sabra "I'm here. I'm here."

            "She said it until it was the only true thing left."

    play sound "sfx/last_breath.ogg"
    "His eyes closed."

    "She did not stand up for a long time."

    hide sabra

    sabra "Sleep, my boy, my dearest boy."

    scene black with fade

    stop sfx fadeout 2.0
    stop music fadeout 3.0

    "  "

    jump scene28_monument


## ─── SCENE 28 — The Monument ──────────────────────────────────────────────────

label scene28_monument:

    scene bg_monument_ceremony with dissolve

    play music "audio/kihekah_parlor.ogg" fadein 2.0 loop

    "A year."

    "The monument had been commissioned by the state legislature — five hundred thousand dollars, the papers said, the largest allocation for public sculpture in Oklahoma's history. The sculptor was a Pole named Masja Krbecek, small and snuffy and extremely precise, who had come to Osage the previous winter with a letter of introduction and a portfolio of photographs of his previous work."

    show sabra ch5 neutral at right with dissolve

    "He had used Yancey's photographs. She knew that, had known it since the commission was announced. She had sent what she had."

    "Krbecek came to the house on Kihekah Street two days before the ceremony."

    show krbecek neutral at left with dissolve

    krbecek "Mrs. Cravat. Before I go — you mentioned photographs. I should like to see them, if you don't mind. To understand the man more fully. The statue is his body; I need the photographs for his face."

    sabra "I have a cedar box."

    krbecek "The face in photographs is always truer than the face in memory. Memory is generous."

    play sound "sfx/cedar_box_open.ogg"
    "She went to the parlor and opened the cedar box she had kept for forty years."

    "Inside: six photographs. She would give him two."

    ## ── Photograph minigame ───────────────────────────────────────────────────

    $ selected_photos = []

    call screen photograph_box_minigame

    $ selected_photos = _return

    jump scene28_photos_result


label scene28_photos_result:

    ## Pair outcome logic
    $ photo_set = set(selected_photos)

    show krbecek thoughtful at left with dissolve

    if photo_set == {1, 4}:
        ## Run + Rough Rider
        $ yancey_relationship += 3

        krbecek "Ah. A man in motion. Always motion. I think I understand now."

        "He turned both photographs over and over in his hands, as if the paper itself could tell him something."

    elif photo_set == {2, 3}:
        ## Tent church + Sabra at press
        $ community_standing += 2

        krbecek "He is not the center of these. She is. Interesting."

        "He looked up at Sabra, not at the photographs."

        sabra "The first one is the church. The second is the paper."

        krbecek "Yes. I see that."

        "He put them in his breast pocket."

    elif photo_set == {5, 6}:
        ## Kid's burial + Cim/Ruby
        $ indian_sympathy += 2

        krbecek "The land. And the people who came after. Yes. I see what to do."

        "He studied the family photograph for a long moment."

    else:
        ## Any other pair
        $ yancey_relationship += 1

        krbecek "Yes. A man of many faces. I will do my best."

        "He tucked the photographs away carefully."

    show krbecek neutral at left

    "He thanked her and left. The ceremony was the next morning."

    hide krbecek

    jump scene28_monument_reveal


label scene28_monument_reveal:

    "The ceremony square."

    "Five hundred people. Senators. Oil men. A delegation from the Osage Nation. The women's federation. The editor of the Tulsa paper. Sabra's granddaughter, who was eight years old and had Ruby's stillness and Cim's gray eyes and was therefore, in Sabra's considered opinion, entirely Yancey's fault."

    play sound "sfx/fabric_billow.ogg"
    "The canvas cover came down in a billow of pale cloth."

    "The statue showed a man with a great buffalo head — magnificent, menacing — stepping forward in high-heeled boots and a long coat, one hand resting on his holster. He was stepping forward as if the land itself had just given way beneath him and he was moving anyway."

    "Behind him, a blanketed Indian, one hand reaching toward the pioneer's shoulder."

    "Yancey."

    "Of course."

    "Who else could it have been."

    play sound "sfx/crowd_applause.ogg"

    ## ── Ending branch determination ───────────────────────────────────────────
    ## Checked in order: Branch 3 → 2 → 1 → fallback (Branch 1)

    if indian_sympathy >= 7 and (sabra_independence >= 5 or yancey_relationship >= 50):
        jump ending_land_belongs

    elif sabra_independence >= 8 and community_standing >= 8:
        jump ending_built_herself

    elif sabra_independence <= 4 and yancey_relationship >= 65:
        jump ending_his_shadow

    else:
        jump ending_his_shadow


## ─── Ending Branch 1 — "She Was His Shadow" ──────────────────────────────────

label ending_his_shadow:

    play music "audio/monument_shadow.ogg" fadein 2.0

    $ journal_scene28 = True

    show sabra ch5 weary at right with dissolve
    "She stood at the foot of the statue and looked up at his face — the great menacing head, the long coat, the brilliant boots — and felt, for the first time in many years, that she was exactly where she was supposed to be."

    "Beside him. As she had always been."

    "The crowd applauded. The Senators made speeches. She did not hear them."

    "She was thinking about the morning of the Run, when he had sat on that horse and the sky had been so wide it was almost incomprehensible, and she had looked at him and thought: {i}Whatever this is, I am in it.{/i}"

    "She had been right. She was in it still."

    scene bg_journal with dissolve

    sabra "{i}1931.{/i}"

    sabra "{i}They made it look like him. It's the right thing. He was what this land was — impossible, larger than life, more beautiful than practical. I was the one who kept the books.{/i}"

    scene black with fade

    stop music fadeout 3.0

    "  "

    "— THE END —"

    return


## ─── Ending Branch 2 — "She Built It Herself" ────────────────────────────────

label ending_built_herself:

    play music "audio/monument_builder.ogg" fadein 2.0

    $ journal_scene28 = True

    "The sculptor said it was the Spirit of the Pioneer. She supposed he was right."

    "She looked at the statue for a long time. The magnificent man. The high-heeled boots. The hand on the holster."

    "Not the whole story. Not even the most important part of the story."

    "She knew what she had built. This state knew it too. The paper. The school board. The water commission. The twenty-three years of editorial positions taken when it was easier to stay quiet. The oil rights hearings. The congressional seat."

    show sabra ch5 proud at right with dissolve
    "The crowd was watching her. She turned and spoke to the Senators, the editors, the oil men, the women who had come from the federation."

    "She spoke for twenty minutes without notes."

    "Afterward, a young woman from the Tulsa paper came up and asked who had taught her to write."

    sabra "No one. I had a newspaper and no choice."

    "The young woman wrote it down."

    scene bg_journal with dissolve

    sabra "{i}1931.{/i}"

    sabra "{i}They built a monument to the Pioneer. They should have built two. But I have the paper, and the paper will say what needs saying. It always has.{/i}"

    scene black with fade

    stop music fadeout 3.0

    "  "

    "— THE END —"

    return


## ─── Ending Branch 3 — "The Land Belongs to All" ─────────────────────────────

label ending_land_belongs:

    play music "audio/monument_land.ogg" fadein 2.0

    $ journal_scene28 = True

    show cim neutral at left with dissolve
    show ruby neutral at center with dissolve

    "Cim and Ruby were in the front row."

    "Their daughter — Sabra's granddaughter, who had her grandfather's gray eyes and her grandmother's black hair and Osage blood in her that made her, Sabra thought, the most interesting person she had ever produced — looked up at the statue."

    "The Indian behind Yancey. She saw it now: not stumbling. Reaching."

    "One hand reaching for the pioneer's shoulder — not for support. For something else. Something between companionship and claim. The two of them moving together, across whatever land this was, which had always been both of theirs."

    hide cim
    hide ruby

    "Sabra looked at her son's daughter, who was looking at the statue with the patient attentiveness Sabra had spent forty years learning to see."

    sabra "What do you think?"

    "The girl tilted her head."

    "\"He's big,\" she said. \"And he's holding on.\""

    "She meant the Indian. She meant the hand on the pioneer's shoulder."

    "Sabra looked at the statue again. She had not seen it that way before."

    scene bg_journal with dissolve

    sabra "{i}1931.{/i}"

    sabra "{i}Her name is Sabra, after me — but she has Cim's face and Ruby's stillness. She will outlast us all. The land belongs to her. It always did.{/i}"

    scene black with fade

    stop music fadeout 3.0

    "  "

    "— THE END —"

    return
