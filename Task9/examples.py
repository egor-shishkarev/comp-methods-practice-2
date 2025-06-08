from dataclasses import dataclass
from math import pi
import numpy as np
from typing import Callable

@dataclass
class EllipticalEquation:
    Nx: float
    Ny: float
    f: Callable[[float, float], float]
    u_exact: Callable[[float, float], float]
    u_exact_str: str
    f_str: str

Nx_1, Ny_1 = 50, 50
u_exact_1 = lambda x, y: np.sin(pi*x) * np.sin(pi*y)
f_1 = lambda x, y: 2 * pi**2 * np.sin(pi*x) * np.sin(pi*y)
u_exact_1_str = "u(x,y) = sin(πx) * sin(πy)"
f_1_str = "f(x,y) = 2π² * sin(πx) * sin(πy)"

Nx_2, Ny_2 = 25, 50
u_exact_2 = lambda x, y: - np.exp(np.sin(pi * x) + np.sin(pi * y))
f_2 = lambda x, y: - u_exact_2(x,y) * pi**2 * (np.cos(pi * x)**2 - np.sin(pi * x) + np.cos(pi * y)**2 - np.sin(pi * y))
u_exact_2_str = "u(x,y) = -exp(sin(πx) + sin(πy))"
f_2_str = "f(x,y) = -u(x,y) * π² * (cos²(πx) - sin(πx) + cos²(πy) - sin(πy))"

task1 = EllipticalEquation(Nx_1, Ny_1, f_1, u_exact_1, u_exact_1_str, f_1_str)
task2 = EllipticalEquation(Nx_2, Ny_2, f_2, u_exact_2, u_exact_2_str, f_2_str)
