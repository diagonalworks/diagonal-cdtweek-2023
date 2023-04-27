#!/usr/bin/env python3
# Print the IDs of all buildings in Camden LSOAs

import diagonal_b6 as b6

w = b6.connect_insecure("localhost:8002")
radius_m = 1000
region = b6.cap_polygon(b6.ll(51.535459, -0.125857), radius_m)
lsoas = b6.find_areas(b6.tagged("#boundary", "lsoa").and_(b6.intersecting(region)))
for lsoa_id, lsoa in w(lsoas):
    print("lsoa: %s" % (lsoa.get_string("name"),))
    # You can use a feature as geometry for b6.intersecting(). If you use
    # b6.find_feature() with an ID from an earlier call, the geometry data
    # itself doesn't get sent back to the b6 server, making it more efficient.
    buildings = b6.find(b6.keyed("#building").and_(b6.intersecting(b6.find_feature(lsoa_id))))
    for building_id, building in w(buildings):
        print("  ", building_id)


# The LSOA features on the shared instance are quite large, as they have both
# the geometry, and lots of tags representing the supplemental data. Returning
# those LSOA features alone for a large area may hit message limit sizes.
# If you don't need the full feature, you can use b6.map() to just return, for
# example, the name of the feature, rather than the entire feature, making the
# response small enough to handle large areas.
radius_m = 5000
region = b6.cap_polygon(b6.ll(51.535459, -0.125857), radius_m)
lsoas = b6.find_areas(b6.tagged("#boundary", "lsoa").and_(b6.intersecting(region))).map(lambda f: f.get_string("name"))
for lsoa_id, name in w(lsoas):
    print("lsoa: %s" % (name,))
    buildings = b6.find(b6.keyed("#building").and_(b6.intersecting(b6.find_feature(lsoa_id))))
    for building_id, building in w(buildings):
        print("  ", building_id)
