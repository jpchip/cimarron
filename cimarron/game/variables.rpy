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
# Reset before each Scene 16 call ($ letters_printed = [], $ letters_spiked = []).
default letters_printed = []
default letters_spiked  = []

# ─── Chapter 4 Flags ──────────────────────────────────────────────────────────
default dixie_lee_editorial = "none"   # "support" / "oppose" / "neutral"
default statehood_stance    = "none"   # "single" / "double" / "consult"

# ─── Chapter 4 Journal Flags ──────────────────────────────────────────────────
default journal_scene19 = False
default journal_scene20 = False
default journal_scene21 = False
default journal_scene22 = False
default journal_scene23 = False

# ─── Trial Minigame State ─────────────────────────────────────────────────────
# Reset before calling trial_arguments_minigame screen.
default trial_sel   = []              # list of selected argument IDs
default trial_ord   = [None, None, None]  # [opening_id, middle_id, closing_id]
default trial_phase = 1               # 1 = selection, 2 = ordering

# ─── Chapter 5 Flags ──────────────────────────────────────────────────────────
default ruby_welcomed        = False   # welcomed Ruby with genuine warmth (scene24)
default ruby_time_needed     = False   # said "I need time" — neutral arc (scene24)
default congress_issue       = "none"  # "indian" / "oil_law" / "education" (scene25)
default donna_wedding_advice = "none"  # "chose_well" / "cravat_stock" / "be_happy" (scene26)

# ─── Chapter 5 Journal Flags ──────────────────────────────────────────────────
default journal_scene24 = False
default journal_scene25 = False
default journal_scene26 = False
# journal_scene27: no journal (scene ends in silence)
default journal_scene28 = False   # set inside whichever ending branch fires

# ─── Photograph Minigame State ────────────────────────────────────────────────
default selected_photos = []    # list of 2 photo IDs; reset before calling screen

# ─── Convenience helpers (read-only computed values) ─────────────────────────
# Use these in conditional dialogue rather than raw numbers.
# Example usage in script:  if yancey_relationship >= 65: ...
