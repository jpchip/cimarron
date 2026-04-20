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
image yancey respect    = Transform("images/sprites/yancey_respect.png",    zoom=0.45)
image yancey charming   = Transform("images/sprites/yancey_charming.png",   zoom=0.45)
image yancey anguished  = Transform("images/sprites/yancey_anguished.png",  zoom=0.45)

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
image sabra happy       = Transform("images/sprites/sabra_happy.png",       zoom=0.45)
image sabra angry       = Transform("images/sprites/sabra_angry.png",       zoom=0.45)
image sabra sad         = Transform("images/sprites/sabra_sad.png",         zoom=0.45)

## Chapter costume variants
image sabra ch1a neutral    = Transform("images/sprites/sabra_ch1a_neutral.png",    zoom=0.45)
image sabra ch1a worried    = Transform("images/sprites/sabra_ch1a_worried.png",    zoom=0.45)
image sabra ch1a determined = Transform("images/sprites/sabra_ch1a_determined.png", zoom=0.45)
image sabra ch1a weary      = Transform("images/sprites/sabra_ch1a_weary.png",      zoom=0.45)

image sabra ch2 neutral    = Transform("images/sprites/sabra_ch2_neutral.png",    zoom=0.45)
image sabra ch2 angry      = Transform("images/sprites/sabra_ch2_angry.png",      zoom=0.45)
image sabra ch2 worried    = Transform("images/sprites/sabra_ch2_worried.png",    zoom=0.45)
image sabra ch2 determined = Transform("images/sprites/sabra_ch2_determined.png", zoom=0.45)
image sabra ch2 tender     = Transform("images/sprites/sabra_ch2_tender.png",     zoom=0.45)
image sabra ch2 proud      = Transform("images/sprites/sabra_ch2_proud.png",      zoom=0.45)
image sabra ch2 weary      = Transform("images/sprites/sabra_ch2_weary.png",      zoom=0.45)

image sabra ch3 neutral    = Transform("images/sprites/sabra_ch3_neutral.png",    zoom=0.45)
image sabra ch3 sad        = Transform("images/sprites/sabra_ch3_sad.png",        zoom=0.45)
image sabra ch3 happy      = Transform("images/sprites/sabra_ch3_happy.png",      zoom=0.45)
image sabra ch3 tender     = Transform("images/sprites/sabra_ch3_tender.png",     zoom=0.45)
image sabra ch3 angry      = Transform("images/sprites/sabra_ch3_angry.png",      zoom=0.45)
image sabra ch3 weary      = Transform("images/sprites/sabra_ch3_weary.png",      zoom=0.45)
image sabra ch3 determined = Transform("images/sprites/sabra_ch3_determined.png", zoom=0.45)

image sabra ch4 neutral    = Transform("images/sprites/sabra_ch4_neutral.png",    zoom=0.45)
image sabra ch4 tender     = Transform("images/sprites/sabra_ch4_tender.png",     zoom=0.45)
image sabra ch4 worried    = Transform("images/sprites/sabra_ch4_worried.png",    zoom=0.45)
image sabra ch4 determined = Transform("images/sprites/sabra_ch4_determined.png", zoom=0.45)
image sabra ch4 weary      = Transform("images/sprites/sabra_ch4_weary.png",      zoom=0.45)
image sabra ch4 proud      = Transform("images/sprites/sabra_ch4_proud.png",      zoom=0.45)

image sabra ch5 neutral    = Transform("images/sprites/sabra_ch5_neutral.png",    zoom=0.45)
image sabra ch5 happy      = Transform("images/sprites/sabra_ch5_happy.png",      zoom=0.45)
image sabra ch5 determined = Transform("images/sprites/sabra_ch5_determined.png", zoom=0.45)
image sabra ch5 sad        = Transform("images/sprites/sabra_ch5_sad.png",        zoom=0.45)
image sabra ch5 tender     = Transform("images/sprites/sabra_ch5_tender.png",     zoom=0.45)
image sabra ch5 weary      = Transform("images/sprites/sabra_ch5_weary.png",      zoom=0.45)
image sabra ch5 proud      = Transform("images/sprites/sabra_ch5_proud.png",      zoom=0.45)
image sabra ch5 worried    = Transform("images/sprites/sabra_ch5_worried.png",    zoom=0.45)

image congregation neutral = Transform("images/sprites/congregation_neutral.png", zoom=0.45)
image congregation cheat   = Transform("images/sprites/congregation_cheat.png",   zoom=0.45)

image rev_barr neutral     = Transform("images/sprites/congregation_7_neutral.png", zoom=0.45)

image isaiah child neutral = Transform("images/sprites/isaiah_child_neutral.png", zoom=0.45)
image isaiah child solemn  = Transform("images/sprites/isaiah_child_solemn.png",  zoom=0.45)
image isaiah neutral       = Transform("images/sprites/isaiah_neutral.png",       zoom=0.45)

image dixie ch1 neutral = Transform("images/sprites/dixie_ch1_neutral.png", zoom=0.45)
image dixie neutral  = Transform("images/sprites/dixie_neutral.png",  zoom=0.45)
image dixie direct   = Transform("images/sprites/dixie_direct.png",   zoom=0.45)
image dixie composed = Transform("images/sprites/dixie_composed.png", zoom=0.45)
image dixie sad      = Transform("images/sprites/dixie_sad.png",      zoom=0.45)

image doc neutral = Transform("images/sprites/doc_neutral.png", zoom=0.45)
image doc weary   = Transform("images/sprites/doc_weary.png",   zoom=0.45)
image doc warm    = Transform("images/sprites/doc_warm.png",    zoom=0.45)

image felice neutral    = Transform("images/sprites/felice_neutral.png",    zoom=0.45)
image felice commanding = Transform("images/sprites/felice_commanding.png", zoom=0.45)

image lewis neutral = Transform("images/sprites/lewis_neutral.png", zoom=0.45)

image pete neutral  = Transform("images/sprites/pete_neutral.png",  zoom=0.45)
image pete curious  = Transform("images/sprites/pete_curious.png",  zoom=0.45)
image pete sardonic = Transform("images/sprites/pete_sardonic.png", zoom=0.45)
image pete serious  = Transform("images/sprites/pete_serious.png",  zoom=0.45)

image sol neutral = Transform("images/sprites/sol_neutral.png", zoom=0.45)

image arita neutral = Transform("images/sprites/arita_neutral.png", zoom=0.45)
image arita gentle  = Transform("images/sprites/arita_gentle.png",  zoom=0.45)
image arita agony   = Transform("images/sprites/arita_agony.png",   zoom=0.45)

image kid dead = Transform("images/sprites/kid_dead.png", zoom=0.45)

image horace neutral = Transform("images/sprites/horace_tubbs_neutral.png", zoom=0.45)
image horace angry   = Transform("images/sprites/horace_tubbs_angry.png",   zoom=0.45)

image tracy neutral  = Transform("images/sprites/tracy_neutral.png",  zoom=0.45)
image tracy charming = Transform("images/sprites/tracy_charming.png", zoom=0.45)

image ruby neutral = Transform("images/sprites/ruby_neutral.png", zoom=0.45)
image ruby direct  = Transform("images/sprites/ruby_direct.png",  zoom=0.45)

image krbecek neutral    = Transform("images/sprites/krbecek_neutral.png",    zoom=0.45)
image krbecek thoughtful = Transform("images/sprites/krbecek_thoughtful.png", zoom=0.45)

image big_elk neutral       = Transform("images/sprites/big_elk_neutral.png",       zoom=0.45)
image big_elk acknowledging = Transform("images/sprites/big_elk_acknowledging.png", zoom=0.45)

image mrs_big_elk neutral   = Transform("images/sprites/mrs_big_elk_neutral.png",   zoom=0.45)

image cim neutral = Transform("images/sprites/cim_neutral.png", zoom=0.45)

image donna neutral      = Transform("images/sprites/donna_neutral.png",      zoom=0.45)
image donna composed     = Transform("images/sprites/donna_composed.png",     zoom=0.45)
image donna ch4 neutral  = Transform("images/sprites/donna_ch4_neutral.png",  zoom=0.45)

image mother_bridget neutral = Transform("images/sprites/mother_bridget_neutral.png", zoom=0.45)
image mother_bridget gentle  = Transform("images/sprites/mother_bridget_gentle.png",  zoom=0.45)

image stranger neutral  = Transform("images/sprites/stranger_neutral.png",  zoom=0.45)
image stranger grinning = Transform("images/sprites/stranger_grinning.png", zoom=0.45)

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

# Sabra Cravat — the player character
define sabra = Character("Sabra", color="#D4895A")

# Yancey Cravat — Sabra's husband; larger-than-life, charismatic
define yancey = Character("Yancey", color="#6BAFAF")

# Felice Venable — Sabra's imperious mother
define felice = Character("Mrs. Venable", color="#D96060")

# Lewis Venable — Sabra's gentle, ailing father
define lewis = Character("Mr. Venable", color="#A08878")

# Sol Levy — the quiet Jewish merchant of Osage
define sol = Character("Sol Levy", color="#90B050")

# Mother Bridget — the wise, plain-spoken nun at the Mission
define mother_bridget = Character("Mother Bridget", color="#8878CC")

# Isaiah — the young Black servant boy who follows the Cravats
define isaiah = Character("Isaiah", color="#C8A030")

# Dixie Lee — a rough frontier woman Sabra encounters in Osage
define dixie = Character("Dixie Lee", color="#C87850")

# Generic frontier character for scene 5
define stranger = Character("Stranger", color="#AAAAAA")

# Rev. Barr — a distinguished frontier minister
define rev_barr = Character("Rev. Barr", color="#6BAFAF")

# ── Chapter 2 characters ──────────────────────────────────────────────────────

# Doc Valliant — the town's hard-drinking, warm-hearted physician
define doc   = Character("Doc Valliant",      color="#B8A080")

# Arita Red Feather — a Cherokee woman; proud, measured, watching
define arita = Character("Arita Red Feather", color="#E07840")

# Pete Pitchlyn — an old acquaintance of Yancey's from the territory days
define pete  = Character("Pete Pitchlyn",     color="#98C050")

# The Kid — a young gunman whose name no one quite knows
define kid   = Character("The Kid",           color="#AAAAAA")

# Horace Greeley Tubbs — hardware merchant and advertiser in Osage; an antagonist in Scene 17
define horace = Character("Horace Tubbs",     color="#B88060")

# ── Chapter 4 characters ──────────────────────────────────────────────────────

# Tracy Wyatt — a Tulsa oil investor; charming, calculating, modern
define tracy = Character("Tracy Wyatt",  color="#A09070")

# Cim Cravat — Sabra and Yancey's son, grown into a young man
define cim   = Character("Cim Cravat",   color="#B08050")

# Donna Cravat — Sabra and Yancey's daughter, growing up fast
define donna = Character("[donna_name] Cravat", color="#C8A888")

# ── Chapter 5 characters ──────────────────────────────────────────────────────

# Ruby Big Elk — Cim's wife; young Osage woman; composed, direct, watchful
define ruby    = Character("Ruby Big Elk",  color="#C8A030")

# Masja Krbecek — the Polish sculptor commissioned for the monument
define krbecek = Character("Masja Krbecek", color="#B0B0B0")

# Big Elk — Ruby's father; former Osage Chief; elder of great dignity
define big_elk = Character("Big Elk", color="#A07848")

# Mrs. Big Elk — Big Elk's third wife; speaks broken English her husband refuses to use
define mrs_big_elk = Character("Mrs. Big Elk", color="#B08860")
