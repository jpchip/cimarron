## options.rpy
## Ren'Py project configuration for Cimarron: Chapter One.

## ─── Game Basics ─────────────────────────────────────────────────────────────

define config.name = "Cimarron: A Visual Novel"

# Version string shown in the launcher.
define config.version = "0.2.0"

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
define config.save_directory = "cimarron-0.2.0"


## This section contains information about how to build your project into
## distribution files.
init python:

    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    build.directory_name = "cimarron-0.2.0"

    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "cimarron"

    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = False

    ## File patterns:
    ##
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##
    ##
    ## In a pattern:
    ##
    ## /
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
    