## script.rpy
## Cimarron: Chapter One — Full Story Script
## Based on Cimarron by Edna Ferber (1929), public domain.
##
## Scene structure:
##   scene1_venable_home      → The Venable dinner; Yancey arrives
##   scene2_land_run          → Yancey's account of April 22, 1889
##   scene3_the_decision      → The argument; Sabra chooses to go
##   scene4_journey_west      → Wagon trail across the prairie
##   scene5_arriving_osage    → Osage: culture shock
##   scene6_oklahoma_wigwam   → The newspaper; first crisis
##   scene7_end_of_chapter    → Church in a gambling tent; epilogue

## ─── Entry Point ─────────────────────────────────────────────────────────────

label chapter1_start:
    $ renpy.block_rollback()

    scene black with fade

    "CIMARRON"
    "{i}Based on the novel by Edna Ferber{/i}"
    "Chapter One: The Land of the Fair God"

    jump scene1a_mission_visit

## ─── SCENE 1a — The Mission Visit ───────────────────────────────────────────

label scene1a_mission_visit:

    scene bg_mission_wichita with dissolve
    play music "audio/wichita_parlor.ogg" fadein 1.5 loop

    "The Mission stood at the edge of Wichita, behind its hedge of osage orange."

    show mother_bridget neutral at center with dissolve

    "Mother Bridget was among the rhubarb, cutting great rosy stalks with a garden knife, her habit hitched up over muddied shoes."

    mother_bridget "Sabra Venable. Come to say goodbye, have you."

    show sabra ch1a neutral at right with dissolve

    "It was not a question. Mother Bridget had always known things before they were said aloud."

    mother_bridget "He's going for the adventure of it. They always have, no matter what excuse they've given."

    sabra "He believes in it. The Territory."

    mother_bridget "Of course he does. That's the most dangerous kind."

    "She set down the rhubarb and wiped her hands on her apron."

    mother_bridget "When you read the history of France you're peeking through a bedroom keyhole. But here — here the women have been the real hewers of wood and drawers of water. They've done more than the men, and got less credit for it since the world began."

    menu:
        "How does she take this in?"

        "\"I want to be one of those women.\" (Frontier spirit)":
            $ sabra_direction += 2
            show sabra ch1a determined at right
            sabra "That's what I intend to be."
            mother_bridget "Well. We'll see."
            "There was no discouragement in it. Only the flat evaluation of someone who had seen intentions tested."

        "\"I want to do Yancey proud.\" (Marriage first)":
            sabra "I only want to be worthy of it — of him."
            "Mother Bridget looked at her for a long moment without speaking."
            mother_bridget "That's a start."

        "\"I'm frightened.\" (Honest)":
            $ yancey_relationship += 2
            show sabra ch1a worried at right
            sabra "I'm not sure I have what it takes."
            show mother_bridget gentle at center
            mother_bridget "Nobody does, before. That's not the thing to have beforehand."

    show sabra ch1a worried at right
    "Then it struck her — not gradually but all at once, the way cold water strikes."

    "The Territory. She did not know its roads. She did not know its weather. Yancey became suddenly remote in her mind — a stranger, terrible, belonging to it already in a way she did not."

    sabra "I couldn't go there. Not really. Could I?"

    show mother_bridget gentle at center
    mother_bridget "You already are."

    "Mother Bridget disappeared into the Mission and returned carrying something thick and folded: a coverlet woven in white and deep brilliant blue."

    mother_bridget "It's to keep you and little Cim warm, in the wagon, on the way to the Territory. Tell 'em a Kansas tapestry — the dye is Indian, nothing can fade it."

    menu:
        "Before she goes—"

        "\"Will I see you again?\"":
            $ yancey_relationship -= 1
            "She had not meant to ask it. It was not a strong woman's question."
            sabra "Will I — shall we come back?"
            mother_bridget "You'll come back when there's something to come back to. Now there isn't."
            "Sabra nodded. She understood, even if she didn't want to."

        "\"Tell me it will be all right.\"":
            sabra "Just — tell me it will be all right."
            show mother_bridget gentle at center
            mother_bridget "It'll be all right. There's no such thing as a new country for the people who come to it. They bring along their own ways and their own bits of things and make it like the old as fast as they can."
            "She believed it then. She didn't know if she was supposed to, but she did."

        "\"Thank you.\" (Take the blanket and go)":
            $ sabra_direction += 1
            show sabra ch1a neutral at right
            sabra "Thank you, Mother Bridget."
            "She took the blanket. It was heavier than it looked."
            mother_bridget "It's a practical thing."

    hide mother_bridget with dissolve
    hide sabra

    "She walked back down the Kihekah road with the blanket over her arm and her eyes wet."

    "The Mission receded behind the osage hedge."

    $ journal_scene1a = True
    call journal_entry("SCENE 1a", "Mother Bridget gave me a blue blanket for the wagon. She said there's no such thing as a new country — people just make it into the old one as fast as they can. I wonder if that is comfort or warning. I am carrying half of Wichita in this trunk and I suspect she knows it.") from _call_journal_scene1a

    jump scene1_venable_home

## ─── SCENE 1 — The Venable Home ──────────────────────────────────────────────

label scene1_venable_home:

    scene bg_venable_home with dissolve
    play music "audio/wichita_parlor.ogg" fadein 1.5 loop

    "Wichita, Kansas. A Sunday in the spring of 1889."

    "All the Venables sat at Sunday dinner — those handsome, high-bred faces turned as one toward the man at the far end of the table."

    "Yancey Cravat. Six feet two in his boots. A great shock of black hair sweeping back from a brow that belonged on a Shakespeare bust. Eyes of a swimming gray-green. A Prince Albert coat that might have been slept in."

    "He was talking."

    show yancey neutral at left with dissolve
    show yancey passionate

    yancey "And you should have seen them, I tell you — fifty thousand souls lined up along the border at the stroke of noon on April twenty-second, eighteen-eighty-nine. Ready to race into two million acres of the finest land on God's green earth."

    show sabra ch1a neutral at right with dissolve

    "Sabra Cravat watched her husband from her place at the table. Twenty-one years old. Dark and quiet and fine, like a figure in a daguerreotype. She had heard this story before. She would hear it a hundred times more. And still it made her heart quicken."

    "How does Sabra respond to Yancey's retelling?"

    menu:
        "Wide-eyed admiration — she leans forward, hanging on every word.":
            $ yancey_relationship += 10
            $ sabra_direction += 1
            sabra "Tell them about the woman on the black thoroughbred, Yancey."
            yancey "Ah — you remember the best part."
            "A warmth passed between them. In that moment, sitting among her mother's people, Sabra felt briefly that she and Yancey were the only two real people in the room."

        "Quiet skepticism — she has heard this story too many times.":
            $ yancey_relationship -= 5
            $ sabra_direction -= 1
            sabra "{i}He tells it a little differently every time.{/i}"
            "She said it only to herself — her lips did not move. But Cousin Dabney Venable, peeling an orange, gave her a sly sidelong look, as if he had heard anyway."

        "Polite reserve — she listens without expression, giving nothing away.":
            sabra "Mm."
            "She kept her face smooth as still water. Whatever she thought of Yancey's theatrics, she had learned that the Venables were always watching, always cataloguing, always ready to file a verdict."

    yancey "Fifty thousand people, all of them hungry — for land, for a new life, for a second chance. The Sooners tried to creep in the night before. The cavalry rode them off. And then — noon struck."

    show felice neutral at center with dissolve

    felice "And you were among those fifty thousand, I suppose, Yancey."

    yancey "I was, Mrs. Venable. I staked a claim in the new town of Osage, in the Oklahoma Territory."

    felice "And then gave it away, as I understand the story."

    "The temperature at the table dropped several degrees."

    $ journal_scene1 = True
    call journal_entry("SCENE 1", "He arrived like weather. One moment the parlor was simply a parlor — Mama's china, the decanters, Cousin Dabney with his orange. And then Yancey was in it, and everything shifted. I have been married to him two years and he still does this to a room. And, I confess, to me.") from _call_journal_scene1

    jump scene2_land_run

## ─── SCENE 2 — The Land Run Flashback ───────────────────────────────────────

label scene2_land_run:

    scene bg_land_run with dissolve

    "Yancey rose from the table — he always rose when a story demanded it — and the room seemed to shrink around him."

    show yancey neutral at center with dissolve

    yancey "I had my claim picked out. Good land. High ground above the Canadian River. I was going to call it — well, it doesn't matter what I was going to call it."

    "He paused. Something moved behind his gray-green eyes."

    show yancey passionate
    yancey "There was a woman. She came out of nowhere on the finest black thoroughbred I have ever seen — a woman in black tights, bold as you please, riding like a Comanche. She had staked the same claim. She had been there before me."

    "He smiled — that slow, helpless smile that Sabra had never been able to resist."

    show yancey tender
    yancey "So I gave it to her."

    show felice neutral at right with dissolve

    felice "You gave away our land."

    yancey "Her need was greater than mine, Mrs. Venable. She was a woman alone in the Territory. I am a man who can make his fortune anywhere."

    "What does Sabra think of this?"

    menu:
        "She admires the gesture — he is a true romantic.":
            $ yancey_relationship += 10
            $ sabra_direction += 1
            $ sabra_admires_yancey = True
            sabra "{i}That was like him. That was exactly like him.{/i}"
            "She thought it fiercely, as though daring anyone at the table to say otherwise. This was the Yancey she had married — this impossible, magnificent man."

        "She finds it reckless — beautiful, but reckless.":
            $ yancey_relationship -= 5
            $ sabra_direction -= 1
            sabra "{i}Beautiful. And completely impractical.{/i}"
            "She said it only to herself, and was ashamed a moment later. It was beautiful. She just wished beauty came a little cheaper."

        "She feels a complex mix — admiration and dread together.":
            $ yancey_relationship += 5
            sabra "{i}What will become of us, then?{/i}"
            "She did not say it aloud. But the question was there, underneath everything, like bedrock."
            "She loved him for giving the claim away. She was also terrified of what it meant."

    hide felice

    yancey "There is more land in the Territory than any one family could ever need. The town of Osage — I know the men who are building it. A newspaper is what it needs. A voice. And I am going to give it one."

    "He looked at Sabra then — just at her — the way he sometimes did, as if the two of them were alone in a great open field."

    yancey "The {i}Oklahoma Wigwam{/i}. That's what we'll call it."

    $ journal_scene2 = True
    call journal_entry("SCENE 2", "He gave his claim away to a woman on a black thoroughbred. A stranger. He doesn't even know her name. I have been sitting with this fact for an hour. I cannot decide if it is the most magnificent thing I have ever heard, or the most maddening. Possibly both. Probably both.") from _call_journal_scene2

    jump scene3_the_decision

## ─── SCENE 3 — The Decision ──────────────────────────────────────────────────

label scene3_the_decision:

    scene bg_venable_home with dissolve

    "After dinner, the storm broke."

    show felice commanding at left with dissolve
    show sabra ch1a neutral at right with dissolve

    felice "I forbid it. You do not know what you are talking about. Wild Indians. Rattlesnakes. Outlaws and desperadoes. No decent society. No schools, no churches—"

    yancey "We'll build them."

    felice "You'll be scalped before you can build a doghouse."

    show lewis neutral at center with dissolve

    lewis "Felice. You might recall that your own mother said much the same thing, when you came West with me twenty years ago."

    show felice neutral

    felice "That was different. Sabra's different."

    lewis "No, she isn't. Look at her."

    "The entire Venable eye — it seemed to work as a single mechanism — swung toward Sabra."

    "She stood very straight. The child Cim was on her hip. Her chin was up."

    "She was her mother, twenty years ago. She was every woman who had ever gone West."

    "What does Sabra do?"

    menu:
        "Confront her mother — stand her ground openly.":
            $ yancey_relationship += 5
            $ sabra_direction += 2
            $ sabra_confronted_mother = True
            show sabra ch1a determined
            show felice commanding
            sabra "I will go, Mamma."
            felice "You won't."
            sabra "I will."
            show felice neutral
            "The older woman's iron met the younger woman's iron. And the older woman's bent — just slightly — for the first time in twenty years."
            "Something shifted permanently in that moment. Sabra felt it."

        "Stand silently behind Yancey — let him speak for her.":
            $ yancey_relationship += 10
            $ sabra_direction -= 1
            "Sabra said nothing. She moved to stand at Yancey's side — quietly, deliberately — and the gesture spoke louder than any word."
            yancey "We'll start Monday week. Fresh and fair."
            felice "Then you are both fools."
            yancey "Possibly. But we are fools who are going."

        "Express private doubts while outwardly complying.":
            $ yancey_relationship -= 5
            $ sabra_direction -= 2
            sabra "Yes, Mamma."
            "She said it to quiet the room. But alone inside herself, Sabra Venable Cravat thought: {i}I am afraid. I am so afraid. And I do not know if that makes me sensible or a coward.{/i}"
            "She went, because she had said she would go. Because Yancey was her husband. Because she was twenty-one and the world had not yet taught her how heavy a word {i}frontier{/i} really was."

    hide felice
    hide lewis

    yancey "Week from Monday. Two wagons. One for the printing outfit, one for the household things. We'll make it in nine days, God willing."

    "He tossed Cim up in the air — once, twice — and the child shrieked with delight."

    show yancey passionate
    yancey "We'll leave all the goddamned middle-class respectability of Wichita, Kansas, behind us."

    play sound "sfx/crash_china.ogg"
    "Somewhere above, there was a crash. Black Isaiah — who had been eavesdropping from atop the sideboard — had fallen directly into Felice Venable's finest frosted silver cake."

    "In the commotion that followed, Sabra thought: {i}Well. It is decided, then.{/i}"

    $ journal_scene3 = True
    call journal_entry("SCENE 3", "We are going to Oklahoma Territory. I have said it aloud and I cannot unsay it. Yancey is already planning the newspaper. I am already planning what linens to pack. Perhaps that is the difference between us.") from _call_journal_scene3

    jump scene4_journey_west

## ─── SCENE 4 — The Journey West ──────────────────────────────────────────────

label scene4_journey_west:

    scene bg_wagon_trail with dissolve
    play music "audio/frontier_theme.ogg" fadein 2.0 loop

    "A Monday in spring. The wagons lurched away from the white house on the elm-shaded street, and Sabra did not look back."

    "She had meant to. She had planned on it — one last romantic glance at her mother's garden, the yellow and purple flags coming up through the flower beds. But Cim was shouting 'Giddap!' at the top of his lungs, and the horses needed minding, and by the time she thought of it, Wichita was gone."

    "The land changed when they crossed into Oklahoma. Abruptly and completely."

    "Red clay as far as the eye could see. The rivers ran rust-colored. The sky was a brazen sheet of tin."

    show yancey neutral at left with dissolve

    yancey "Oklahoma. From the Choctaw — {i}okla{/i}, people. {i}humma{/i}, red. The Red People's land."

    "He said it with something like reverence."

    show sabra ch1a neutral at right with dissolve

    "At midday, they stopped beside a grove of cottonwoods to eat and water the horses. Yancey came and sat beside Sabra on the wagon tongue."

    yancey "Are you frightened?"

    "How does Sabra answer?"

    menu:
        "\"Not at all\" — she opens up to his dream.":
            $ yancey_relationship += 10
            $ sabra_direction += 2
            sabra "Ask me again in a week."
            yancey "Ha! That's honest."
            "He laughed — his great, full-throated laugh — and Sabra felt something in her loosen, just slightly. Like the first button on a very tight boot."
            "She let herself look at the red land. At the enormous sky. {i}It is extraordinary,{/i} she thought. {i}And I am here.{/i}"

        "\"Yes\" — she stays guarded but truthful.":
            $ yancey_relationship += 5
            $ sabra_direction -= 1
            show sabra ch1a worried
            sabra "Terrified, if you want the truth."
            yancey "Good. That means you're paying attention."
            "He said it gently — not dismissively. And for a moment she felt that he saw her, the real her, the one behind the cheviot jacket and the gray straw bonnet."

        "She deflects — changes the subject to practical matters.":
            $ sabra_direction -= 2
            sabra "Will there be a doctor in Osage?"
            yancey "There will be everything, in time."
            sabra "And in the meantime?"
            "He grinned. 'In the meantime, we improvise.' She was not entirely comforted."

    play sfx "sfx/wind_howl.ogg" fadein 2.0 loop
    "That night, camped under a sky that went on forever, Sabra lay awake listening to coyotes."

    "Isaiah, who had been found rolled in a carpet in the back of the wagon, was already one of them. He tended Cim like a devoted sheepdog."

    "The boy slept with his fists curled under his chin, dreaming — Yancey said — of buried Spanish gold."

    "Yancey sat by the fire, writing."

    sabra "What are you writing?"

    yancey "The first editorial for the {i}Oklahoma Wigwam{/i}. I write it in my head every night."

    "He looked up at her across the fire. His face in the firelight was all planes and shadows, like a face on a coin."

    show yancey passionate
    yancey "Oklahoma will be the last, best chance America has. The other states were built on the mistakes of men who did not know better. We will know better. We will build something — different."

    "She watched him write. The fire snapped. The coyotes sang."

    sabra "I hope you're right."

    stop sfx fadeout 2.0

    $ journal_scene4 = True
    call journal_entry("SCENE 4", "We have been three days on the road. The country is red and enormous and I confess it has a certain terrible beauty. Yancey says we are making history. I am making biscuits over a campfire and trying not to burn them. Perhaps these are the same thing.") from _call_journal_scene4

    jump scene5_arriving_osage

## ─── SCENE 5 — Arriving at Osage ────────────────────────────────────────────

label scene5_arriving_osage:

    scene bg_osage_tent_town with dissolve

    "Osage, Oklahoma Territory."

    "It was not what she had imagined."

    "She had imagined — what? A raw village, certainly. Rough. But she had also imagined something purposeful, something being built. And yes, it was being built — but in the middle of the building it was also drinking, and gambling, and shooting, and cooking over open fires in the street, and hollering across wagon tops, and a brass band playing something unidentifiable under a canvas awning."

    "Mud. Red mud everywhere. Her beautiful high-buttoned shoes disappeared into it at the first step."

    "Tents. Shacks. One solid-looking structure of raw lumber. And then — a hardware store, a dry goods emporium, and between them, half-hidden, a small man in a black coat standing very still, watching the street with sad, knowing eyes."

    show sol neutral at right with dissolve

    sol "Mr. Cravat."

    show yancey neutral at left with dissolve

    yancey "Sol! Sol Levy. By God, you beat me here."

    sol "I beat almost everyone here, Mr. Cravat. That is how commerce works."

    "He looked at Sabra with a small, careful bow."

    sol "Mrs. Cravat. Welcome to Osage."

    show sabra ch1a neutral at center with dissolve

    show sabra ch1a worried
    sabra "Mr. Levy. Is it — always like this?"

    sol "Like what, Mrs. Cravat?"

    sabra "So... loud."

    sol "Only during the day. At night it is loud and dark."

    "His face was impassive. It might have been a joke."

    hide sol

    "Sabra was still processing the smell of the place — wood shavings, horse dung, frying meat, something unidentifiable but vigorous — when a rough hand grabbed her arm."

    show stranger neutral at right with dissolve

    stranger "Hey there, pretty lady. You lost? You lookin' for someone?"

    "The man was enormous, sunburned to mahogany, with a beard like a buffalo robe. He smelled of whisky and optimism."

    "What does Sabra do?"

    menu:
        "Stand her ground — look him in the eye and refuse to be intimidated.":
            $ yancey_relationship += 5
            $ sabra_direction += 3
            $ sabra_helped_frontier_char = True
            show sabra ch1a determined
            sabra "I am not lost. I am exactly where I intend to be."
            "The man blinked. Then — to her astonishment — he grinned."
            show stranger grinning at right with dissolve
            stranger "Ha! Good answer, ma'am. Good answer. Welcome to Osage."
            "He touched the brim of his hat and moved on."
            "Sabra's heart was hammering. But her face had not moved. She filed that small victory away for future use."

        "Call for Yancey — let him handle it.":
            $ sabra_direction -= 2
            sabra "Yancey!"
            "He was there in three steps, all six feet two of him, and the stranger melted back into the crowd with a murmured apology."
            "She was grateful. She was also, privately, annoyed at herself. {i}This is going to have to stop,{/i} she thought."

        "Ignore him completely — fix her gaze on the horizon and walk past.":
            $ sabra_direction += 1
            "She walked past him as though he were a fence post."
            "Afterward she was not sure if this was bravery or simply the paralysis of shock."
            "The man laughed — not unkindly."
            stranger "Spunky! I like 'em spunky!"

    hide stranger

    "That night they slept in the wagon. In the morning, Yancey found them a tent."

    "Osage, Oklahoma Territory. Population: rising. Mud: unlimited. Possibilities: enormous."

    "Sabra Cravat looked at what was to be her home and thought, carefully and completely: {i}Well.{/i}"

    $ journal_scene5 = True
    call journal_entry("SCENE 5", "We have arrived. I do not know what I expected. I know that this was not it. And yet — there is something in the air here, some electric impossibility, as though the whole place knows it is becoming something and cannot quite believe its luck. I find I cannot entirely hate it. I will not tell Mamma that.") from _call_journal_scene5

    jump scene6_oklahoma_wigwam

## ─── SCENE 6 — Building the Oklahoma Wigwam ──────────────────────────────────

label scene6_oklahoma_wigwam:

    scene bg_wigwam_office with dissolve

    "The press went up in a tent at the end of what would eventually be called Cherokee Street."

    "It was not a beautiful tent. It was not a beautiful press. But it was theirs."

    show yancey neutral at left with dissolve
    show sabra ch1a neutral at right with dissolve

    yancey "Here. The case rack goes there. The rollers here. And the press — right in the middle, where the light is best."

    "He moved through the tent like a man arranging a throne room."

    sabra "The light from a tent is not particularly good."

    yancey "It's the best light in Osage. I checked."

    "She looked at the type cases with their tiny pigeonholes of lead letters. She had watched typesetters at her father-in-law's paper years ago. She had even, as a girl, set a few lines of type herself."

    yancey "Do you remember how to set type?"

    sabra "I remember enough."

    yancey "Good. Because I need a compositor and I can't afford to hire one."

    "She pulled on her apron and looked at the scattered lead letters in the type case. Five of them, pulled out and waiting: the name of the town that was now her home."

    yancey "Start with the headline. The name of the town — O, S, A, G, E. Simple enough."

    "Simple enough. She picked up the composing stick."

    ## ── Typesetting mini-game ─────────────────────────────────────────────
    $ typeset_target    = "OSAGE"
    $ typeset_placed    = []
    $ typeset_available = ["G", "E", "S", "O", "A"]

    call screen typesetting_minigame
    $ typeset_result = _return

    if typeset_result == "OSAGE":
        $ sabra_direction += 2
        $ sabra_stood_firm_danger = True
        call screen typesetting_result(True)
        sabra "There."
        yancey "Perfect. Every letter true."
        "He looked at her with something new in his expression — a kind of pleased surprise, as if he had just remembered something he'd always known."
        sabra "It's not so different from embroidery, really. Each piece in its proper place."
        yancey "Ha! Don't tell the pressmen that. They'll never forgive you."
    else:
        call screen typesetting_result(False)
        "She had the letters almost right. Yancey reached past her without a word and shifted two of them."
        yancey "Like this. The eye reads left to right — so the type must be set left to right, exactly."
        sabra "I'll remember."
        yancey "You will. In about twenty minutes you won't be able to stop yourself."
        "He was right."
    ## ── End mini-game ─────────────────────────────────────────────────────

    play sfx "sfx/printing_press.ogg" fadein 1.0 loop
    "They worked through the afternoon. Yancey wrote. Sabra set type. Outside, Osage made its various noises."

    stop sfx fadeout 0.5
    play sound "sfx/gunshot.ogg"
    "Then: a shot."

    "And then: shouting."

    yancey "Stay here."

    "He was through the tent flap before she could answer."

    "Sabra stood very still beside the press."

    "What does Sabra do?"

    menu:
        "Go to the tent door and look — she will know what is happening.":
            $ yancey_relationship += 5
            $ sabra_direction += 2
            $ sabra_stood_firm_danger = True
            "She went to the tent flap and pulled it aside an inch."
            "A man lay in the street. Another man stood over him with a pistol. A crowd was forming — but at a careful distance."
            "She watched until she found Yancey in the crowd, that dark head above the rest. He was talking to the man with the gun."
            "Quietly. Hands out. Voice calm."
            "The pistol went down."
            "She let out a breath she hadn't known she was holding."
            sabra "Good man."
            "She went back to setting type. Her hands shook slightly. She set type anyway."

        "Stay at the press and keep working — she will not be frightened from her work.":
            $ sabra_direction += 3
            $ sabra_stood_firm_danger = True
            "She picked up the composing stick and went on setting type."
            "Her hands were steady. She was mildly surprised."
            "The shouting rose, peaked, subsided. When Yancey came back, she had set twenty lines."
            yancey "A quarrel over a lot. Nobody killed. Nobody even hurt badly."
            sabra "I finished the headline. And the subhead."
            "He looked at her — really looked at her."
            yancey "Good girl."
            "She did not tell him her hands had been shaking."

        "Go to find Yancey — she will not wait helplessly.":
            $ yancey_relationship -= 5
            $ sabra_direction += 1
            "She went after him."
            "In the street she found a scene of total confusion: two men, a crowd, a gun, and her husband in the middle of it all."
            "He saw her. His expression flashed from concern to something harder."
            yancey "I said stay inside."
            sabra "And I chose not to."
            "He held her gaze for a long moment. Then turned back to the business of peacemaking."
            "She had not helped. She had not hurt. But she had not waited, and that counted for something."

    show yancey neutral at left

    yancey "The first edition of the {i}Oklahoma Wigwam{/i} will publish Friday."

    "He was ink-stained and pleased with himself and completely alive."

    "He read her the first editorial aloud, standing in the middle of the tent with the press behind him:"

    show yancey passionate
    yancey "'{i}We come not as conquerors but as builders. We come to a land that has known injustice and knows it still, and we come swearing that this new commonwealth shall be different — that its laws shall be equitable, its courts honest, its press free. The Oklahoma Wigwam will print the truth as it finds it, the whole truth and nothing beside it, so help us God.{/i}'"

    "Silence."

    "Sabra looked at him."

    show sabra ch1a worried
    sabra "They might shoot you for that."

    show yancey neutral
    yancey "They might."

    "He was grinning."

    sabra "You're looking forward to it."

    show yancey tender
    yancey "Not the shooting part. The writing part."

    show sabra ch1a neutral
    "She shook her head. She was trying not to smile."

    $ journal_scene6 = True
    call journal_entry("SCENE 6", "The first issue of the Wigwam will print Friday. I set half the type myself. My fingers are black with ink and my back aches and I find I do not mind at all. There was a shooting in the street today. I am making a list of things I have survived that I did not think I could survive. It is becoming a long list.") from _call_journal_scene6

    jump scene7_end_of_chapter

## ─── SCENE 7 — End of Chapter One ───────────────────────────────────────────

label scene7_end_of_chapter:

    scene bg_osage_tent_town with dissolve
    play music "audio/wichita_parlor.ogg" fadein 2.0 loop

    "Sunday morning."

    "The church service was held in the largest tent in Osage, which happened to be the Silver Dollar Saloon. The tables were pushed back. The bottles were hidden, more or less. Someone had found a hymnal."

    "Sabra sat in a folding chair with Cim on her lap, listening to a circuit preacher deliver a sermon of considerable passion and limited grammar about the blessings of a new country."

    "She looked around at the congregation."

    "Gamblers. Land speculators. Merchants. Cowboys. A scattering of women. Sol Levy sat in the far corner, quiet and a little apart, as he always was."

    "Isaiah sat beside Cim and kept him from wriggling."

    "Yancey stood at the back."

    "He always stood at the back."

    scene bg_wigwam_office with dissolve

    "That evening, when Cim and Isaiah were asleep, Sabra sat at the little table they'd set up beside the press and wrote a letter."

    show sabra ch1a neutral at center with dissolve
    show sabra ch1a weary

    "She wrote it to her mother."

    "She wrote about the tent. The mud. The red clay that got into everything — their food, their shoes, their lungs."

    "She wrote about the church service in the saloon, and how the preacher's voice had cracked on the high notes of 'Rock of Ages,' and how the cowboys had sung along."

    "She wrote about the first edition of the {i}Oklahoma Wigwam{/i}, which had sold forty-two copies in a single afternoon."

    "She wrote about Cim, who had announced that he was going to be an Indian when he grew up."

    "She did not write about the shooting."

    "She did not write about being frightened."

    "She ended the letter with the words she always ended letters with: {i}Your devoted daughter, Sabra.{/i}"

    "Then she folded it, sealed it, and set it aside to post in the morning."

    "She blew out the lamp."

    "In the dark, the tent was very quiet. Yancey's breathing was even and deep. Outside, a coyote called once, and was answered."

    "Oklahoma Territory. April, 1889."

    "The world Sabra Cravat had known was exactly nine days' drive behind her."

    "The world she was making was right here, in this tent, in this mud, in this red impossible country."

    "She was not sure yet what she thought of it."

    "But she was here. And she had not flinched."

    "That would have to do, for now."

    hide sabra

    $ journal_scene7 = True
    call journal_entry("SCENE 7", "Dear Mamma, I am well. The tent is not as cold as I feared. Yancey has sold forty-two papers. Cim has decided he is an Indian. I set type today and I was good at it. I miss the elm trees and your garden. I do not miss being told what to feel. I will write again soon. Your devoted daughter, Sabra.") from _call_journal_scene7

    scene black with dissolve

    "— End of Chapter One —"

    call chapter_summary from _call_chapter_summary

    return

## ─── CHAPTER SUMMARY ─────────────────────────────────────────────────────────

label chapter_summary:

    scene black

    "CHAPTER ONE COMPLETE"
    " "
    "— Your Story So Far —"
    " "

    if yancey_relationship >= 65:
        "YANCEY & SABRA: Deeply trusting. He confides in her; she believes in his vision."
    elif yancey_relationship >= 35:
        "YANCEY & SABRA: Balanced. There is warmth, and there is distance. The marriage is real."
    else:
        "YANCEY & SABRA: Strained. Sabra follows, but she follows alone, inside."

    " "

    if sabra_direction >= 3:
        "SABRA'S PATH: Frontier Woman. She is becoming someone her mother would not entirely recognize."
    elif sabra_direction <= -3:
        "SABRA'S PATH: Refined Lady. She carries Wichita with her like a shield. It may serve her, or not."
    else:
        "SABRA'S PATH: Undecided. She is between two worlds, and has not yet chosen."

    " "

    if sabra_confronted_mother:
        "She stood up to her mother. The iron in her was tested and held."
    if sabra_admires_yancey:
        "She believes in Yancey's impossible idealism, even when she cannot afford to."
    if sabra_helped_frontier_char:
        "She met the frontier on its own terms, and did not look away."
    if sabra_stood_firm_danger:
        "When danger came, she held her ground."

    " "
    "The territory does not wait. Neither does she."

    jump chapter2_start

## ─── JOURNAL ENTRY SUBROUTINE ────────────────────────────────────────────────

label journal_entry(scene_name, entry_text):
    ## Displays a journal page overlay at the end of each scene.
    ## Call with:  call journal_entry("SCENE N", "text here")

    scene bg_journal with dissolve

    "[scene_name] — SABRA'S JOURNAL"
    " "
    "[entry_text]"
    " "
    "— S.C."

    return
