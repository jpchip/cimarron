## minigame_trial.rpy
## Scene 20 mini-game: Yancey presents arguments in Dixie Lee's defense.
##
## How it works:
##   Phase 1 — Select 3 of 6 argument cards; "Proceed" activates at exactly 3
##   Phase 2 — Place those 3 in slots: OPENING / MIDDLE / CLOSING
##             Click a slot to view and remove its argument
##             "Present to Jury" activates when all 3 slots are filled
##   Returns ([selected_ids], [opening_id, middle_id, closing_id]) via Return(...)
##
## State lives in store variables trial_sel, trial_ord, trial_phase
## (reset in script_chapter4.rpy before calling the screen)
##
## Outcomes applied in scene20_trial_result (script_chapter4.rpy).


## ─── Argument data ────────────────────────────────────────────────────────────

init python:

    ARGUMENTS = [
        {
            "id":    1,
            "short": "She pays taxes",
            "type":  "Legal / Equality",
            "desc":  "Equal taxation demands equal protection under law.",
            "text": (
                "Dixie Lee pays her business license fees, her property tax, and her "
                "territorial assessment the same as any merchant in Osage. The law offers "
                "equal protection to equal contributors. This court cannot apply it "
                "selectively without undermining the very foundation of civic life."
            ),
        },
        {
            "id":    2,
            "short": "Came to survive",
            "type":  "Sympathy",
            "desc":  "She built what she could with what the territory gave her.",
            "text": (
                "This woman came to the Oklahoma Territory, as every woman in this "
                "courtroom came, without inheritance, without patronage, with nothing but "
                "her own will and her own labor. She built what she could with what she "
                "had. The law was not designed to punish survival."
            ),
        },
        {
            "id":    3,
            "short": "Selective enforcement",
            "type":  "Legal / Hypocrisy",
            "desc":  "Others conduct similar trade freely — why only her?",
            "text": (
                "This statute has not been enforced against other establishments in Osage "
                "conducting similar or adjacent trade. The court is asked to apply to one "
                "woman a law it has chosen not to apply to others. That is not justice. "
                "That is a personal grievance wearing law's clothing."
            ),
        },
        {
            "id":    4,
            "short": "No jurisdiction",
            "type":  "Jurisdictional",
            "desc":  "The acts predate the statute that now prohibits them.",
            "text": (
                "The acts alleged took place prior to the incorporation of Osage under "
                "territorial statute. This court's jurisdiction does not reach backward "
                "in time to criminalize conduct that was, at the moment of its occurrence, "
                "not prohibited by any applicable law."
            ),
        },
        {
            "id":    5,
            "short": "Challenge the jury",
            "type":  "Jury Challenge",
            "desc":  "Three jurors have property interests near her establishment.",
            "text": (
                "Three members of this jury have financial interests in property adjacent "
                "to the defendant's establishment. Their verdict cannot be impartial. "
                "I move for a mistrial and a new panel — or, alternatively, that this "
                "jury be dismissed and the matter decided by the bench alone."
            ),
        },
        {
            "id":    6,
            "short": "Due process",
            "type":  "Constitutional",
            "desc":  "The Constitution is not a garment worn only by the respectable.",
            "text": (
                "No person, regardless of occupation or standing, may be deprived of "
                "liberty or property without due process of law. The prosecution has not "
                "provided sufficient notice, sufficient evidence, or sufficient cause. "
                "The Constitution is not a garment to be worn only by the respectable."
            ),
        },
    ]


## ─── Helper functions ─────────────────────────────────────────────────────────

init python:

    def get_argument(arg_id):
        """Look up an argument dict by id."""
        for a in ARGUMENTS:
            if a["id"] == arg_id:
                return a
        return None

    def trial_toggle_arg(arg_id):
        """Toggle selection of arg_id in trial_sel (max 3)."""
        if arg_id in store.trial_sel:
            store.trial_sel = [x for x in store.trial_sel if x != arg_id]
        elif len(store.trial_sel) < 3:
            store.trial_sel = store.trial_sel + [arg_id]
        renpy.restart_interaction()

    def trial_place_arg(arg_id):
        """Place arg_id in next empty slot of trial_ord."""
        if arg_id in store.trial_ord:
            return
        new_ord = list(store.trial_ord)
        for i, v in enumerate(new_ord):
            if v is None:
                new_ord[i] = arg_id
                store.trial_ord = new_ord
                renpy.restart_interaction()
                return

    def trial_clear_slot(slot_idx):
        """Clear the slot at slot_idx in trial_ord."""
        new_ord = list(store.trial_ord)
        new_ord[slot_idx] = None
        store.trial_ord = new_ord
        renpy.restart_interaction()


## ─── Slot detail overlay (Phase 2) ───────────────────────────────────────────

screen trial_slot_detail(slot_idx, arg_id):
    modal True

    $ arg = get_argument(arg_id)

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

            text "[arg['short']]":
                size 26
                color "#E8D5A3"
                bold True

            text "[arg['type']]":
                size 18
                color "#C8A860"
                italic True

            text "[arg['text']]":
                size 18
                color "#C8B890"
                text_align 0.0
                line_spacing 4

            null height 12

            hbox:
                spacing 16
                xalign 0.5

                button:
                    xsize 180
                    ysize 44
                    background "#5C1A1Acc"
                    hover_background "#8C2A2Acc"
                    action [
                        Function(trial_clear_slot, slot_idx),
                        Hide("trial_slot_detail"),
                    ]
                    text "Remove":
                        xalign 0.5
                        yalign 0.5
                        size 20
                        color "#CC8080"
                        bold True

                button:
                    xsize 140
                    ysize 44
                    background "#2A2218cc"
                    hover_background "#3A3228cc"
                    action Hide("trial_slot_detail")
                    text "Back":
                        xalign 0.5
                        yalign 0.5
                        size 20
                        color "#A08060"


## ─── Main trial minigame screen ──────────────────────────────────────────────

screen trial_arguments_minigame():
    modal True

    add "#000000cc"

    if trial_phase == 1:

        ## ── Phase 1: Select 3 of 6 ────────────────────────────────────────────

        $ can_proceed = len(trial_sel) == 3

        vbox:
            xalign 0.5
            yalign 0.08
            spacing 18

            text "— Select Arguments —":
                xalign 0.5
                size 38
                color "#D2691E"

            text "Choose 3 arguments for Yancey to present in Dixie Lee's defense.":
                xalign 0.5
                size 19
                color "#C4956A"
                text_align 0.5

            null height 2

            hbox:
                xalign 0.5
                spacing 40
                text "Selected: [len(trial_sel)] / 3":
                    size 20
                    color "#80CC80"

            null height 2

            ## Row 1 (arguments 0–2)
            hbox:
                xalign 0.5
                spacing 12

                for i in range(3):
                    $ arg    = ARGUMENTS[i]
                    $ aid    = arg["id"]
                    $ chosen = aid in trial_sel

                    button:
                        xsize 205
                        ysize 155
                        padding (12, 10)
                        background ("#1A4A1Acc" if chosen else "#1C120Acc")
                        hover_background "#3A2A18cc"
                        action Function(trial_toggle_arg, aid)

                        vbox:
                            spacing 6
                            xalign 0.0

                            text "[arg['short']]":
                                size 16
                                color "#E8D5A3"
                                bold True

                            text "[arg['type']]":
                                size 13
                                color "#C8A860"
                                italic True
                                text_align 0.0

                            text "[arg['desc']]":
                                size 12
                                color "#A8906A"
                                text_align 0.0
                                line_spacing 2

                            null height 4

                            if chosen:
                                text "SELECTED":
                                    size 12
                                    color "#80CC80"
                                    bold True

            ## Row 2 (arguments 3–5)
            hbox:
                xalign 0.5
                spacing 12

                for i in range(3, 6):
                    $ arg    = ARGUMENTS[i]
                    $ aid    = arg["id"]
                    $ chosen = aid in trial_sel

                    button:
                        xsize 205
                        ysize 155
                        padding (12, 10)
                        background ("#1A4A1Acc" if chosen else "#1C120Acc")
                        hover_background "#3A2A18cc"
                        action Function(trial_toggle_arg, aid)

                        vbox:
                            spacing 6
                            xalign 0.0

                            text "[arg['short']]":
                                size 16
                                color "#E8D5A3"
                                bold True

                            text "[arg['type']]":
                                size 13
                                color "#C8A860"
                                italic True
                                text_align 0.0

                            text "[arg['desc']]":
                                size 12
                                color "#A8906A"
                                text_align 0.0
                                line_spacing 2

                            null height 4

                            if chosen:
                                text "SELECTED":
                                    size 12
                                    color "#80CC80"
                                    bold True

            null height 6

            button:
                xalign 0.5
                xsize 280
                ysize 54
                sensitive can_proceed
                background ("#8B4513cc" if can_proceed else "#2A180Acc")
                hover_background "#D2691Ecc"
                action SetVariable("trial_phase", 2)

                text "Proceed to Ordering":
                    xalign 0.5
                    yalign 0.5
                    size 22
                    color ("#F5DEB3" if can_proceed else "#5A3A22")
                    bold True

    else:

        ## ── Phase 2: Order the 3 selected arguments ───────────────────────────

        $ can_present  = None not in trial_ord
        $ slot_labels  = ["OPENING", "MIDDLE", "CLOSING"]
        $ slot_colors  = ["#2A4A6Bcc", "#2A4A2Acc", "#6B2A2Acc"]

        vbox:
            xalign 0.5
            yalign 0.08
            spacing 18

            text "— Order Your Arguments —":
                xalign 0.5
                size 38
                color "#D2691E"

            text "Place each argument: Opening Statement — Middle — Closing Appeal.":
                xalign 0.5
                size 19
                color "#C4956A"
                text_align 0.5

            null height 2

            ## Three ordered slots
            hbox:
                xalign 0.5
                spacing 20

                for slot_idx in range(3):
                    $ slot_id  = trial_ord[slot_idx]
                    $ slot_arg = get_argument(slot_id) if slot_id else None
                    $ s_label  = slot_labels[slot_idx]
                    $ s_color  = slot_colors[slot_idx]

                    frame:
                        xsize 220
                        ysize 155
                        padding (12, 10)
                        background s_color

                        vbox:
                            spacing 8
                            xalign 0.0

                            text "[s_label]":
                                size 16
                                color "#F5DEB3"
                                bold True

                            if slot_arg:
                                button:
                                    background "#00000000"
                                    hover_background "#FFFFFF1A"
                                    xfill True
                                    action Show("trial_slot_detail",
                                                slot_idx=slot_idx,
                                                arg_id=slot_id)
                                    vbox:
                                        spacing 4
                                        xalign 0.0
                                        text "[slot_arg['short']]":
                                            size 15
                                            color "#E8D5A3"
                                            bold True
                                        text "[slot_arg['type']]":
                                            size 12
                                            color "#C8A860"
                                            italic True
                                        text "(click to remove)":
                                            size 11
                                            color "#806050"
                            else:
                                text "— empty —":
                                    size 14
                                    color "#706050"
                                    italic True

            null height 6

            text "Available:":
                xalign 0.5
                size 20
                color "#C4956A"

            hbox:
                xalign 0.5
                spacing 14

                for aid in trial_sel:
                    $ avail_arg = get_argument(aid)
                    $ is_placed = aid in trial_ord

                    button:
                        xsize 200
                        ysize 110
                        padding (10, 8)
                        sensitive not is_placed
                        background ("#2A3A2Acc" if not is_placed else "#1A1A1Acc")
                        hover_background "#3A4A2Acc"
                        action Function(trial_place_arg, aid)

                        vbox:
                            spacing 4
                            xalign 0.0

                            text "[avail_arg['short']]":
                                size 15
                                color ("#E8D5A3" if not is_placed else "#5A5A5A")
                                bold True

                            text "[avail_arg['type']]":
                                size 12
                                color ("#C8A860" if not is_placed else "#484848")
                                italic True

                            if is_placed:
                                text "PLACED":
                                    size 11
                                    color "#4A8A4A"
                                    bold True
                            else:
                                text "(click to assign)":
                                    size 11
                                    color "#806050"

            null height 6

            button:
                xalign 0.5
                xsize 280
                ysize 54
                sensitive can_present
                background ("#8B4513cc" if can_present else "#2A180Acc")
                hover_background "#D2691Ecc"
                action [Play("sound", "sfx/gavel_strike.ogg"), Return((list(trial_sel), list(trial_ord)))]

                text "Present to Jury":
                    xalign 0.5
                    yalign 0.5
                    size 22
                    color ("#F5DEB3" if can_present else "#5A3A22")
                    bold True
