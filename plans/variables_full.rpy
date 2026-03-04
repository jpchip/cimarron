## variables_full.rpy
## Proposed full-series variable file for Chapters 2–5.
## When implementing Chapter 2, merge these into cimarron_chapter2/game/variables.rpy
## (or use persistent data to pass values from Chapter 1).

# ─── Chapter 1 carry-overs ────────────────────────────────────────────────────
# These originate in Chapter 1. Carry them via persistent data or save import.
# Defaults shown are fallback values if no Ch1 save is found.
default yancey_relationship = 50   # 0–100; < 35 strained, 35–65 balanced, > 65 trusting
default sabra_direction      = 0   # negative = Refined Lady, positive = Frontier Woman

# Ch1 achievement flags (carry forward as backstory)
default sabra_confronted_mother    = False
default sabra_admires_yancey       = False
default sabra_helped_frontier_char = False
default sabra_stood_firm_danger    = False

# ─── Chapter 2 additions ─────────────────────────────────────────────────────
# community_standing: Sabra's reputation in Osage
#   < 0   → seen as passive, outside figure, no civic weight
#   0–4   → known but not central
#   5–8   → respected leader; doors open
#   > 8   → commanding; she is Osage's most prominent woman
default community_standing = 0    # range: approximately -10 to +12

# indian_sympathy: Sabra's evolving stance on Native people
#   < 0   → hostility / contempt; affects Cim's marriage scene badly
#   0–3   → neutral or polite distance
#   4–6   → genuine curiosity; advocacy possible
#   > 6   → strong advocacy; unlocks "The Land Belongs to All" ending
default indian_sympathy = 0       # range: approximately -5 to +10

# Minor flags from Chapter 2
default yancey_mystery = False    # True if Sabra sensed something wrong before Ch Strip departure

# ─── Chapter 3 additions ─────────────────────────────────────────────────────
# sabra_independence: Has Sabra accepted her own authority, separate from Yancey?
#   0–3   → still defines herself in relation to Yancey
#   4–7   → finding her footing as her own person
#   8–10+ → fully independent; Yancey's returns are welcome, not necessary
default sabra_independence = 0    # range: 0 to ~14 across all chapters

# ─── Chapter 4 additions ─────────────────────────────────────────────────────
# newspaper_stance: The Wigwam's editorial voice
#   < -2  → conservative; defends tradition, skeptical of change
#   -2–2  → balanced / neutral
#   > 2   → progressive; champions Indian rights, statehood reform, oil regulation
default newspaper_stance = 0      # range: approximately -5 to +6

# Editorial flags (used in Ch5 speech content)
default dixie_lee_editorial = "neutral"  # "support" | "oppose" | "neutral"
default statehood_stance    = "neutral"  # "single" | "double" | "neutral"

# ─── Chapter 5 additions ─────────────────────────────────────────────────────
# Ending branch (computed at monument scene from accumulated variables)
# Do not set this directly — it is calculated in the ending logic block.
default ending_branch = ""  # "shadow" | "herself" | "land" (set by ending logic)

# ─── Journal flags (all chapters) ────────────────────────────────────────────
# Chapter 1 (already in variables.rpy)
default journal_scene1 = False
default journal_scene2 = False
default journal_scene3 = False
default journal_scene4 = False
default journal_scene5 = False
default journal_scene6 = False
default journal_scene7 = False

# Chapter 2
default journal_scene8  = False
default journal_scene9  = False
default journal_scene10 = False
default journal_scene11 = False
default journal_scene12 = False
default journal_scene13 = False

# Chapter 3
default journal_scene14 = False
default journal_scene15 = False
default journal_scene16 = False
default journal_scene17 = False
default journal_scene18 = False

# Chapter 4
default journal_scene19 = False
default journal_scene20 = False
default journal_scene21 = False
default journal_scene22 = False
default journal_scene23 = False

# Chapter 5
default journal_scene24 = False
default journal_scene25 = False
default journal_scene26 = False
# scene 27: no journal (intentional silence at Yancey's death)
default journal_scene28 = False  # the ending journal entry

# ─── Ending Branch Logic (place at start of Ch5 monument scene) ───────────────
# The following block should be pasted into script.rpy at the start of scene 28:
#
#   if indian_sympathy >= 7 and (sabra_independence >= 5 or yancey_relationship >= 50):
#       $ ending_branch = "land"
#   elif sabra_independence >= 8 and community_standing >= 8:
#       $ ending_branch = "herself"
#   elif sabra_independence <= 4 and yancey_relationship >= 65:
#       $ ending_branch = "shadow"
#   else:
#       $ ending_branch = "shadow"   # fallback
#
#   jump ending_[ending_branch]

# ─── Convenience thresholds (reference only) ─────────────────────────────────
# yancey_relationship:
#   < 35       → strained
#   35–65      → balanced
#   > 65       → trusting
#
# community_standing:
#   <= 0       → passive newcomer
#   1–4        → known
#   5–7        → respected
#   >= 8       → civic leader (required for Branch 2)
#
# indian_sympathy:
#   < 0        → hostile
#   0–3        → neutral
#   4–6        → sympathetic
#   >= 7       → advocate (required for Branch 3)
#
# sabra_independence:
#   0–3        → defines self through Yancey (required for Branch 1)
#   4–7        → transition
#   >= 8       → self-determined (required for Branch 2)
