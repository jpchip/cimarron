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


## ─── SCENE 24 — Cim and Ruby Big Elk ─────────────────────────────────────────

label scene24_cim_ruby:

    scene bg_cravat_kitchen with dissolve

    play music "audio/kihekah_parlor.ogg" fadein 1.0 loop

    "Ruby Big Elk had been in the house for three years."

    "She had come the summer Cim turned fifteen — a big, silent girl of about twenty-two, almost handsome, one of six children, which was a large family for an Osage. Sabra learned, months in, that the girl had already been twice married."

    show sabra ch5 neutral at right with dissolve
    show ruby neutral at left with dissolve

    sabra "What became of your husbands, Ruby?"

    ruby "One dead. One divorced."

    "She said it flat, and went on making the bed as if she had been asked about the weather."

    "She walked with a scuffling step that Sabra could not break her of. Sabra spoke to her about it once, sharply — and then discovered she was lame, the left leg slightly shorter than the right. She apologized. The girl said nothing."

    "Ruby made beds with the manner of a deposed queen. She moved about the kitchen with the pace and air of a Lady Macbeth. Her broad immobile face, her unspeaking eyes, her secret manner all worked a slow constant poison in Sabra — who, in fairness, admitted that Ruby was good to the children, fed them well, never complained about the work."

    hide ruby with dissolve
    hide sabra with dissolve

    show cim neutral at left with dissolve
    show ruby neutral at right with dissolve

    "What Sabra did not fully admit, for almost three years, was what she had been seeing with her own eyes."

    "Young Cim lingering in the kitchen. Cim at the table with his head close to Ruby's, learning Osage. Cim's face when he listened to her sing the long pulsing vowels of songs Sabra could not follow — a pulsation like a violin note sounded several times in a single bow stroke."

    cim "One more time. Slow."

    "Ruby sang. Cim tried to follow, his eyes fixed on her face, utterly absorbed."

    "Sabra had seen it. She had put it away. She had seen it again, and put it away again."

    hide cim with dissolve
    hide ruby with dissolve

    ## ── The Announcement ─────────────────────────────────────────────────────

    scene bg_kihekah_house_parlor with dissolve

    "On an afternoon in October, Sabra came home from the Wigwam to a house that was too quiet."

    show sabra ch5 worried at right with dissolve

    sabra "Cim? Ruby?"

    "No one answered. The kitchen was empty. Ruby's apron was gone from the hook behind the door. Sabra went into the stiff little front parlor — the room she almost never used — and stopped."

    show big_elk neutral at left with dissolve
    show mrs_big_elk neutral at center with dissolve

    "Big Elk and his wife were sitting in the parlor chairs."

    "They were in ceremonial dress. Big Elk's striped blanket hung regally from his shoulders; silver emblems of his former office as Chief hung at his breast; on his head was a round high cap of brown beaver with an eagle feather stuck up the back, and his long locks, hanging straight and stiff, were dyed a brilliant orange. His wife wore a cerise satin blouse and a fine bright-hued blanket; her hair was neatly braided and wound about her hatless head."

    "Sabra understood, before a word was said, that the dress was the announcement."

    "Big Elk raised one palm. The other wielded languidly, back and forth, back and forth, an enormous semicircular fan made of eagle feathers."

    big_elk "How."

    "He said nothing else. He did not speak English — a refusal he had maintained for forty years, though he understood it perfectly well. His wife spoke for him. She had attended an Indian Mission school in her girlhood; her English was broken and slovenly, from carelessness or indifference or pride."

    mrs_big_elk "Four o'clock big dinner, big dance. Your son want um come tell you."

    "Sabra's hand went to the back of a chair."

    mrs_big_elk "Want um know he marry Ruby this morning."

    "The fan went back and forth, back and forth, regally."

    ## ── Choice 1: Sabra's First Words ────────────────────────────────────────

    menu:
        "The room was very quiet. The fan went on. What does Sabra say?"

        "\"I have been employing my own daughter-in-law.\" (Recognition)":
            $ indian_sympathy    += 2
            $ ruby_welcomed       = True

            "She heard it come out of her own mouth before she had decided to say it. Three years. Three years of sharp little corrections about the grape jell and the scuffling step — and the girl on the other side of them had been the one Cim was going to marry from the beginning. Perhaps from the first week."

            sabra "I have been employing my own daughter-in-law."

            "Mrs. Big Elk smiled a strange fixed smile, like a schoolgirl's — a rare expression in her face, more frightening than a scowl. Big Elk himself showed nothing."

            "Sabra thought, with a clarity she disliked: {i}They have known this longer than I have.{/i}"

        "\"There will be no acknowledgment from this family.\" (Felice's voice)":
            $ indian_sympathy    -= 2
            $ yancey_relationship -= 5

            "Her mother's voice came up through her own throat. The bright hard tone Felice Venable had used on Cherokees and on tradesmen and, in the last years, on Yancey himself."

            sabra "There will be no acknowledgment from this family."

            "Mrs. Big Elk stopped smiling. Big Elk's eyes moved, once, and came to rest on Sabra, and did not move again. The fan went on, back and forth."

            mrs_big_elk "You come anyway. Four o'clock."

            "She said it without heat, the way one would state a timetable."

        "\"Where is my husband?\" (Postponement)":
            "Her mouth was dry. She could not look at either of them."

            sabra "Where is my husband? He should be here for this."

            mrs_big_elk "Mister Yancey come soon. Cim go tell him at the paper."

            "Sabra sat down. The cerise satin of Mrs. Big Elk's blouse seemed too bright, like something seen through fever."

    ## ── Yancey Takes It in Stride ────────────────────────────────────────────

    show yancey neutral at right with dissolve

    "Yancey came down the stairs with his quick light step. At the sight of Big Elk and his wife his look of concern changed to one of relief — as though something long expected had finally arrived."

    yancey "How, old friend."

    big_elk "How."

    "They exchanged a sentence or two in Osage. Sabra could not follow it. Yancey turned to her."

    yancey "Cim married Ruby this morning at Wazhazhe. Dinner at four. We're expected."

    "He said it the way he would have said {i}the weather is turning{/i}. Then he went to the telephone in the hall and, without waiting for her to speak, dictated the wedding announcement to Jesse Rickey at the Wigwam."

    yancey "Jesse! Take this. Get it in. Ready. Ex-Chief Big Elk, of the Osage Nation, and Mrs. Big Elk, living at Wazhazhe, announce the marriage of their daughter Ruby Big Elk to Cimarron Cravat — don't interrupt me, I'm in a hurry — son of Mr. and Mrs. Yancey Cravat, of this city. The wedding was solemnized at the home of the bride's parents and was followed by an elaborate dinner made up of many Indian and American dishes."

    "He came back into the parlor and clapped Big Elk once on the shoulder, which Big Elk permitted."

    hide yancey with dissolve
    hide big_elk with dissolve
    hide mrs_big_elk with dissolve
    hide sabra with dissolve

    ## ── At Wazhazhe ──────────────────────────────────────────────────────────

    scene bg_wazhazhe_bungalow with fade

    "Ruby's handsome head right had bought the young couple the house — a one-story red brick bungalow, substantial and ugly — just across the road from Big Elk's. It was furnished complete. Mongrel Spanish in the living room: red plush, fringe, brass nail heads as big as twenty-dollar gold pieces. An upright piano. A rose-colored taffeta spread on the bed."

    "In the kitchen sat a new hired girl — white, pale-haired, pale-eyed — hired by Ruby for Ruby's own house. Sabra felt a wave of nausea and held on."

    show cim neutral at left with dissolve
    show ruby neutral at center with dissolve

    "Ruby came toward her with that slow scuffling step — the same step she had used crossing Sabra's kitchen for three years. Only now it crossed a floor Ruby owned."

    "The two women looked at each other. Their looks clashed like swords held high."

    ## ── Choice 2: The Greeting ───────────────────────────────────────────────

    menu:
        "Ruby does not extend her hand first. Neither does Sabra. What does Sabra do?"

        "Do not offer a hand. (The distance Ferber draws)":
            $ yancey_relationship -= 2

            "She did not offer her hand. Ruby did not offer hers. They stood two feet apart, and did not shake hands, and everyone in the room saw it, and no one remarked on it."

            show ruby direct at center
            "Ruby's gaze did not falter. There was no apology in it, and no invitation."

            show big_elk neutral at right with dissolve
            mrs_big_elk "Come. Eat."

            hide big_elk

            "Sabra went through the motions of eating. Sometimes she put a morsel into her mouth and actually swallowed it."

        "Extend a formal hand. (Civil, not warm)":
            $ indian_sympathy += 1

            sabra "Ruby."

            "She put her hand out. Ruby looked at it for a moment, as though examining a strange object, then took it. The grip was firm and brief."

            "It was not a welcome. It was an acknowledgment that a transaction had occurred in the world and both of them were now obliged to act as though they had agreed to it."

        "Embrace her. (A thing she did not know she would do)":
            $ indian_sympathy    += 3
            $ yancey_relationship += 3
            $ ruby_welcomed       = True

            "She did a thing that surprised her, and probably surprised Ruby: she crossed the two feet between them and put her arms around the girl."

            "Ruby did not return the embrace. She did not refuse it, either. She stood still inside Sabra's arms the way she had stood in the kitchen when Sabra corrected her about the jelly — present, unpushing, impossible to read."

            "When Sabra stepped back, Ruby inclined her head once. It was the most the girl had ever given her."

            show yancey neutral at right with dissolve
            "Yancey, from across the room, caught Sabra's eye. He did not smile. He looked at her, steadily, as though she had finally said a thing he had been waiting twenty years to hear her say."
            hide yancey

    ## ── Ruby, Alone ──────────────────────────────────────────────────────────

    hide cim with dissolve
    show ruby direct at center with dissolve

    "Later — when the dancing was starting in the yard and Yancey was laughing with old Big Elk over a plate — Ruby came and stood beside Sabra at the window."

    "She did not look at her mother-in-law. She looked out at the dancers."

    ruby "I didn't expect it to be easy."

    sabra "No."

    ruby "It won't always be uncomfortable."

    "She said it without consolation, the way a person states a weather pattern. Then she went back to her guests."

    "Sabra found herself — unexpectedly — believing her."

    $ indian_sympathy += 1

    ## ── Journal Entry 24 ─────────────────────────────────────────────────────

    scene bg_journal with dissolve

    $ journal_scene24 = True

    sabra "{i}October, 1910.{/i}"

    sabra "{i}Ruby Big Elk has lived in my house for three years. I gave her orders about the jell and the beds. I asked her to pick up her feet. I did not see what was in front of me. This afternoon at four o'clock she became my son's wife — at her father's house, to which I had never been invited before today. I do not yet know what kind of mother-in-law I am going to become. I know what kind I have been, because I have been it for three years without knowing.{/i}"

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

    show sabra ch5 worried
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

    sabra "{i}A Senator from Pennsylvania told me Oklahoma needed a woman Governor. He said it as a joke. Men like that always say it as a joke. I find that if you wait long enough, the joke becomes the agenda.{/i}"

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
    ## Checked in order: Branch 3 → 2 → 1a → 1 (fallback)

    if indian_sympathy >= 7 and (sabra_independence >= 5 or yancey_relationship >= 50):
        jump ending_land_belongs

    elif sabra_independence >= 8 and community_standing >= 8:
        jump ending_built_herself

    elif sabra_independence <= 4 and yancey_relationship >= 65:
        jump ending_his_shadow_chosen

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


## ─── Ending Branch 1a — "She Chose the Shadow" ───────────────────────────────

label ending_his_shadow_chosen:

    play music "audio/monument_shadow_chosen.ogg" fadein 2.0

    $ journal_scene28 = True

    show sabra ch5 tender at right with dissolve
    "She stood at the foot of the statue and looked up at his face — the great menacing head, the long coat, the brilliant boots — and felt something she had not expected to feel."

    "Peace."

    "She had spent thirty years angry at him, or trying not to be, or pretending she wasn't. She had spent thirty years keeping the Wigwam alive on her own, raising his children, voting in elections he'd never bothered to show up for, watching the territory become a state while he was somewhere on the Cimarron with a new story she'd never entirely believe."

    "And she had spent thirty years choosing it. Every single time. Every letter she'd answered, every door she'd left unlocked, every night she'd pulled out the photograph from the Run and looked at it for longer than she meant to."

    show sabra ch5 happy
    "She had known what he was on the day she married him. She had known it was not sensible. She had known she would be the one who kept the house while he kept the horizon."

    "She had chosen it anyway. She would choose it again."

    "The crowd applauded. A Senator said something about the Pioneer Spirit. She did not hear it."

    "She was thinking about the way he had tipped his hat at her from the back of that horse, before the Run, when the world was still about to begin. She was thinking that she had never loved anything the way she loved that impossible, irresponsible, glorious man."

    "That this was enough. That she was enough."

    scene bg_journal with dissolve

    sabra "{i}1931.{/i}"

    sabra "{i}They made it look like him, and they were right to. He was what this land wanted to be. I was what it actually was. I am not sure those are different things. I chose him. He chose this country. The country got both of us, whether it knew it or not.{/i}"

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

    show sabra ch5 neutral at right with dissolve
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
