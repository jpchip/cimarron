## minigame_typesetting.rpy
## Scene 6 mini-game: Sabra sets the headline for the Oklahoma Wigwam's first edition.
##
## How it works:
##   - Scrambled letter tiles are shown in the "type case" tray
##   - Player clicks letters to move them into the composing stick (left to right)
##   - Clicking a placed letter sends it back to the tray
##   - Submit checks the result; Give Up exits with a partial outcome

## ─── Store variables ─────────────────────────────────────────────────────────

default typeset_placed    = []   # letters placed in the composing stick
default typeset_available = []   # letters still in the tray
default typeset_target    = ""   # the correct answer

## ─── Custom Actions ──────────────────────────────────────────────────────────

init python:

    class TypesetPlace(Action):
        """Move letter at tray index idx into the composing stick."""
        def __init__(self, idx):
            self.idx = idx

        def __call__(self):
            letter = store.typeset_available[self.idx]
            avail  = list(store.typeset_available)
            avail.pop(self.idx)
            store.typeset_available = avail
            store.typeset_placed    = store.typeset_placed + [letter]
            renpy.restart_interaction()

        def get_sensitive(self):
            return len(store.typeset_placed) < len(store.typeset_target)

        def __eq__(self, other):
            return isinstance(other, TypesetPlace) and self.idx == other.idx


    class TypesetRemove(Action):
        """Return placed letter at composing-stick index idx to the tray."""
        def __init__(self, idx):
            self.idx = idx

        def __call__(self):
            placed = list(store.typeset_placed)
            letter = placed.pop(self.idx)
            store.typeset_placed    = placed
            store.typeset_available = store.typeset_available + [letter]
            renpy.restart_interaction()

        def __eq__(self, other):
            return isinstance(other, TypesetRemove) and self.idx == other.idx


## ─── Screen ──────────────────────────────────────────────────────────────────

screen typesetting_minigame():
    modal True

    ## Dim the background
    add "#000000bb"

    vbox:
        xalign 0.5
        yalign 0.45
        spacing 24

        ## Title
        text "— Set the Headline —":
            xalign 0.5
            size 38
            color "#D2691E"

        text "Click a letter to place it. Click a placed letter to take it back.":
            xalign 0.5
            size 21
            color "#C4956A"

        null height 8

        ## ── Composing stick (destination) ─────────────────────────────────
        frame:
            xalign 0.5
            padding (24, 16)
            background Frame("#2C1A0Eee", Borders(6, 6, 6, 6))

            vbox:
                spacing 10
                text "COMPOSING STICK":
                    xalign 0.5
                    size 17
                    color "#A08060"

                hbox:
                    xalign 0.5
                    spacing 10

                    for i in range(len(typeset_target)):
                        if i < len(typeset_placed):
                            ## Filled slot — click to return
                            button:
                                xsize 64
                                ysize 64
                                background "#8B4513dd"
                                hover_background "#D2691Edd"
                                action TypesetRemove(i)
                                text typeset_placed[i]:
                                    xalign 0.5
                                    yalign 0.5
                                    size 38
                                    color "#F5DEB3"
                                    bold True
                        else:
                            ## Empty slot
                            frame:
                                xsize 64
                                ysize 64
                                background "#1A0E0699"
                                text "·":
                                    xalign 0.5
                                    yalign 0.5
                                    size 38
                                    color "#6B4423"

        null height 4

        ## ── Available type tray ───────────────────────────────────────────
        frame:
            xalign 0.5
            padding (24, 16)
            background Frame("#1A0E06dd", Borders(6, 6, 6, 6))

            vbox:
                spacing 10
                text "TYPE CASE":
                    xalign 0.5
                    size 17
                    color "#A08060"

                hbox:
                    xalign 0.5
                    spacing 10

                    for i, letter in enumerate(typeset_available):
                        button:
                            xsize 64
                            ysize 64
                            background "#4A2810dd"
                            hover_background "#8B4513dd"
                            action TypesetPlace(i)
                            sensitive len(typeset_placed) < len(typeset_target)
                            text letter:
                                xalign 0.5
                                yalign 0.5
                                size 38
                                color "#F5DEB3"
                                bold True

        null height 12

        ## ── Action buttons ────────────────────────────────────────────────
        hbox:
            xalign 0.5
            spacing 50

            button:
                xsize 180
                ysize 50
                background ("#8B4513cc" if len(typeset_placed) == len(typeset_target) else "#3D2010cc")
                hover_background "#D2691Ecc"
                sensitive len(typeset_placed) == len(typeset_target)
                action Return("".join(typeset_placed))
                text "Set the Type":
                    xalign 0.5
                    yalign 0.5
                    size 22
                    color "#F5DEB3"

            button:
                xsize 140
                ysize 50
                background "#2C1A0Ecc"
                hover_background "#5C3317cc"
                action Return("gave_up")
                text "Give Up":
                    xalign 0.5
                    yalign 0.5
                    size 22
                    color "#A08060"


## ─── Result overlay ──────────────────────────────────────────────────────────

screen typesetting_result(success):
    modal True

    add "#000000bb"

    frame:
        xalign 0.5
        yalign 0.45
        xsize 560
        padding (40, 32)
        background Frame("#1A0E06f0", Borders(8, 8, 8, 8))

        vbox:
            spacing 20
            xalign 0.5

            if success:
                text "— Perfect —":
                    xalign 0.5
                    size 34
                    color "#D2691E"
                text "Every letter true. The composing stick is set.":
                    xalign 0.5
                    size 22
                    color "#E8D5A3"
                    text_align 0.5
            else:
                text "— Nearly —":
                    xalign 0.5
                    size 34
                    color "#A08060"
                text "A few letters out of order. Yancey will reset them.":
                    xalign 0.5
                    size 22
                    color "#C4956A"
                    text_align 0.5

            null height 8

            button:
                xalign 0.5
                xsize 160
                ysize 46
                background "#8B4513cc"
                hover_background "#D2691Ecc"
                action Return()
                text "Continue":
                    xalign 0.5
                    yalign 0.5
                    size 22
                    color "#F5DEB3"
