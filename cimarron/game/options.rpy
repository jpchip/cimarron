## options.rpy
## Ren'Py project configuration for Cimarron: Chapter One.

## ─── Game Basics ─────────────────────────────────────────────────────────────

define config.name = "Cimarron: A Visual Novel"

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
# Font definitions live in gui.rpy. Font files are in game/fonts/.

## ─── Music ───────────────────────────────────────────────────────────────────
# Default music volume.
define config.default_music_volume = 0.6

## ─── Skip / Auto-Forward ─────────────────────────────────────────────────────

define config.allow_skipping = True

## Tab toggles the quick menu bar (handled in screens.rpy quick_menu screen).

## ─── Developer Mode ──────────────────────────────────────────────────────────
# Set to False before final distribution.
define config.developer = True

## ─── Save Directory ──────────────────────────────────────────────────────────
define config.save_directory = "cimarron-1.0"
