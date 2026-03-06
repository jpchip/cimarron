## minigame_letters.rpy
## Scene 16 mini-game: Sabra edits letters to the editor for publication.
##
## How it works:
##   - 8 letter cards shown in 2 rows of 4; each shows sender, summary, tag
##   - Click a card to open a detail overlay with full text
##   - PRINT adds the letter to the print column (max 4); SPIKE discards it
##   - "Go to Press" activates when exactly 4 letters are printed
##   - Returns letters_printed (list of IDs) via Return(letters_printed)
##
## Outcomes applied in scene16_letters_result (script_chapter3.rpy):
##   Tags: anti-indian, pro-indian, yancey, gossip, oil, frontier, neutral

## ─── Letter data ─────────────────────────────────────────────────────────────

init python:

    LETTERS = [
        {
            "id":      1,
            "sender":  "A.J. Folsom",
            "summary": "Indian land grants are theft from honest settlers",
            "tag":     "anti-indian",
            "text": (
                "Dear Editor — I write on behalf of the many families who have worked this "
                "soil with their hands. Every acre held in trust by the Indian Nations is an "
                "acre denied to the citizens of this republic. The law must reflect the future "
                "of Oklahoma, not the sentimentalities of the past. Print this or admit your "
                "paper has chosen sides."
            ),
        },
        {
            "id":      2,
            "sender":  "Pete Pitchlyn",
            "summary": "Consolidated statehood must protect treaty rights",
            "tag":     "pro-indian",
            "text": (
                "Mrs. Cravat — Statehood is coming whether the Nations consent or not. But the "
                "form it takes is not yet settled. I urge the Wigwam to make clear: no "
                "constitution for Oklahoma is legitimate that strips the Five Tribes of the "
                "guarantees made to them in treaty. The territory was built on those promises. "
                "A state founded on their violation will not stand clean."
            ),
        },
        {
            "id":      3,
            "sender":  "Mrs. H. Wyatt",
            "summary": "Praise for the Women's Improvement Club",
            "tag":     "neutral",
            "text": (
                "To the Editor — I wish to commend the fine work of the Osage Women's "
                "Improvement Club under the leadership of Mrs. Cravat. The new lending library "
                "shelf and the school supply drive represent exactly the kind of enterprise "
                "that elevates a frontier settlement to a civilized community. This paper "
                "and its editor are a credit to Osage."
            ),
        },
        {
            "id":      4,
            "sender":  "Shanghai Wiley",
            "summary": "High praise for Yancey's cattle-drive article",
            "tag":     "yancey",
            "text": (
                "Editor — I have read your husband's piece on the last big cattle drives and "
                "I will say it plain: that is the best writing to come out of this territory "
                "since it was a territory. Yancey Cravat has a gift. The Wigwam is lucky to "
                "have him, even when he is not exactly present. Please pass along my regards "
                "and tell him Shanghai Wiley still has that unpaid poker debt on the books."
            ),
        },
        {
            "id":      5,
            "sender":  "Anonymous",
            "summary": "Rumor: Dixie Lee seen at the land office twice this week",
            "tag":     "gossip",
            "text": (
                "Dear Editor — A concerned citizen writes to note that the woman known as "
                "Dixie Lee has been observed at the territorial land office on two occasions "
                "this week, in the company of men whose business is not known to respectable "
                "Osage. We think the community deserves to know what transactions are being "
                "conducted in its name. An inquiring public awaits."
            ),
        },
        {
            "id":      6,
            "sender":  "A Ponca Farmer",
            "summary": "Reservation conditions — drought, delayed rations",
            "tag":     "pro-indian",
            "text": (
                "Mrs. Editor — I write because I do not know who else will print what I say. "
                "The rations promised by the government have not arrived. The allotment agent "
                "tells us there has been a delay. My children have been eating cornmeal for "
                "three weeks. I am not asking for sympathy. I am asking for someone to write "
                "down the facts as they are and put them before the people who might act."
            ),
        },
        {
            "id":      7,
            "sender":  "Midland Oil & Lease Co.",
            "summary": "Seeking investors — mineral rights in Osage territory",
            "tag":     "oil",
            "text": (
                "To the Editor of the Oklahoma Wigwam — Midland Oil & Lease Co. invites your "
                "readers to consider the extraordinary opportunity presented by mineral lease "
                "arrangements in the Osage hills. Our survey teams have identified formations "
                "of considerable promise. Readers interested in correspondent investment terms "
                "may write to our Guthrie office. We would also welcome a favorable notice "
                "in the Wigwam's business column."
            ),
        },
        {
            "id":      8,
            "sender":  "Name Withheld",
            "summary": "Grateful for law after the Kid's death",
            "tag":     "frontier",
            "text": (
                "Mrs. Cravat — I will not give my name but I will give you the truth. I came "
                "to this territory afraid of men like the Kid. When I heard he was dead I sat "
                "down and cried and I am not ashamed of it. I do not know your husband. But "
                "I know what it means that a man like that came through our town and left it "
                "safer than he found it. Please print this if you think it worth reading."
            ),
        },
    ]

    TAG_COLORS = {
        "anti-indian": "#8B2020",
        "pro-indian":  "#3A6B3A",
        "neutral":     "#6B5A3A",
        "yancey":      "#2F4F6F",
        "gossip":      "#6B3A6B",
        "oil":         "#4A4A2A",
        "frontier":    "#5A4A2A",
    }


## ─── Helper: look up a letter dict by id ─────────────────────────────────────

init python:

    def get_letter(letter_id):
        for l in LETTERS:
            if l["id"] == letter_id:
                return l
        return None


## ─── Detail overlay ───────────────────────────────────────────────────────────

screen letter_detail(letter_id, printed_list, spiked_list):
    modal True

    $ letter = get_letter(letter_id)
    $ is_printed = letter_id in printed_list
    $ is_spiked  = letter_id in spiked_list
    $ can_print  = len(printed_list) < 4 and not is_printed
    $ tag_col    = TAG_COLORS.get(letter["tag"], "#6B5A3A")

    add "#000000cc"

    frame:
        xalign 0.5
        yalign 0.45
        xsize 620
        padding (36, 30)
        background Frame("#100A06f0", Borders(8, 8, 8, 8))

        vbox:
            spacing 16
            xalign 0.0

            hbox:
                spacing 14
                xalign 0.0

                text "[letter['sender']]":
                    size 26
                    color "#E8D5A3"
                    bold True

                text "[letter['tag']]":
                    size 16
                    color tag_col
                    yalign 0.7

            text "[letter['text']]":
                size 18
                color "#C8B890"
                text_align 0.0
                line_spacing 4

            null height 12

            hbox:
                spacing 16
                xalign 0.5

                ## PRINT button
                button:
                    xsize 140
                    ysize 44
                    sensitive can_print
                    background (
                        "#2A5C2Acc" if can_print else "#1A2A1Acc"
                    )
                    hover_background "#3A8C3Acc"
                    action [
                        SetScreenVariable("printed_list",
                            printed_list + [letter_id] if not is_printed else printed_list),
                        Hide("letter_detail"),
                    ]

                    text "PRINT":
                        xalign 0.5
                        yalign 0.5
                        size 20
                        color ("#80CC80" if can_print else "#405040")
                        bold True

                ## SPIKE button
                button:
                    xsize 140
                    ysize 44
                    background "#5C1A1Acc"
                    hover_background "#8C2A2Acc"
                    action [
                        SetScreenVariable("printed_list",
                            [x for x in printed_list if x != letter_id]),
                        SetScreenVariable("spiked_list",
                            spiked_list + [letter_id] if letter_id not in spiked_list
                            else spiked_list),
                        Hide("letter_detail"),
                    ]

                    text "SPIKE":
                        xalign 0.5
                        yalign 0.5
                        size 20
                        color "#CC8080"
                        bold True

                ## Cancel
                button:
                    xsize 140
                    ysize 44
                    background "#2A2218cc"
                    hover_background "#3A3228cc"
                    action Hide("letter_detail")

                    text "Back":
                        xalign 0.5
                        yalign 0.5
                        size 20
                        color "#A08060"


## ─── Main letters minigame screen ────────────────────────────────────────────

screen letters_minigame():
    modal True

    ## Local state — reset on every call
    default printed_list = []
    default spiked_list  = []

    $ can_go_to_press = len(printed_list) == 4

    add "#000000cc"

    vbox:
        xalign 0.5
        yalign 0.1
        spacing 20

        text "— Letters to the Editor —":
            xalign 0.5
            size 38
            color "#D2691E"

        text "Select exactly 4 letters to print. Click a card to read the full text.":
            xalign 0.5
            size 19
            color "#C4956A"
            text_align 0.5

        null height 4

        ## Status line
        hbox:
            xalign 0.5
            spacing 40

            text "Printed: [len(printed_list)] / 4":
                size 20
                color "#80CC80"

            text "Spiked: [len(spiked_list)]":
                size 20
                color "#CC8080"

        null height 4

        ## ── Row 1 (letters 0-3) ──────────────────────────────────────────────
        hbox:
            xalign 0.5
            spacing 12

            for i in range(4):
                $ letter  = LETTERS[i]
                $ lid     = letter["id"]
                $ printed = lid in printed_list
                $ spiked  = lid in spiked_list
                $ tcol    = TAG_COLORS.get(letter["tag"], "#6B5A3A")
                $ card_bg = (
                    "#1A4A1Acc" if printed else
                    "#4A1A1Acc" if spiked  else
                    "#1C120Acc"
                )

                button:
                    xsize 180
                    ysize 140
                    padding (10, 8)
                    background card_bg
                    hover_background "#3A2A18cc"
                    action Show("letter_detail",
                                letter_id=lid,
                                printed_list=printed_list,
                                spiked_list=spiked_list)

                    vbox:
                        spacing 6
                        xalign 0.0

                        text "[letter['sender']]":
                            size 15
                            color "#E8D5A3"
                            bold True

                        text "[letter['summary']]":
                            size 13
                            color "#A8906A"
                            text_align 0.0
                            line_spacing 2

                        null height 4

                        text "[letter['tag']]":
                            size 13
                            color tcol

                        if printed:
                            text "IN PRINT":
                                size 12
                                color "#80CC80"
                                bold True
                        elif spiked:
                            text "SPIKED":
                                size 12
                                color "#CC8080"
                                bold True

        ## ── Row 2 (letters 4-7) ──────────────────────────────────────────────
        hbox:
            xalign 0.5
            spacing 12

            for i in range(4, 8):
                $ letter  = LETTERS[i]
                $ lid     = letter["id"]
                $ printed = lid in printed_list
                $ spiked  = lid in spiked_list
                $ tcol    = TAG_COLORS.get(letter["tag"], "#6B5A3A")
                $ card_bg = (
                    "#1A4A1Acc" if printed else
                    "#4A1A1Acc" if spiked  else
                    "#1C120Acc"
                )

                button:
                    xsize 180
                    ysize 140
                    padding (10, 8)
                    background card_bg
                    hover_background "#3A2A18cc"
                    action Show("letter_detail",
                                letter_id=lid,
                                printed_list=printed_list,
                                spiked_list=spiked_list)

                    vbox:
                        spacing 6
                        xalign 0.0

                        text "[letter['sender']]":
                            size 15
                            color "#E8D5A3"
                            bold True

                        text "[letter['summary']]":
                            size 13
                            color "#A8906A"
                            text_align 0.0
                            line_spacing 2

                        null height 4

                        text "[letter['tag']]":
                            size 13
                            color tcol

                        if printed:
                            text "IN PRINT":
                                size 12
                                color "#80CC80"
                                bold True
                        elif spiked:
                            text "SPIKED":
                                size 12
                                color "#CC8080"
                                bold True

        null height 8

        ## ── Go to Press ──────────────────────────────────────────────────────
        button:
            xalign 0.5
            xsize 260
            ysize 54
            sensitive can_go_to_press
            background (
                "#8B4513cc" if can_go_to_press else "#2A180Acc"
            )
            hover_background "#D2691Ecc"
            action Return(printed_list)

            text "Go to Press":
                xalign 0.5
                yalign 0.5
                size 24
                color ("#F5DEB3" if can_go_to_press else "#5A3A22")
                bold True
