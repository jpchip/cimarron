################################################################################
## screens.rpy — Standard Ren'Py 8.x UI screens
## Generated boilerplate for Cimarron: Chapter One.
## Defines all required screens: say, choice, main_menu, game_menu,
## save, load, preferences, confirm, and more.
################################################################################

################################################################################
## Styles
################################################################################

style default:
    font gui.text_font
    color gui.text_color
    size gui.text_size
    language gui.language

style input:
    color gui.accent_color
    size gui.text_size
    adjust_spacing False

style hyperlink_text:
    color gui.accent_color
    hover_underline True

style gui_text:
    font gui.interface_text_font
    color gui.interface_text_color
    size gui.interface_text_size

## Base button — solid color backgrounds, no image files needed.
style button:
    padding (6, 6)
    background Frame("#2C1A0Ecc", Borders(6, 6, 6, 6))
    hover_background Frame("#8B4513cc", Borders(6, 6, 6, 6))
    selected_background Frame("#A0522Dcc", Borders(6, 6, 6, 6))
    insensitive_background Frame("#1A0E0699", Borders(6, 6, 6, 6))

style button_text is gui_text:
    color gui.interface_text_color
    hover_color gui.hover_color
    selected_color gui.selected_color
    insensitive_color gui.insensitive_color
    yalign 0.5

style label_text is gui_text:
    color gui.accent_color
    bold True

style prompt_text is gui_text:
    color gui.interface_text_color

style bar:
    ysize gui.bar_size
    left_bar Frame("#8B4513", gui.bar_borders)
    right_bar Frame("#3D2010", gui.bar_borders)

style vbar:
    xsize gui.bar_size
    top_bar Frame("#8B4513", gui.vbar_borders)
    bottom_bar Frame("#3D2010", gui.vbar_borders)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("#3D2010", gui.scrollbar_borders)
    thumb Frame("#8B4513", gui.scrollbar_borders)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("#3D2010", gui.vscrollbar_borders)
    thumb Frame("#8B4513", gui.vscrollbar_borders)

style slider:
    ysize gui.slider_size
    base_bar Frame("#3D2010", gui.slider_borders)
    thumb Frame("#8B4513", gui.slider_borders)

style vslider:
    xsize gui.slider_size
    base_bar Frame("#3D2010", gui.vslider_borders)
    thumb Frame("#8B4513", gui.vslider_borders)

style frame:
    padding gui.frame_borders.padding
    background Frame("#1A0E06e0", gui.frame_borders)


################################################################################
## Say Screen
################################################################################

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    if not renpy.variant("small"):
        add SpriteManager(update=none_update) as sm

define none_update = None

style say_window is default:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Frame("#1A0E06cc", Borders(0, 0, 0, 0))
    padding (gui.text_xpadding, gui.text_ypadding)

style say_text is default:
    color gui.text_color
    size gui.text_size
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

style namebox is default:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Frame("#2C1A0Ecc", gui.namebox_borders)
    padding gui.namebox_borders.padding

style namebox_text is default:
    color gui.accent_color
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5


################################################################################
## Input Screen
################################################################################

screen input(prompt):
    style_prefix "input"

    window:
        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default:
    xalign gui.dialogue_text_xalign
    color gui.interface_text_color
    size gui.text_size

style input is default:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


################################################################################
## Choice Screen
################################################################################

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

style choice_vbox is vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5
    spacing gui.choice_button_text_size + 10

style choice_button is default:
    padding (8, 8)
    background Frame("#2C1A0Ecc", Borders(6,6,6,6))
    hover_background Frame("#8B4513cc", Borders(6,6,6,6))

style choice_button_text is default:
    color gui.interface_text_color
    hover_color gui.hover_color
    size gui.choice_button_text_size


################################################################################
## Quick Menu Screen
################################################################################

screen quick_menu():
    zorder 100

    key "K_TAB" action ToggleVariable("quick_menu")

    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 1.0
            ypos 5
            xoffset -10

            textbutton _("Back")    action Rollback()
            textbutton _("Skip")    action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto")    action Preference("auto-forward", "toggle")
            textbutton _("Save")    action ShowMenu("save")
            textbutton _("Q.Save")  action QuickSave()
            textbutton _("Q.Load")  action QuickLoad()
            textbutton _("Prefs")   action ShowMenu("preferences")

style quick_button is default:
    padding (6, 4)
    background Frame("#2C1A0Ecc", Borders(4,4,4,4))
    hover_background Frame("#8B4513cc", Borders(4,4,4,4))

style quick_button_text is button_text:
    color gui.interface_text_color
    hover_color gui.hover_color
    size 18

init python:
    config.overlay_screens.append("quick_menu")


################################################################################
## Main Menu Screen
################################################################################

screen main_menu():
    tag menu

    style_prefix "main_menu"

    ## Full-screen background
    add gui.main_menu_background

    ## Title block — top-left, dark overlay panel behind it
    frame:
        xalign 0.0
        yalign 0.0
        xoffset 60
        yoffset 60
        background Frame("#00000099", 20, 20, 20, 20)
        padding (30, 20, 40, 20)

        vbox:
            text "CIMARRON":
                style "main_menu_title"
            text "Chapter One":
                style "main_menu_subtitle"

    ## Menu buttons — bottom-left, dark panel
    frame:
        xalign 0.0
        yalign 1.0
        xoffset 60
        yoffset -60
        background Frame("#00000099", 20, 20, 20, 20)
        padding (30, 24, 50, 24)

        vbox:
            spacing 8
            textbutton _("Start Game")  action Start()
            textbutton _("Load Game")   action ShowMenu("load")
            textbutton _("Preferences") action ShowMenu("preferences")
            textbutton _("About")       action ShowMenu("about")
            textbutton _("Quit")        action Quit(confirm=False)

style main_menu_frame is empty

style main_menu_title:
    color "#D4A84B"
    size 72

style main_menu_subtitle:
    color "#C8A87A"
    size 28

style main_menu_button is button:
    padding (0, 4, 0, 4)

style main_menu_button_text is button_text:
    size 28
    color "#E8D5B0"
    hover_color "#D4A84B"
    xalign 0.0


################################################################################
## Game Menu Screen (base for save/load/prefs/about)
################################################################################

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):
    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:
            frame:
                style "game_menu_navigation_frame"

                vbox:
                    style "game_menu_navigation_vbox"

                    if main_menu:
                        textbutton _("Return") action ShowMenu("main_menu")
                    else:
                        textbutton _("History")     action ShowMenu("history")
                        textbutton _("Save")        action ShowMenu("save")
                        textbutton _("Load")        action ShowMenu("load")
                        textbutton _("Preferences") action ShowMenu("preferences")
                        textbutton _("Main Menu")   action MainMenu()
                        textbutton _("About")       action ShowMenu("about")
                        textbutton _("Quit")        action Quit(confirm=not main_menu)

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing
                            transclude

                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude
                else:
                    transclude

    label title

    if not main_menu:
        key "game_menu" action ShowMenu("main_menu")

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is label:
    xpos 50
    ysize 120

style game_menu_label_text is label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style game_menu_navigation_vbox:
    xsize 240
    yalign 0.5
    spacing gui.navigation_spacing

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_outer_frame:
    bottom_margin 45
    top_margin 120
    xfill True
    yfill True


################################################################################
## Navigation (used inside game menus)
################################################################################

style navigation_button is gui_button
style navigation_button_text is gui_button_text:
    color gui.interface_text_color
    hover_color gui.hover_color
    size gui.interface_text_size


################################################################################
## Save / Load Screens
################################################################################

screen save():
    tag menu
    use file_slots(_("Save"))

screen load():
    tag menu
    use file_slots(_("Load"))

screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:
            order_reverse True

            button:
                style "page_label"
                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            hbox:
                style "page_button_hbox"
                xalign 0.5

                textbutton _("<") action FilePagePrevious()
                textbutton _("{#auto_page}A") action FilePage("auto")
                textbutton _("{#quick_page}Q") action FilePage("quick")

                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()

            vpgrid:
                cols 2
                yinitial 0.0

                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                side_yfill True

                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    button:
                        style "slot_button"
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

style page_label is gui_button:
    xpadding 75
    ypadding 5

style page_label_text is gui_button_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button_hbox:
    xalign 0.5

style slot_button is gui_button:
    padding (10, 10)
    background Frame("#2C1A0Ecc", Borders(6,6,6,6))
    hover_background Frame("#8B4513cc", Borders(6,6,6,6))

style slot_button_text is gui_button_text:
    color gui.interface_text_color
    size gui.slot_button_text_size

style slot_time_text:
    size gui.interface_text_size

style slot_name_text:
    size gui.interface_text_size


################################################################################
## Preferences Screen
################################################################################

screen preferences():
    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:
            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window")   action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left")    action Preference("rollback side", "left")
                    textbutton _("Right")   action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions (fast skip)") action InvertSelected(Preference("transitions", "toggle"))

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:
                    label _("Text Speed")
                    bar value Preference("text speed")

                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")

                vbox:
                    if config.has_music:
                        label _("Music Volume")
                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:
                        label _("Sound Volume")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)

                    if config.has_voice:
                        label _("Voice Volume")
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing
                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

style pref_label is label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text is label_text:
    yalign 1.0

style pref_vbox is vbox:
    xsize 338

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text:
    color gui.accent_color
    hover_color gui.hover_color
    selected_color gui.selected_color
    size gui.interface_text_size

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text:
    color gui.accent_color
    hover_color gui.hover_color
    selected_color gui.selected_color
    size gui.interface_text_size

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text:
    color gui.interface_text_color
    hover_color gui.hover_color
    size gui.interface_text_size
style slider_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text


################################################################################
## History Screen
################################################################################

define gui.history_height = 210
define gui.history_text_width = 809
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0
define gui.history_text_xpos = 259
define gui.history_text_ypos = gui.history_name_ypos
define gui.history_text_xalign = 0.0

screen history():
    tag menu

    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        for h in renpy.roll_forward_info() or []:
            window:
                style "history_window"

                has fixed:
                    yfit True

                if h.who:
                    label h.who:
                        style "history_name"
                        substitute False
                        xalign gui.history_name_xalign

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False
                    xpos gui.history_text_xpos
                    ypos gui.history_text_ypos
                    xanchor gui.history_text_xalign
                    xsize gui.history_text_width
                    min_width gui.history_text_width
                    text_align gui.history_text_xalign

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }

style history_window is empty:
    yminimum gui.history_height

style history_name is default:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width
    min_width gui.history_name_width
    text_align gui.history_name_xalign
    color gui.accent_color

style history_text is default:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign


################################################################################
## About Screen
################################################################################

define gui.about = _("{b}Cimarron: Chapter One{/b}\nBased on the novel by Edna Ferber (1929)\n\nPublic domain source text via Standard Ebooks.")

screen about():
    tag menu

    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:
            label "[config.name!t]"
            text _("Version [config.version!t]\n")
            if gui.about:
                text "[gui.about!t]\n"


style about_label is label:
    xalign 0.5

style about_label_text is label_text:
    text_align 0.5

style about_text is gui_text:
    xalign 0.5
    text_align 0.5
    layout "subtitle"


################################################################################
## Confirm Screen  (this is what replaces "yesno_prompt")
################################################################################

screen confirm(message, yes_action, no_action):
    modal True

    zorder 200

    style_prefix "confirm"

    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No")  action no_action

    key "game_menu" action no_action


style confirm_frame is gui_frame:
    background Frame("#1A0E06f0", gui.confirm_frame_borders)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt is gui_text:
    text_align 0.5
    layout "subtitle"

style confirm_prompt_text is gui_text:
    text_align 0.5
    layout "subtitle"

style confirm_button is gui_button

style confirm_button_text is gui_button_text:
    color gui.accent_color
    hover_color gui.hover_color
    size gui.interface_text_size


################################################################################
## Skip Indicator Screen
################################################################################

screen skip_indicator():
    zorder 100
    style_prefix "skip"

    frame:
        hbox:
            spacing 6
            text _("Skipping")
            text "▸▸▸"

style skip_frame is empty:
    ypos gui.skip_ypos
    background Frame("#1A0E06cc", gui.skip_frame_borders)
    padding gui.skip_frame_borders.padding

style skip_text is gui_text

style skip_triangle is skip_text:
    color gui.accent_color


################################################################################
## Notify Screen
################################################################################

screen notify(message):
    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide("notify")

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style notify_frame is empty:
    ypos gui.notify_ypos
    background Frame("#1A0E06cc", gui.notify_frame_borders)
    padding gui.notify_frame_borders.padding

style notify_text is gui_text:
    color gui.interface_text_color
    size gui.notify_text_size


################################################################################
## NVL Screen
################################################################################

screen nvl(dialogue, items=None):
    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        for d in dialogue:
            window:
                id d.window_id
                if d.who is not None:
                    window:
                        id d.namebox_id
                        style "nvl_namebox"
                        text d.who id d.who_id
                text d.what id d.what_id

        add gui.nvl_adv_transition_widget

        if items:
            vbox:
                id "nvl_menu"
                style "nvl_menu_choice_vbox"
                for i in items:
                    textbutton i.caption:
                        action i.action
                        style "nvl_menu_choice_button"

define gui.nvl_name_xpos   = 645
define gui.nvl_name_ypos   = 0
define gui.nvl_name_width  = 610
define gui.nvl_name_xalign = 1.0
define gui.nvl_text_xpos   = 675
define gui.nvl_text_ypos   = gui.nvl_name_ypos
define gui.nvl_text_width  = 610
define gui.nvl_text_xalign = 0.0
define gui.nvl_thought_xpos   = 360
define gui.nvl_thought_ypos   = 0
define gui.nvl_thought_width  = 900
define gui.nvl_thought_xalign = 0.0
define gui.nvl_button_xpos   = 675
define gui.nvl_button_xanchor = 0.0

style nvl_window is default:
    xfill True
    yfill True
    background Frame("#1A0E06e0", gui.nvl_borders)
    padding gui.nvl_borders.padding

style nvl_entry is default:
    xfill True
    ysize gui.nvl_height

style nvl_namebox is namebox:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    xsize gui.nvl_name_width
    ypos gui.nvl_name_ypos

style nvl_name is default:
    color gui.accent_color
    size gui.name_text_size
    xalign gui.nvl_name_xalign

style nvl_thought is nvl_dialogue

style nvl_text is default:
    color gui.text_color
    size gui.text_size
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign

style nvl_menu_choice_vbox is choice_vbox

style nvl_menu_choice_button is choice_button

style nvl_menu_choice_button_text is choice_button_text
