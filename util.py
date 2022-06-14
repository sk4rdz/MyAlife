import numpy as np


def make_dot_circle(radius):
    size = np.array(radius * 2 + 1, radius * 2 + 1)
    is_enclose = np.zeros(size)
    c_radius = radius + 0.5
    for y in np.arange(0, 1, 0.01):
        for x in np.arange(0, 1, 0.01):



