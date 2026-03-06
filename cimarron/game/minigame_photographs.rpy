## minigame_photographs.rpy
## Scene 28 mini-game: Sabra selects 2 photographs from the cedar box for Krbecek.
##
## How it works:
##   - 6 photo cards shown in 2 rows of 3
##   - Click a card to open a detail overlay with caption, chapter reference, and memory
##   - SELECT marks the photo; DESELECT un-marks it (max 2 at once)
##   - "Give to Krbecek" activates when exactly 2 photos are selected
##   - State lives in store variable selected_photos (reset before calling screen)
##   - Returns selected_photos (list of 2 IDs) via Return(list(selected_photos))
##
## Outcomes applied in scene28_photos_result (script_chapter5.rpy).


## ─── Photo data ───────────────────────────────────────────────────────────────

init python:

    PHOTOS = [
        {
            "id":      1,
            "caption": "April 1889 — the morning of the Run",
            "chapter": "Chapter 1",
            "desc": (
                "Yancey on horseback, the sombrero tipped back, the prairie "
                "impossibly wide."
            ),
            "memory": (
                "The morning before everything changed. He already looked "
                "like a legend."
            ),
        },
        {
            "id":      2,
            "caption": "The first church of Osage, August 1890",
            "chapter": "Chapter 2",
            "desc": (
                "A canvas tent. A wooden cross. Twenty people on rough pine benches."
            ),
            "memory": (
                "We built this town out of canvas and stubbornness."
            ),
        },
        {
            "id":      3,
            "caption": "Editing the Wigwam, c. 1896",
            "chapter": "Chapter 3",
            "desc": (
                "Sabra at the composing table, alone. The press behind her."
            ),
            "memory": (
                "I took this myself — no, that's not right. Isaiah took it. "
                "He was learning."
            ),
        },
        {
            "id":      4,
            "caption": "Cuba, 1898 — before San Juan Hill",
            "chapter": "Chapter 4",
            "desc": (
                "Yancey in the Rough Rider uniform. Eight notches on the hat band."
            ),
            "memory": (
                "He sent this from Tampa. He was grinning. He was always grinning."
            ),
        },
        {
            "id":      5,
            "caption": "Yancey reads the service, 1898",
            "chapter": "Chapters 3–4",
            "desc": (
                "The open prairie. A mound of earth. Yancey's hat in his hands."
            ),
            "memory": (
                "He gave the Kid a proper burial. That is the part nobody "
                "wrote about."
            ),
        },
        {
            "id":      6,
            "caption": "Cim's family, c. 1912",
            "chapter": "Chapter 5",
            "desc": (
                "Cim and Ruby Big Elk, seated. Ruby is looking at the camera. "
                "Cim is not."
            ),
            "memory": (
                "Cim has his grandfather Venable's eyes and his father's "
                "inability to sit still."
            ),
        },
    ]


## ─── Helper: look up a photo dict by id ──────────────────────────────────────

init python:

    def get_photo(photo_id):
        for p in PHOTOS:
            if p["id"] == photo_id:
                return p
        return None

    def photo_toggle(photo_id):
        """Select or deselect a photo (max 2 selected at once)."""
        if photo_id in store.selected_photos:
            store.selected_photos = [x for x in store.selected_photos if x != photo_id]
        elif len(store.selected_photos) < 2:
            store.selected_photos = store.selected_photos + [photo_id]
        renpy.restart_interaction()


## ─── Detail overlay ───────────────────────────────────────────────────────────

screen photo_detail(photo_id):
    modal True

    $ photo       = get_photo(photo_id)
    $ is_selected = photo_id in selected_photos
    $ can_select  = len(selected_photos) < 2 and not is_selected

    add "#000000cc"

    frame:
        xalign 0.5
        yalign 0.45
        xsize 640
        padding (38, 32)
        background Frame("#100A06f0", Borders(8, 8, 8, 8))

        vbox:
            spacing 14
            xalign 0.0

            text "[photo['caption']]":
                size 26
                color "#E8D5A3"
                bold True

            text "[photo['chapter']]":
                size 17
                color "#C8A860"
                italic True

            null height 4

            text "[photo['desc']]":
                size 18
                color "#C8B890"
                text_align 0.0
                line_spacing 4

            null height 4

            text "[photo['memory']]":
                size 17
                color "#A09070"
                italic True
                text_align 0.0
                line_spacing 4

            null height 12

            hbox:
                spacing 16
                xalign 0.5

                ## SELECT / DESELECT button
                button:
                    xsize 180
                    ysize 44
                    sensitive (can_select or is_selected)
                    background (
                        "#1A4A1Acc" if is_selected else
                        "#2A3C2Acc" if can_select  else
                        "#1A1A1Acc"
                    )
                    hover_background ("#3A7A3Acc" if is_selected else "#3A6A3Acc")
                    action Function(photo_toggle, photo_id)

                    text ("Deselect" if is_selected else "Select"):
                        xalign 0.5
                        yalign 0.5
                        size 20
                        color ("#80EE80" if is_selected else "#80CC80" if can_select else "#405040")
                        bold True

                ## CLOSE button
                button:
                    xsize 140
                    ysize 44
                    background "#2A2218cc"
                    hover_background "#3A3228cc"
                    action Hide("photo_detail")

                    text "Close":
                        xalign 0.5
                        yalign 0.5
                        size 20
                        color "#A08060"


## ─── Main photograph box minigame screen ─────────────────────────────────────

screen photograph_box_minigame():
    modal True

    $ can_give = len(selected_photos) == 2

    add "#000000cc"

    vbox:
        xalign 0.5
        yalign 0.1
        spacing 20

        text "— The Cedar Box —":
            xalign 0.5
            size 38
            color "#D2691E"

        text "Select 2 photographs to give to Krbecek. Click a card to read the memory.":
            xalign 0.5
            size 19
            color "#C4956A"
            text_align 0.5

        null height 4

        ## Status line
        hbox:
            xalign 0.5
            spacing 40

            text "Selected: [len(selected_photos)] / 2":
                size 20
                color "#80CC80"

        null height 4

        ## ── Row 1 (photos 0–2) ───────────────────────────────────────────────
        hbox:
            xalign 0.5
            spacing 14

            for i in range(3):
                $ photo      = PHOTOS[i]
                $ pid        = photo["id"]
                $ selected   = pid in selected_photos
                $ card_bg    = "#1A4A1Acc" if selected else "#1C120Acc"

                button:
                    xsize 200
                    ysize 140
                    padding (12, 10)
                    background card_bg
                    hover_background "#2A2010cc"
                    action Show("photo_detail", photo_id=pid)

                    vbox:
                        spacing 6
                        xalign 0.0

                        text "[photo['caption']]":
                            size 15
                            color "#E8D5A3"
                            bold True
                            text_align 0.0

                        null height 2

                        text "[photo['chapter']]":
                            size 14
                            color "#C8A860"
                            italic True

                        null height 4

                        if selected:
                            text "✓ Selected":
                                size 15
                                color "#80EE80"
                                bold True

        null height 8

        ## ── Row 2 (photos 3–5) ───────────────────────────────────────────────
        hbox:
            xalign 0.5
            spacing 14

            for i in range(3, 6):
                $ photo      = PHOTOS[i]
                $ pid        = photo["id"]
                $ selected   = pid in selected_photos
                $ card_bg    = "#1A4A1Acc" if selected else "#1C120Acc"

                button:
                    xsize 200
                    ysize 140
                    padding (12, 10)
                    background card_bg
                    hover_background "#2A2010cc"
                    action Show("photo_detail", photo_id=pid)

                    vbox:
                        spacing 6
                        xalign 0.0

                        text "[photo['caption']]":
                            size 15
                            color "#E8D5A3"
                            bold True
                            text_align 0.0

                        null height 2

                        text "[photo['chapter']]":
                            size 14
                            color "#C8A860"
                            italic True

                        null height 4

                        if selected:
                            text "✓ Selected":
                                size 15
                                color "#80EE80"
                                bold True

        null height 16

        ## ── Give to Krbecek button ────────────────────────────────────────────
        button:
            xalign 0.5
            xsize 300
            ysize 54
            sensitive can_give
            background ("#4A3010cc" if can_give else "#2A1C0Acc")
            hover_background "#7A5020cc"
            action Return(list(selected_photos))

            text "Give to Krbecek":
                xalign 0.5
                yalign 0.5
                size 22
                color ("#E8C060" if can_give else "#605030")
                bold True
