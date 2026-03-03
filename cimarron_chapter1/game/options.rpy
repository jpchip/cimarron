## options.rpy
## Ren'Py project configuration for Cimarron: Chapter One.

## ─── Game Basics ─────────────────────────────────────────────────────────────

define config.name = "Cimarron: Chapter One"

# Version string shown in the launcher.
define config.version = "0.1.0"

# If True, the game will save automatically at the start of each scene.
define config.has_autosave = True

## ─── Window / Screen ─────────────────────────────────────────────────────────

define config.screen_width  = 1280
define config.screen_height = 720

## ─── Transitions ─────────────────────────────────────────────────────────────

define config.enter_transition  = dissolve
define config.exit_transition   = dissolve
define config.intra_transition  = dissolve
define config.after_load_transition = None

## ─── Text and Fonts ──────────────────────────────────────────────────────────
# Fonts must be placed in game/fonts/ if you add custom .ttf files.
# Ren'Py ships with DejaVuSans by default; replace below once you have
# Playfair Display or IM Fell English from Google Fonts.

# define gui.text_font          = "fonts/PlayfairDisplay-Regular.ttf"
# define gui.name_text_font     = "fonts/PlayfairDisplay-Bold.ttf"
# define gui.interface_text_font = "fonts/IMFellEnglish-Regular.ttf"

## ─── Music ───────────────────────────────────────────────────────────────────
# Default music volume.
define config.default_music_volume = 0.6

## ─── Skip / Auto-Forward ─────────────────────────────────────────────────────

define config.allow_skipping = True
define config.skip_unseen_dialogue = False

## ─── Developer Mode ──────────────────────────────────────────────────────────
# Set to False before final distribution.
define config.developer = True

## ─── Save Directory ──────────────────────────────────────────────────────────
define config.save_directory = "cimarron_chapter1-1.0"
