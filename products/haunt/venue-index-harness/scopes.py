"""scopes.py - the three index scopes compared in the remediation spike.

A  = the baseline scope, exactly as feasibility-note.md §2 / venue-index-spike.md §4.1
B  = A widened by a named going-out allow-list of categories Overture files
     OUTSIDE the food_and_drink hierarchy (recovers the `inn`/`lodging` class)
C  = B widened again by every named row carrying NO taxonomy at all
"""
# cat_primary values that are 'going out' venues but sit outside food_and_drink
OUT_OF_HIER = [
 'inn','casino','social_club','comedy_club','dance_club','music_venue','karaoke',
 'theatre','theaters_and_performance_venues','dinner_theater','cabaret','cinema',
 'drive_in_theater','stadium_arena','hockey_arena','venue_and_event_space',
 'bowling_alley','pool_billiards','country_club','country_dance_hall','salsa_club',
 'strip_club','liquor_store','beer_wine_and_spirits','sports_club_and_league',
 'golf_club','fishing_club','sailing_club','lawn_bowling_club','rowing_club',
 'music_festivals_and_organizations','musical_band_orchestras_and_symphonies',
]
BASE = "name IS NOT NULL AND confidence >= 0.5"
FD   = "tax_hier[1] = 'food_and_drink'"
ALLOW= "cat_primary IN (" + ",".join("'%s'"%c for c in OUT_OF_HIER) + ")"
NULLTAX = "(tax_hier IS NULL OR len(tax_hier) = 0)"
SCOPE = {
  "A": f"{BASE} AND {FD}",
  "B": f"{BASE} AND ({FD} OR {ALLOW})",
  "C": f"{BASE} AND ({FD} OR {ALLOW} OR {NULLTAX})",
}
