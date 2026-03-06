## variables.rpy
## Tracks game state across all scenes of Chapters One through Three.

# ─── Relationship Meter ───────────────────────────────────────────────────────
# yancey_relationship: 0–100
#   < 35   → strained; Yancey is distant, Sabra feels isolated
#   35–65  → balanced; warm but guarded
#   > 65   → trusting; Yancey confides deeply, Sabra feels at home in the frontier
default yancey_relationship = 50

# ─── Sabra's Character Direction ─────────────────────────────────────────────
# sabra_direction: negative = Refined Lady track, positive = Frontier Woman track
#   Affects narration tone and available dialogue options in later chapters.
default sabra_direction = 0

# ─── Journal Unlocks ─────────────────────────────────────────────────────────
# Each flag becomes True after the matching scene is completed.
default journal_scene1 = False
default journal_scene2 = False
default journal_scene3 = False
default journal_scene4 = False
default journal_scene5 = False
default journal_scene6 = False
default journal_scene7 = False

# ─── Chapter Summary Flags ───────────────────────────────────────────────────
# Track how Sabra handled key moments (used in epilogue scene 7 summary).
default sabra_confronted_mother    = False
default sabra_admires_yancey       = False
default sabra_helped_frontier_char = False
default sabra_stood_firm_danger    = False

default quick_menu = True

# ─── Chapter 2 Meters ────────────────────────────────────────────────────────
# community_standing: how Osage sees Sabra; negative=outcast, positive=respected
default community_standing = 0

# indian_sympathy: Sabra's stance toward Osage/Cherokee people
#   < -2 → prejudiced; 0 = cautious; > 3 → advocate
default indian_sympathy = 0

# sabra_independence: how self-sufficient Sabra becomes without Yancey
default sabra_independence = 0

# yancey_mystery: True if Sabra has glimpsed the darker/unknowable side of Yancey
default yancey_mystery = False

# ─── Chapter 2 Journal Flags ──────────────────────────────────────────────────
default journal_scene8  = False
default journal_scene9  = False
default journal_scene10 = False
default journal_scene11 = False
default journal_scene12 = False
default journal_scene13 = False

# ─── Chapter 2 Achievement Flags ─────────────────────────────────────────────
default sabra_stood_alone      = False   # handled birth of Donna without Yancey
default sabra_defended_indians = False   # refused to exclude Arita from the club

# ─── Chapter 3 Meters ────────────────────────────────────────────────────────
# newspaper_stance: editorial direction Sabra steers the Wigwam
#   negative = conservative (conciliatory, advertiser-friendly)
#   positive  = progressive (Indian rights, reform, women's voice)
default newspaper_stance = 0

# ─── Chapter 3 Journal Flags ──────────────────────────────────────────────────
default journal_scene14 = False
default journal_scene15 = False
default journal_scene16 = False
default journal_scene17 = False
default journal_scene18 = False

# ─── Chapter 3 Achievement Flags ─────────────────────────────────────────────
default sabra_cleared_the_office = False  # took charge when Yancey returned (scene15)
default isaiah_defended          = False  # defended Isaiah against the advertiser (scene17)

# ─── Letters Minigame State ───────────────────────────────────────────────────
# Reset before each Scene 16 call; tracks which letter IDs were selected.
default letters_printed = []

# ─── Convenience helpers (read-only computed values) ─────────────────────────
# Use these in conditional dialogue rather than raw numbers.
# Example usage in script:  if yancey_relationship >= 65: ...
