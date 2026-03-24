## minigame_collection.rpy
## Scene 8 mini-game: Sabra watches the Sunday church collection.
##
## How it works:
##   - 8 congregation members are shown; the collection hat passes left-to-right
##   - Hat position is derived from elapsed time (advances every 4 seconds)
##   - 3 of 8 members are secretly skimming; they show an amber "!" tell while
##     the hat is on them
##   - Click a member while the hat is on them to flag them as a cheat
##   - Score (collection_caught, 0–3) applies a community_standing bonus in script

## ─── Store variables ─────────────────────────────────────────────────────────

default collection_time_left = 30
default collection_caught    = 0
default collection_flagged   = []

## ─── Python helpers and actions ──────────────────────────────────────────────

init python:

    COLLECTION_CHEATS = (1, 3, 6)   # member indices that skim from the hat

    COLLECTION_NAMES = [
        "Elder Howe", "Pete R.",    "Mrs. Flynn", "Bart Simms",
        "Sister Oaks", "Jim Hull",  "Cal Mott",   "Rev. Barr",
    ]

    COLLECTION_SPRITES = [
        "sprites/congregation_0_neutral.png",   # Elder Howe
        "sprites/congregation_1_neutral.png",   # Pete R.
        "sprites/congregation_2_neutral.png",   # Mrs. Flynn
        "sprites/congregation_3_neutral.png",   # Bart Simms
        "sprites/congregation_4_neutral.png",   # Sister Oaks
        "sprites/congregation_5_neutral.png",   # Jim Hull
        "sprites/congregation_6_neutral.png",   # Cal Mott
        "sprites/congregation_7_neutral.png",   # Rev. Barr
    ]

    COLLECTION_CHEAT_SPRITES = {
        1: "sprites/congregation_1_cheat.png",  # Pete R.
        3: "sprites/congregation_3_cheat.png",  # Bart Simms
        6: "sprites/congregation_6_cheat.png",  # Cal Mott
    }

    class FlagMember(Action):
        """Flag the congregation member at index idx as a suspected cheat."""

        def __init__(self, idx):
            self.idx = idx

        def __call__(self):
            if self.idx not in store.collection_flagged:
                store.collection_flagged = store.collection_flagged + [self.idx]
                if self.idx in COLLECTION_CHEATS:
                    store.collection_caught += 1
                    renpy.sound.play("sfx/collection_alert.ogg", channel="sound")
                else:
                    renpy.sound.play("sfx/coin_jingle.ogg", channel="sound")
            renpy.restart_interaction()

        def get_sensitive(self):
            hat = ((30 - store.collection_time_left) // 4) % 8
            return (
                hat == self.idx
                and self.idx not in store.collection_flagged
                and store.collection_time_left > 0
            )

        def __eq__(self, other):
            return isinstance(other, FlagMember) and self.idx == other.idx


## ─── Main screen ─────────────────────────────────────────────────────────────

screen church_collection_minigame():
    modal True

    ## Countdown — fires every second; SetVariable restarts the interaction,
    ## which re-evaluates the `if collection_time_left <= 0` branch below.
    timer 1.0 repeat True action SetVariable(
        "collection_time_left",
        max(0, collection_time_left - 1)
    )

    ## Hat advances every 4 seconds — play a fabric rustle to signal movement
    timer 4.0 repeat True action Play("sound", "sfx/hat_fabric_pass.ogg")

    ## Auto-return when timer hits zero (Return() is safe in screen language)
    if collection_time_left <= 0:
        timer 0.05 action Return(collection_caught)

    ## Hat position: advances one seat every 4 seconds
    $ hat_pos    = ((30 - collection_time_left) // 4) % 8
    $ time_color = "#FF6644" if collection_time_left <= 10 else "#C4956A"

    add "#000000cc"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 10

        text "— Pass the Hat —":
            xalign 0.5
            size 36
            color "#D2691E"

        hbox:
            xalign 0.5
            spacing 20

            text "Click a member while the hat is on them if you think they are cheating.":
                size 18
                color "#C4956A"
                text_align 0.5

            text "Time: [collection_time_left]s":
                size 22
                color time_color

        ## ── Row 1: members 0–3 ────────────────────────────────────────────
        hbox:
            xalign 0.5
            spacing 8

            for i in range(4):
                $ is_hat     = (hat_pos == i)
                $ is_cheat   = (i in COLLECTION_CHEATS)
                $ is_flagged = (i in collection_flagged)

                $ slot_bg = "#2C1A0Edd"
                $ slot_bg = "#3A6060dd" if is_hat      else slot_bg
                $ slot_bg = "#AA7700dd" if (is_hat and is_cheat and not is_flagged) else slot_bg
                $ slot_bg = "#6B0000dd" if is_flagged  else slot_bg

                button:
                    xsize 250
                    ysize 360
                    padding (4, 6)
                    background slot_bg
                    hover_background "#D2691E88"
                    action FlagMember(i)

                    vbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 4

                        if is_hat:
                            add "images/sprites/hat_collection.png":
                                xalign 0.5
                        else:
                            null height 62

                        if is_hat and is_cheat and not is_flagged:
                            add Transform(COLLECTION_CHEAT_SPRITES[i], maxsize=(230, 270)) xalign 0.5
                        else:
                            add Transform(COLLECTION_SPRITES[i], maxsize=(230, 270)) xalign 0.5

                        text COLLECTION_NAMES[i]:
                            xalign 0.5
                            size 15
                            color "#A08060"
                            text_align 0.5

                        if is_flagged:
                            text "FLAGGED":
                                xalign 0.5
                                size 13
                                color "#FF4444"
                                bold True

        ## ── Row 2: members 4–7 ────────────────────────────────────────────
        hbox:
            xalign 0.5
            spacing 8

            for i in range(4, 8):
                $ is_hat     = (hat_pos == i)
                $ is_cheat   = (i in COLLECTION_CHEATS)
                $ is_flagged = (i in collection_flagged)

                $ slot_bg = "#2C1A0Edd"
                $ slot_bg = "#3A6060dd" if is_hat      else slot_bg
                $ slot_bg = "#AA7700dd" if (is_hat and is_cheat and not is_flagged) else slot_bg
                $ slot_bg = "#6B0000dd" if is_flagged  else slot_bg

                button:
                    xsize 250
                    ysize 360
                    padding (4, 6)
                    background slot_bg
                    hover_background "#D2691E88"
                    action FlagMember(i)

                    vbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 4

                        if is_hat:
                            add "images/sprites/hat_collection.png":
                                xalign 0.5
                        else:
                            null height 62

                        if is_hat and is_cheat and not is_flagged:
                            add Transform(COLLECTION_CHEAT_SPRITES[i], maxsize=(230, 270)) xalign 0.5
                        else:
                            add Transform(COLLECTION_SPRITES[i], maxsize=(230, 270)) xalign 0.5

                        text COLLECTION_NAMES[i]:
                            xalign 0.5
                            size 15
                            color "#A08060"
                            text_align 0.5

                        if is_flagged:
                            text "FLAGGED":
                                xalign 0.5
                                size 13
                                color "#FF4444"
                                bold True

        hbox:
            xalign 0.5
            spacing 30

            text "Caught: [collection_caught] / 3":
                size 22
                color "#E8D5A3"

            button:
                xsize 200
                ysize 42
                background "#2C1A0Ecc"
                hover_background "#5C3317cc"
                action Return(collection_caught)

                text "End Collection":
                    xalign 0.5
                    yalign 0.5
                    size 20
                    color "#A08060"


## ─── Result overlay ──────────────────────────────────────────────────────────

screen collection_result(caught):
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

            if caught >= 3:
                text "— Nothing Gets Past You —":
                    xalign 0.5
                    size 30
                    color "#D2691E"
                text "All three cheaters caught. The congregation takes note of Mrs. Cravat.":
                    xalign 0.5
                    size 20
                    color "#E8D5A3"
                    text_align 0.5
            elif caught >= 1:
                text "— Watchful —":
                    xalign 0.5
                    size 30
                    color "#C4956A"
                text "You caught [caught] of 3. Not bad for a first Sunday in Osage.":
                    xalign 0.5
                    size 20
                    color "#E8D5A3"
                    text_align 0.5
            else:
                text "— A Difficult Congregation —":
                    xalign 0.5
                    size 30
                    color "#A08060"
                text "None flagged. The cheaters pocket their coins and smile at you.":
                    xalign 0.5
                    size 20
                    color "#E8D5A3"
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
