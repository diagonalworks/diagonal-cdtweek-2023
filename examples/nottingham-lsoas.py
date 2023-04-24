#!/usr/bin/env python3
# Print the populations of LSOAs around the Newcastle area

import diagonal_b6 as b6

w = b6.connect_insecure("cdtweek-2023.diagonal.works:8002")
nottingham = b6.cap_polygon(b6.ll(52.940982, -1.1896612), 10000)
lsoas = b6.find(b6.and_(b6.tagged("#boundary", "lsoa"), b6.intersecting(nottingham)))
print([population for id_, population in w(lsoas.get_int("mid_2019_population"))])
