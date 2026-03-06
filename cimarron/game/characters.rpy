## characters.rpy
## Defines all speaking characters for Cimarron: Chapter One.

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
