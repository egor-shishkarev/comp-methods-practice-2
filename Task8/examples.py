from dataclasses import dataclass
import numpy as np
from typing import Callable

@dataclass
class ThermalConductivityTask:
    kappa: float
    a: float
    T: float
    N: float
    M: float
    mu: Callable[[float], float]
    mu1: Callable[[float], float]
    mu2: Callable[[float], float]
    f: Callable[[float, float], float]
    u_exact: Callable[[float, float], float]

kappa = 1.0
a     = 1.0
T     = 0.1
N     = 50
mu    = lambda x: np.sin(np.pi * x)
mu1   = lambda t: 0.0 * t
mu2   = lambda t: 0.0 * t
f     = lambda x, t: np.zeros_like(x)
u_exact = lambda X, T: np.exp(-np.pi**2 * kappa * T) * np.sin(np.pi * X)

h = a/N

# Случай 1: r = 2.0 (сильно нестабильно)
r1 = 2.0
M1 = int(kappa * T / (r1 * h**2))

# Случай 2: r = 0.55 (средне нестабильно)
r2 = 0.53
M2 = int(kappa * T / (r2 * h**2))

# Случай 3: r = 0.51 (слегка нестабильно)
r3 = 0.51
M3 = int(kappa * T / (r3 * h**2))

# Случай 4: r = 0.1 (стабильно)
r4 = 0.1
M4 = int(kappa * T / (r4 * h**2))

task1 = ThermalConductivityTask(kappa, a, T, N, M1, mu, mu1, mu2, f, u_exact)
task2 = ThermalConductivityTask(kappa, a, T, N, M2, mu, mu1, mu2, f, u_exact)
task3 = ThermalConductivityTask(kappa, a, T, N, M3, mu, mu1, mu2, f, u_exact)
task4 = ThermalConductivityTask(kappa, a, T, N, M4, mu, mu1, mu2, f, u_exact)