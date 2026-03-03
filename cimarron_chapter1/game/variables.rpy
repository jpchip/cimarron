## variables.rpy
## Tracks game state across all scenes of Chapter One.

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

# ─── Convenience helpers (read-only computed values) ─────────────────────────
# Use these in conditional dialogue rather than raw numbers.
# Example usage in script:  if yancey_relationship >= 65: ...
