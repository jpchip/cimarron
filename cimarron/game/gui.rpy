################################################################################
## gui.rpy — Complete GUI configuration for Cimarron: Chapter One.
## Custom earth-tone color palette applied over standard Ren'Py 8.x defaults.
################################################################################

init -2 python:
    gui.init(1280, 720)

## ─── Language ─────────────────────────────────────────────────────────────────
define gui.language = "unicode"

## ─── Colors ───────────────────────────────────────────────────────────────────
## Earth tones: ochre, burnt sienna, cream, dark brown.

define gui.accent_color          = "#8B4513"   # Saddle brown
define gui.idle_color            = "#A0522D"   # Sienna
define gui.idle_small_color      = "#C4956A"   # Sandy
define gui.hover_color           = "#D2691E"   # Chocolate
define gui.selected_color        = "#F5DEB3"   # Wheat
define gui.insensitive_color     = "#A08060"   # Muted tan
define gui.muted_color           = "#C4956A"   # Sandy
define gui.hover_muted_color     = "#D4B07A"

define gui.text_color            = "#F5DEB3"   # Wheat cream — readable on dark textbox
define gui.interface_text_color  = "#E8D5A3"   # Pale gold — menus and UI
define gui.sensitive_color       = "#F5DEB3"

## ─── Fonts ────────────────────────────────────────────────────────────────────
## Uncomment after placing .ttf files in game/fonts/:
define gui.text_font           = "fonts/PlayfairDisplay-Regular.ttf"
define gui.name_text_font      = "fonts/PlayfairDisplay-Bold.ttf"
define gui.interface_text_font = "fonts/IMFellEnglish-Regular.ttf"

## ─── Text Sizes ───────────────────────────────────────────────────────────────
define gui.text_size             = 26
define gui.name_text_size        = 30
define gui.interface_text_size   = 24
define gui.label_text_size       = 30
define gui.slot_button_text_size = 20
define gui.notify_text_size      = 24
define gui.title_text_size       = 56
define gui.main_menu_text_size   = 26

## ─── Textbox (Dialogue Window) ────────────────────────────────────────────────
define gui.textbox_height  = 220
define gui.textbox_yalign  = 1.0

define gui.text_xpadding   = 45
define gui.text_ypadding   = 20

define gui.dialogue_xpos   = 80
define gui.dialogue_ypos   = 80
define gui.dialogue_width  = 1100
define gui.dialogue_text_xalign = 0.0

## ─── Name Box ─────────────────────────────────────────────────────────────────
define gui.name_xpos       = 30
define gui.name_ypos       = -65
define gui.name_xalign     = 0.0
define gui.namebox_width   = 320
define gui.namebox_height  = 50
define gui.namebox_borders = Borders(14, 8, 14, 8)
define gui.namebox_tile    = False

## ─── Buttons ──────────────────────────────────────────────────────────────────
define gui.button_width    = None
define gui.button_height   = None
define gui.button_borders  = Borders(6, 6, 6, 6)
define gui.button_tile     = False

define gui.radio_button_borders  = Borders(27, 6, 6, 6)
define gui.check_button_borders  = Borders(27, 6, 6, 6)
define gui.confirm_button_borders = Borders(6, 6, 6, 6)
define gui.page_button_borders   = Borders(15, 6, 15, 6)
define gui.quick_button_borders  = Borders(15, 6, 15, 6)
define gui.navigation_button_borders = Borders(15, 6, 15, 6)
define gui.slot_button_borders   = Borders(15, 15, 15, 15)

## ─── Choice Menu ──────────────────────────────────────────────────────────────
define gui.choice_button_width      = 920
define gui.choice_button_text_size  = 24
define gui.choice_button_borders    = Borders(150, 8, 150, 8)
define gui.choice_button_tile       = False

## ─── Bars, Scrollbars, Sliders ────────────────────────────────────────────────
define gui.bar_size        = 38
define gui.bar_tile        = False
define gui.bar_borders     = Borders(6, 6, 6, 6)

define gui.vbar_borders    = Borders(6, 6, 6, 6)

define gui.scrollbar_size    = 18
define gui.scrollbar_tile    = False
define gui.scrollbar_borders = Borders(6, 6, 6, 6)

define gui.vscrollbar_borders = Borders(6, 6, 6, 6)

define gui.slider_size     = 38
define gui.slider_tile     = False
define gui.slider_borders  = Borders(6, 6, 6, 6)

define gui.vslider_borders = Borders(6, 6, 6, 6)

## ─── Frames ───────────────────────────────────────────────────────────────────
define gui.frame_borders   = Borders(6, 6, 6, 6)
define gui.frame_tile      = False

define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## ─── Game / Main Menu ─────────────────────────────────────────────────────────
define gui.main_menu_background = "images/bg_land_run.png"
define gui.game_menu_background = "#1A0E06"
define gui.game_name            = "Cimarron"

## ─── Navigation ───────────────────────────────────────────────────────────────
define gui.navigation_spacing = 4

## ─── Preferences ──────────────────────────────────────────────────────────────
define gui.pref_spacing = 15
define gui.pref_button_spacing = 0

## ─── File Slots ───────────────────────────────────────────────────────────────
define gui.file_slot_cols = 2
define gui.file_slot_rows = 4

## ─── History ──────────────────────────────────────────────────────────────────
define gui.history_spacing = 0

## ─── Skip Indicator ───────────────────────────────────────────────────────────
define gui.skip_ypos         = 15
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## ─── Notify ───────────────────────────────────────────────────────────────────
define gui.notify_ypos         = 68
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## ─── NVL ──────────────────────────────────────────────────────────────────────
define gui.nvl_borders    = Borders(0, 15, 0, 30)
define gui.nvl_height     = None
define gui.nvl_spacing    = 15
define gui.nvl_adv_transition_widget = None

## ─── About ────────────────────────────────────────────────────────────────────
define gui.about = _("{b}Cimarron: A Visual Novel{/b}\nBased on the novel by Edna Ferber (1929)\nPublic domain.")

## ─── Helper: button_properties ────────────────────────────────────────────────
## Ren'Py's gui module uses this to look up per-button-type properties.
## The defaults below match standard Ren'Py behavior.
init python:
    def _gui_button_props(kind):
        return {}
