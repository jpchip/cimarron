# Cimarron Visual Novel — Full Series Plan

## Context

Chapter 1 (book chapters I-VII) is complete as a Ren'Py MVP. This plan covers the full remainder of Edna Ferber's *Cimarron* (1929), structured into four additional game chapters that can each be implemented independently. The goal is to stay true to Ferber's source material while building a coherent choice-driven narrative where Sabra's decisions accumulate into a meaningful ending.

---

## Source-to-Game Chapter Mapping

| Game Chapter | Book Chapters | Time Period | Theme |
|---|---|---|---|
| Ch 1 (done) | I–VII | 1889, ~6 months | The Land Run & Arrival |
| **Ch 2** | VIII–XII | 1890–1894, ~4 years | Building Osage |
| **Ch 3** | XIII–XV | 1894–1898, ~5 years | Yancey Leaves; Sabra Rises |
| **Ch 4** | XVI–XX | 1898–1907, ~9 years | War Hero, Statehood, Oil |
| **Ch 5** | XXI–XXV | 1907–1930, ~23 years | Legacy & Monument |

---

## Global Mechanics (all chapters)

### Persisted Variables (carry across all chapters)

- `yancey_relationship` (0–100): Trust/tension with Yancey. Starts from Ch1 value.
- `sabra_direction` (int): Refined Lady (negative) vs. Frontier Woman (positive). Starts from Ch1 value.
- `community_standing` (default 0, new in Ch2): How Osage sees Sabra — passive newcomer (negative) to respected civic leader (positive).
- `indian_sympathy` (default 0, new in Ch2): Sabra's stance on Native Americans. Affects Cim's marriage arc and the monument ending.
- Ch1 achievement flags carry forward as backstory context.

### New Mechanics Introduced Per Chapter

- **Ch 2**: `community_standing`, `indian_sympathy`, journal continues (scenes 8–14)
- **Ch 3**: `sabra_independence` — tracks whether Sabra has stopped waiting for Yancey (unlocks new dialogue options)
- **Ch 4**: `newspaper_stance` — conservative or progressive editorial voice; affects statehood and oil debate scenes
- **Ch 5**: Ending convergence — all meters + flags determine ending variant

### Endings (Ch 5 resolution, driven by cumulative choices)

The final scene (monument unveiling) has three possible framings:

1. **"She Was His Shadow"** — low `sabra_independence`, high `yancey_relationship` → bittersweet, Yancey glorified
2. **"She Built It Herself"** — high `community_standing`, high `sabra_independence` → triumphant, Sabra as the true pioneer
3. **"The Land Belongs to All"** — high `indian_sympathy`, moderate everything else → Cim/Ruby's children at the statue; the mixed heritage as the real legacy

---

## File Structure

```
/home/jchip/workspace/cimarron/plans/
├── overview.md            ← this document
├── chapter2/
│   └── plan.md
├── chapter3/
│   └── plan.md
├── chapter4/
│   └── plan.md
└── chapter5/
    └── plan.md
```

---

## New Variables Summary

```python
# Ch 2 additions (add to variables.rpy when implementing Ch 2)
default community_standing = 0    # -10 to +10; civic reputation in Osage
default indian_sympathy = 0       # -5 to +10; Sabra's stance toward Native people

# Ch 3 additions
default sabra_independence = 0    # 0 to 10; willingness to act without Yancey

# Ch 4 additions
default newspaper_stance = 0      # negative=conservative, positive=progressive

# Ch 3 journal flags
default journal_scene8  = False
default journal_scene9  = False
default journal_scene10 = False
default journal_scene11 = False
default journal_scene12 = False
default journal_scene13 = False
default journal_scene14 = False
# (Ch 4 and Ch 5 add scenes 15–21)
```

---

## Implementation Order

Each chapter is a separate Ren'Py project folder:
- `cimarron_chapter2/` — implements scenes 8–14
- `cimarron_chapter3/` — implements scenes 15–18
- `cimarron_chapter4/` — implements scenes 19–23
- `cimarron_chapter5/` — implements scenes 24–28 + ending branches

Variables are passed between chapters using Ren'Py persistent data or save file conventions (TBD at implementation time).

---

## Verification Checklist

After each chapter plan is written:
1. Confirm all book chapters in the range are represented in scenes
2. Confirm every new variable has at least 3 choice points that affect it
3. Confirm the ending branches in Ch 5 can be reached by plausible playthroughs
4. Cross-check character list against `characters.rpy` — new characters need entries

---

## Critical Files

- Existing: `cimarron_chapter1/game/script.rpy`, `variables.rpy`, `characters.rpy`
- Plans: `plans/overview.md`, `plans/chapter*/plan.md`
- Template: `plans/variables_full.rpy` (proposed extension for Ch 2+)
- Future: `cimarron_chapter2/game/`, `cimarron_chapter3/game/`, etc.
