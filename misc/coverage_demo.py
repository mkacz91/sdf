from math import cos
from coverage import coverage, _octant_coverage
from numpy import linspace, vectorize
import matplotlib.pyplot as plt

def plot_coverage(phi_count, d_count):
    half_sqrt2 = 0.70710678118
    quarter_pi = 0.78539816339

    vcoverage = vectorize(coverage)
    for phi in linspace(0, quarter_pi, phi_count):
        max_d = half_sqrt2 * cos(quarter_pi - phi)
        ds = linspace(-max_d, max_d, d_count)
        cs = vcoverage(phi, ds)
        plt.plot(ds, cs)

    plt.show()

if __name__ == '__main__':
    plot_coverage(3, 41)
