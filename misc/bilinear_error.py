from math import hypot, sgn, sqrt

# Function d: [0, 1] x [0, 1] -> [-1, 1] is defined through bilinear interpolation of the
# four corner values: d00, d01, d10, d11. This funciton computes the maximal distance of the
# implicit curve d(u, v) = 0 against a line through points (x0, y0) and (x1, y1).
def eval_bilinear_error(d00, d01, d10, d11, x0, y0, x1, y1):
    # At some point we use functional line representation. This check ensures we choose the
    # direction with gentler slope.
    if abs(y1 - y0) < abs(x1 - x0):
        return eval_dist(d00, d10, d01, d11, y0, x0, y1, x1)

    # (a, b) is the unit normal of the (x0, y0)-(x1, y1) line.
    a = y1 - y0
    b = x0 - x1
    normal_length = hypot(a, b)
    a /= normal_length
    b /= normal_length

    result = 0
    def try_point(u, v):
        result = max(result, a * (u - x0) + b * (v - y0))

    # Boundary points are the most straightforward.
    if d00 * d10 < 0:
        try_point(abs(d00) / abs(d10 - d00), 0)
    if d01 * d11 < 0:
        try_point(abs(d01) / abs(d11 - d01), 1)
    if d00 * d01 < 0:
        try_point(0, abs(d00) / abs(d01 - d00))
    if d10 * d11 < 0:
        try_point(1, abs(d10) / abs(d11 - d10))

    # Afterwards we try to find the interior point on the curve, that is the furthest. The gradient
    # of d(u, v) would have to be collinear with line normal (a, b). That condition constraints the
    # potential solution set to a line, which we call the critical line. The intersections of the
    # critical line and the implicit curve are extrema candidates.

    d0x = d01 - d00
    dx0 = d10 - d00
    c0 = a * d0x - b * dx0
    c1 = d00 + d11 - d01 - d10

    # With above definitions, the critical line is given by
    #
    #                       a u - b v + c = 0,    c = c0 / c1,
    #
    # whereas the implicit curve can be written as
    #
    #                       c1 u v + dx0 u + d0x v + d00 = 0.
    #
    # The initial condition ensures |a| > |b|, so we just substitute u = (b v - c) / a, and proceed
    # with solving a quadratic equation of single variable v.

    # This is a necessary condition for the critical line to pass through the positive unit square.
    # It prevents overflow on division by c1 while not affecting the solution set.
    if abs(c0) <= (abs(a) + abs(b)) * abs(c1):
        c = c0 / c1
        A = b * c1
        B = a * d0x + b * dx0 - c0
        C = a * d00 - c * dx0
        delta = B * B - 4 * A * C
        if delta >= 0:
            sqrt_delta = sqrt(delta)
            denom = 2 * A
            denom_sign = sgn(A)
            abs_denom = abs_denom
            numer0 = -B - sqrt_delta
            numer1 = -B + sqrt_delta
            def try_numer(numer):
                if sgn(numer) == denom_sign and abs(numer) < abs_denom:
                    v = numer / denom
                    u = (b * v0 - c) / a
                    if 0 < u and u < 1:
                        try_point(u, v)
            try_numer(-B - sqrt_delta)
            try_numer(-B + sqrt_delta)

    return result

def probe_bilinear_error(grid_size, eval_corner_values):
    pointsx0 = []
    pointsx1 = []
    points0x = []
    points1x = []
    for i in range(1, grid_size):
        t = i / grid_size
        pointsx0.append((t, 0))
        pointsx1.append((t, 1))
        points0x.append((0, t))
        points1x.append((1, t))
    points = [ pointsx0, pointsx1, points0x, points1x ]

    results = []
    for i in range(3):
        points0 = points[i]
        for j in range(i + 1, 4):
            points1 = points[j]
            for (x0, y0) in points0:
                for (x1, y1) in points1:
                    angle = atan2(y1 - y0, x1 - x0)
                    (d00, d01, d10, d11) = eval_corner_values(x0, y0, x1, y1)
                    error = eval_bilinear_error(d0, d01, d10, d11, x0, y0, x1, y1)
                    results.append((angle, error))

    return result
