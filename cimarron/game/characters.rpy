## characters.rpy
## Defines all speaking characters for Cimarron: Chapter One.

## ── Sprite image declarations ─────────────────────────────────────────────────
## Ren'Py auto-names images in subdirectories with the folder prefix, so we
## declare explicit names that match the "show yancey passionate" syntax.

image yancey neutral    = Transform("images/sprites/yancey_neutral.png",    zoom=0.45)
image yancey passionate = Transform("images/sprites/yancey_passionate.png", zoom=0.45)
image yancey tender     = Transform("images/sprites/yancey_tender.png",     zoom=0.45)
image yancey dangerous  = Transform("images/sprites/yancey_dangerous.png",  zoom=0.45)
image yancey restless   = Transform("images/sprites/yancey_restless.png",   zoom=0.45)
image yancey weary      = Transform("images/sprites/yancey_weary.png",      zoom=0.45)

image yancey roughrider neutral = Transform("images/sprites/yancey_roughrider_neutral.png", zoom=0.45)
image yancey roughrider weary   = Transform("images/sprites/yancey_roughrider_weary.png",   zoom=0.45)
image yancey roughrider tender  = Transform("images/sprites/yancey_roughrider_tender.png",  zoom=0.45)
image yancey dying              = Transform("images/sprites/yancey_dying.png",               zoom=0.45)

image sabra neutral     = Transform("images/sprites/sabra_neutral.png",     zoom=0.45)
image sabra determined  = Transform("images/sprites/sabra_determined.png",  zoom=0.45)
image sabra worried     = Transform("images/sprites/sabra_worried.png",     zoom=0.45)
image sabra proud       = Transform("images/sprites/sabra_proud.png",       zoom=0.45)
image sabra tender      = Transform("images/sprites/sabra_tender.png",      zoom=0.45)
image sabra weary       = Transform("images/sprites/sabra_weary.png",       zoom=0.45)

image congregation neutral = Transform("images/sprites/congregation_neutral.png", zoom=0.45)
image congregation cheat   = Transform("images/sprites/congregation_cheat.png",   zoom=0.45)

image isaiah child neutral = Transform("images/sprites/isaiah_child_neutral.png", zoom=0.45)
image isaiah neutral       = Transform("images/sprites/isaiah_neutral.png",       zoom=0.45)

image dixie neutral  = Transform("images/sprites/dixie_neutral.png",  zoom=0.45)
image dixie direct   = Transform("images/sprites/dixie_direct.png",   zoom=0.45)
image dixie composed = Transform("images/sprites/dixie_composed.png", zoom=0.45)
image dixie sad      = Transform("images/sprites/dixie_sad.png",      zoom=0.45)

image doc neutral = Transform("images/sprites/doc_neutral.png", zoom=0.45)
image doc weary   = Transform("images/sprites/doc_weary.png",   zoom=0.45)
image doc warm    = Transform("images/sprites/doc_warm.png",    zoom=0.45)

## ── Position transforms for character sprites ────────────────────────────────
## Override built-in left/right/center to position sprites in upper screen area.

transform left:
    xpos 0.0 xanchor 0.0
    ypos 500 yanchor 1.0

transform right:
    xpos 1.0 xanchor 1.0
    ypos 500 yanchor 1.0

transform center:
    xpos 0.5 xanchor 0.5
    ypos 500 yanchor 1.0

# Narrator — third-person literary voice (Ferber-style prose)
# Ren'Py provides a built-in narrator; unquoted strings use it automatically.
# No definition needed here.

# Sabra Cravat — the player character; her thoughts appear in italics
define sabra = Character("Sabra", color="#8B4513", what_italic=True)

# Yancey Cravat — Sabra's husband; larger-than-life, charismatic
define yancey = Character("Yancey", color="#2F4F4F")

# Felice Venable — Sabra's imperious mother
define felice = Character("Mrs. Venable", color="#800000")

# Lewis Venable — Sabra's gentle, ailing father
define lewis = Character("Mr. Venable", color="#4A3728")

# Sol Levy — the quiet Jewish merchant of Osage
define sol = Character("Sol Levy", color="#556B2F")

# Mother Bridget — the wise, plain-spoken nun at the Mission
define mother_bridget = Character("Mother Bridget", color="#483D8B")

# Isaiah — the young Black servant boy who follows the Cravats
define isaiah = Character("Isaiah", color="#8B6914")

# Dixie Lee — a rough frontier woman Sabra encounters in Osage
define dixie = Character("Dixie Lee", color="#A0522D")

# Generic frontier character for scene 5
define stranger = Character("Stranger", color="#696969")

# ── Chapter 2 characters ──────────────────────────────────────────────────────

# Doc Valliant — the town's hard-drinking, warm-hearted physician
define doc   = Character("Doc Valliant",      color="#8B7355")

# Arita Red Feather — a Cherokee woman; proud, measured, watching
define arita = Character("Arita Red Feather", color="#CD5C1A")

# Pete Pitchlyn — an old acquaintance of Yancey's from the territory days
define pete  = Character("Pete Pitchlyn",     color="#6B8E23")

# The Kid — a young gunman whose name no one quite knows
define kid   = Character("The Kid",           color="#444444")

# ── Chapter 4 characters ──────────────────────────────────────────────────────

# Tracy Wyatt — a Tulsa oil investor; charming, calculating, modern
define tracy = Character("Tracy Wyatt",  color="#5F4F3B")

# Cim Cravat — Sabra and Yancey's son, grown into a young man
define cim   = Character("Cim Cravat",   color="#6B4B2B")

# Donna Cravat — Sabra and Yancey's daughter, growing up fast
define donna = Character("Donna Cravat", color="#9B7E6A")

# ── Chapter 5 characters ──────────────────────────────────────────────────────

# Ruby Big Elk — Cim's wife; young Osage woman; composed, direct, watchful
define ruby    = Character("Ruby Big Elk",  color="#8B6914")

# Masja Krbecek — the Polish sculptor commissioned for the monument
define krbecek = Character("Masja Krbecek", color="#888888")
