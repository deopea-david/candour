"""handscores.py - hand adjudication applied on top of match.py's automated matcher.

Every override below was decided by reading the venue name, the matched row name,
the distance and the category. They are listed individually so a reader can
disagree item by item, as venue-index-spike.md §4.2 does.
"""
# FSA registrations that are not venues a person "goes out" to -> excluded from scoring
NOT_A_VENUE = {
 "manchester:Addleshaw Goddard",              # a law firm's staff canteen
 "manchester:Manchester Civil Justice Centre also T/as Mediterranean Cuisine",  # court canteen
 "ludlow:Monkey Mania",                       # soft play
 "ludlow:Working Together (Ludlow) Ltd Cafe", # disability-services community cafe
}
# ambiguous -> excluded and named
AMBIGUOUS = {
 "ludlow:3 Church Street",        # an FSA record whose business name is its address
 "chorlton:The Chorlton Green",   # matches 'Chorlton Green Brasserie' 78 m away; could not establish
}
# automated matches I judge WRONG -> forced to a miss
FALSE_MATCH = {
 "chorlton:Beech Inn",            # matched 'Beech Road Cafe' 31 m away: a cafe, not the pub
 "manchester:Luna",               # matched 'Luna Manchester', a clothing shop 366 m away
 "manchester:San Carlo Gran Cafe",# matched 'San Carlo - Manchester', a different branch 398 m away
}
# reported separately rather than excluded: sports and social clubs (as the baseline did)
CLUBS = {
 "chorlton:South West Manchester Cricket Club","chorlton:Whalley Range Amateur Football Club",
 "chorlton:West Disbury & Chorlton AFC","ludlow:The Ludlow Club",
}
