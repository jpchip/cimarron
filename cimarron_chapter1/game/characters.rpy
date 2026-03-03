## characters.rpy
## Defines all speaking characters for Cimarron: Chapter One.

# Narrator — third-person literary voice (Ferber-style prose)
define narrator = Character(None, kind=narrator)

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
