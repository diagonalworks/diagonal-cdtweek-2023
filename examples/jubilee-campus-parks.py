#!/usr/bin/env python3
# What leisure features can you see from the Jubilee campus?

import diagonal_b6 as b6

w = b6.connect_insecure("cdtweek-2023.diagonal.works:8002")
viewpoint = b6.ll(52.95201,-1.18724)
viewshed_radius = 500 # meters
leisure = b6.or_(b6.keyed("#leisure"), b6.tagged("#landuse", "grass"))
features = w(b6.find(b6.and_(leisure, b6.intersecting(b6.sightline(viewpoint, viewshed_radius)))))
for id_, f in features:
    print("%s: %s %s" % (id_, f.get_string("#leisure"), f.get_string("#landuse")))
