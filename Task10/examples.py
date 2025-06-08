from function import Function
from math import *

from math import sin, cos, exp, log, pi
import numpy as np

expressions = [
    Function(
        "(x1^2 + x2 − 11)^2 + (x1 + x2^2 − 7)^2",
        lambda x: (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2,
        dim=2,
        expected_minimum=[3, 2]
    ),
    Function(
        "y = (x - pi)^2",
        lambda x: (x[0] - np.pi)**2,
        dim=1,
        expected_minimum=[np.pi]
    ),
    Function(
        "y = x1^2 + x2^2",
        lambda x: x[0]**2 + x[1]**2,
        dim=2,
        expected_minimum=[0.0, 0.0]
    ),
    Function(
        "y = (x1 - 1)^2 + 2*(x2 + 2)^2",
        lambda x: (x[0] - 1)**2 + 2*(x[1] + 2)**2,
        dim=2,
        expected_minimum=[1.0, -2.0]
    ),
    Function(
        "y = x1^2 + x2^2 + x3^2",
        lambda x: x[0]**2 + x[1]**2 + x[2]**2,
        dim=3,
        expected_minimum=[0.0, 0.0, 0.0]
    ),
    Function(
        "y = (x1 ^ 2 + 2) * ((x2 - 2) ^ 2 + 3) * ((x3 - 3) ^ 2 + 5)",
        lambda x: (x[0] ** 2 + 2)
        * ((x[1] - 2) ** 2 + 3)
        * ((x[2] - 3) ** 2 + 5),
        dim=3,
        expected_minimum=[0, 2, 3]
    ),
]
