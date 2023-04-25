#!/usr/bin/env python3
# Print the sugar metric of LSOAs around Granary square, finding them via
# the ONS code

import diagonal_b6 as b6

w = b6.connect_insecure("cdtweek-2023.diagonal.works:8002")
codes = ["E01000953", "E01000956", "E01002711"]
for code in codes:
    sugar = w(b6.find_feature(b6.uk_ons_boundary_id(code)).get_float("nutrition:sodium_sum:2021q1"))
    print("%s: %f" % (code, sugar))
