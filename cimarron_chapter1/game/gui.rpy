## gui.rpy
## Visual theme for Cimarron: Chapter One.
## Earth tones, parchment textures, period-appropriate feel.
##
## This file overrides Ren'Py's default GUI colors.
## Replace font paths once you download fonts from Google Fonts.

## ─── Color Palette ───────────────────────────────────────────────────────────
## Dusty earth tones drawn from 1889 Oklahoma — ochre, burnt sienna, cream.

define gui.accent_color         = "#8B4513"   # Saddle brown (accent / buttons)
define gui.idle_color           = "#A0522D"   # Sienna (unselected menu items)
define gui.idle_small_color     = "#C4956A"   # Sandy (small idle text)
define gui.hover_color          = "#D2691E"   # Chocolate (hovered menu items)
define gui.selected_color       = "#F5DEB3"   # Wheat (selected items)
define gui.insensitive_color    = "#6B4423"   # Dark brown (disabled)

# Text colors
define gui.text_color           = "#2C1A0E"   # Near-black ink
define gui.interface_text_color = "#3D2010"   # Dark sepia

## ─── Dialogue Box ────────────────────────────────────────────────────────────
## Parchment-toned background for the text window.

define gui.textbox_height       = 185
define gui.textbox_yalign       = 1.0

# Background image: replace with game/gui/textbox.png (parchment texture)
# See README.md for sourcing instructions.

## ─── Fonts ───────────────────────────────────────────────────────────────────
## Default Ren'Py font is DejaVu Sans (readable but not period-appropriate).
## Download from Google Fonts and place in game/fonts/ to activate:
##
##   Narration / body text:
##     Playfair Display Regular  →  fonts/PlayfairDisplay-Regular.ttf
##
##   Character names:
##     Playfair Display Bold     →  fonts/PlayfairDisplay-Bold.ttf
##
##   UI / menus:
##     IM Fell English Regular   →  fonts/IMFellEnglish-Regular.ttf

# Uncomment these lines once the font files are in game/fonts/:
# define gui.text_font          = "fonts/PlayfairDisplay-Regular.ttf"
# define gui.name_text_font     = "fonts/PlayfairDisplay-Bold.ttf"
# define gui.interface_text_font = "fonts/IMFellEnglish-Regular.ttf"

## ─── Text Size ───────────────────────────────────────────────────────────────

define gui.text_size        = 26
define gui.name_text_size   = 30
define gui.interface_text_size = 24
define gui.label_text_size  = 30
define gui.slot_button_text_size = 20

## ─── Buttons ─────────────────────────────────────────────────────────────────

define gui.button_width     = None
define gui.button_height    = None

## ─── Choice Menu ─────────────────────────────────────────────────────────────

define gui.choice_button_width       = 920
define gui.choice_button_text_size   = 24

## ─── Window Layout ───────────────────────────────────────────────────────────

define gui.game_menu_background = "#1A0E06"   # Very dark brown
define gui.main_menu_background = "#1A0E06"

## ─── Name Box ────────────────────────────────────────────────────────────────

define gui.namebox_width    = 240
define gui.namebox_height   = None
define gui.namebox_borders  = Borders(5, 5, 5, 5)
