import numpy as np
from math import sqrt
from random import random
from typing import Callable, Tuple
from scipy.integrate import nquad
from examples import *

def accurate_value(integral: Integral):
    """Точное значение через scipy.integrate.nquad для 1D"""
    return nquad(integral.func, [[integral.a, integral.b]])

def monte_carlo_importance(integral: Integral, count: int = 1000) -> float:
    """
    Importance sampling с линейной плотностью p(x) ~ (x - a)
    """
    a, b = integral.a, integral.b
    func = integral.func
    def p(x): return 2 * (x - a) / (b - a)**2
    def sample(): return a + (b - a) * sqrt(random())
    total = 0.0
    for _ in range(count):
        x = sample()
        total += func(x) / p(x)
    return total / count


def monte_carlo_plain_area(integral: Integral, count: int = 1000) -> Tuple[float, List[Tuple[float, float]]]:
    """
    Классический метод hit-or-miss: возвращает оценку интеграла и список точек.
    Для функций, где f(x)>=0 на [a,b], используется простая доля попаданий.
    Для знакопеременных — со знаком.
    """
    a, b = integral.a, integral.b
    func = integral.func
    xs = np.linspace(a, b, 500)
    ys = [func(x) for x in xs]
    ymax, ymin = max(ys), min(ys)
    # границы прямоугольника
    if ymin >= 0:
        lb = 0
    else:
        lb = ymin
    ub = ymax
    hits = 0
    dots: List[Tuple[float, float]] = []
    for _ in range(count):
        x = a + (b - a) * random()
        y = lb + (ub - lb) * random()
        fv = func(x)
        if ymin >= 0:
            # простая доля попаданий для неотрицательных функций
            if 0 <= y <= fv:
                hits += 1
        else:
            # знакопеременная: учитываем знак
            if fv >= 0 and 0 <= y <= fv:
                hits += 1
            elif fv < 0 and fv <= y <= 0:
                hits -= 1
        dots.append((x, y))
    area_rect = (b - a) * (ub - lb)
    estimate = area_rect * hits / count
    return estimate, dots
