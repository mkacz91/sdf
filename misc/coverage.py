from math import floor, cos, tan

# Computes the coverage induced upon a pixel square by a line with attack angle `phi` and distance
# `d` to the center. Arguments are constrained to `0 <= phi <= pi / 4` and `d >= 0`.
def _octant_coverage(phi, d):
    half_sqrt2 = 0.70710678118
    quarter_pi = 0.78539816339

    d1 = half_sqrt2 * cos(quarter_pi + phi)
    c1 = 0.5 * tan(phi)
    if d < d1:
        alpha = d / d1
        return (1 - alpha) * 0.5 + alpha * c1
    d2 = half_sqrt2 * cos(quarter_pi - phi)
    if d < d2:
        alpha = (d2 - d) / (d2 - d1)
        return alpha * alpha * c1
    return 0

# Computes the coverage induced upon a pixel square by a line with attack angle `phi` and distance
# `d` to the center.
def coverage(phi, d):
    quarter_pi = 0.78539816339
    octant = floor(phi / quarter_pi)
    phi -= octant * quarter_pi
    if int(octant) % 2 != 0:
        phi = quarter_pi - phi
    if d >= 0:
        return _octant_coverage(phi, d)
    else:
        return 1.0 - _octant_coverage(phi, -d)
