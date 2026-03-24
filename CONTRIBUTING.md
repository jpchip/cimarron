# Contributing to Cimarron

Thanks for your interest in contributing. This is a Ren'Py visual novel adaptation
of *Cimarron* by Edna Ferber (1929). Contributions are welcome across writing,
code, and art.

---

## Ways to Contribute

### Writing
- Dialogue polish — improving lines to better match Ferber's prose style
- New branches or choice variations within existing scenes
- Content for future chapters (Chapter 2 onward)
- Proofreading for typos, anachronisms, or historical inaccuracies

### Code
- Bug fixes in `.rpy` scripts or screens
- New mini-games for other scenes (see `PLAN.md` for candidates)
- UI improvements in `gui.rpy` or `screens.rpy`
- Save/load, accessibility, or quality-of-life improvements

### Art & Audio
- Background images matching the scene descriptions in `cimarron_chapter1/README.md`
- Character sprites (see the sprite table in the same file)
- Music tracks or ambient sound effects
- GUI assets (textbox, namebox, buttons) matching the earth-tone palette

---

## Getting Started

1. **Fork** the repository and clone your fork locally.
2. **Install Ren'Py** from https://www.renpy.org/ if you haven't already.
3. Open the Ren'Py launcher → **Open Project** → select `cimarron_chapter1/`.
4. Make your changes, then click **Launch Project** to test.
5. Open a pull request with a clear description of what you changed and why.

---

## Project Structure

```
cimarron/
├── book.md               ← Source novel (read-only reference — do not edit)
├── PLAN.md               ← Design document; check here before adding scenes
├── cimarron_chapter1/
│   └── game/
│       ├── script.rpy                ← Main story (scenes 1–7)
│       ├── characters.rpy            ← Character definitions
│       ├── variables.rpy             ← Game state variables
│       ├── minigame_typesetting.rpy  ← Scene 6 mini-game
│       ├── gui.rpy                   ← Visual theme
│       └── screens.rpy               ← UI screens
```

Full asset filenames and AI prompt suggestions are in `cimarron_chapter1/README.md`.

---

## Guidelines

### Staying True to the Source
- Ferber's prose is literary and specific — preserve her voice in narration.
- Sabra's interiority is the heart of the story. Choices should feel like her
  perspective, not generic VN options.
- The novel is critical of racism and settler colonialism. Any new content should
  reflect that complexity rather than flattening it.

### Code Style
- Follow the existing `.rpy` formatting: two-space indents, section header comments.
- New game state variables go in `variables.rpy` with a comment explaining the range
  and effect.
- New characters go in `characters.rpy`.
- Mini-games get their own file: `minigame_<name>.rpy`.

### Historical Accuracy
- The story is set 1889–1893 (Chapter 1 is April 1889).
- `book.md` is the primary reference — quote or paraphrase it when in doubt.
- Flag any dialogue or detail you're uncertain about in your pull request.

### Assets
- All contributed art and audio must be either original work or clearly licensed
  for use (CC0, CC-BY, or similar). Include the source and license in your PR.
- Backgrounds: 1280×720px minimum.
- Sprites: PNG with transparent background, roughly 400–600px tall.
- Audio: `.ogg` format, loopable where applicable.

---

## Reporting Issues

Open a GitHub issue for:
- Bugs (errors, broken branches, variables not updating correctly)
- Dialogue that feels out of period or out of character
- Layout or readability problems
- Missing asset references

---

## License

By contributing, you agree that your contributions will be licensed under the
project's License. See `LICENSE` for details.

The source novel text (`book.md`) is public domain and is not affected by the
license.
