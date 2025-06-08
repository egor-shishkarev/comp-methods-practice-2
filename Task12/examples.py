from dataclasses import dataclass
from typing import List, Callable
from math import sin, cos, pi, sqrt, log
import numpy as np

@dataclass
class Integral:
    func_str: str
    func: Callable
    a: float
    b: float

# Одномерные интегралы
integral1 = Integral("sin(x)", lambda x: sin(x), -1, 1)
integral2 = Integral("exp(-x^2)*log(x+1)", lambda x: np.exp(-x**2)*log(x+1), 0, 2)
integral3 = Integral("x^x", lambda x: x ** x, 0, 1)
integral4 = Integral("sin(x) / x", lambda x: np.sin(x) / x, 1, 5)