from typing import List, Tuple
from random import random
import matplotlib.pyplot as plt
import numpy as np
from examples import *

def visualize_integral(dots: List[Tuple[float, float]], integral: Integral) -> None:
    """
    Визуализация метода Монте-Карло для одномерного интеграла с аннотацией попаданий.
    dots: список точек (x,y)
    integral: объект Integral с полями a, b, func и func_str
    """
    a, b = integral.a, integral.b
    func = integral.func
    func_str = getattr(integral, 'func_str', integral.func_str)
    xs = np.linspace(a, b, 500)
    ys = [func(x) for x in xs]
    ymax, ymin = max(ys), min(ys)
    ub = ymax + abs(ymax)/5 if ymax != 0 else 1
    lb = ymin - abs(ymin)/5 if ymin != 0 else -1

    under_pos_x, under_pos_y = [], []  # точки, где f>=0 и y<=f
    under_neg_x, under_neg_y = [], []  # точки, где f<0 и y>=f
    above_x, above_y = [], []          # все остальные

    for x, y in dots:
        fv = func(x)
        if fv >= 0 and 0 <= y <= fv:
            under_pos_x.append(x); under_pos_y.append(y)
        elif fv < 0 and fv <= y <= 0:
            under_neg_x.append(x); under_neg_y.append(y)
        else:
            above_x.append(x); above_y.append(y)

    count_pos = len(under_pos_x)
    count_neg = len(under_neg_x)
    count_above = len(above_x)
    signed_count = count_pos - count_neg

    plt.figure(figsize=(8, 5))
    plt.plot(xs, ys, label="f(x)")
    plt.scatter(under_pos_x, under_pos_y, s=10, alpha=0.5,
                label=f"под графиком (f>=0): {count_pos}")
    if under_neg_x:
        plt.scatter(under_neg_x, under_neg_y, s=10, alpha=0.5,
                    label=f"под графиком (f<0): {count_neg}")
    plt.scatter(above_x, above_y, s=10, marker='x', alpha=0.5,
                label=f"снаружи: {count_above}")
    plt.axhline(0)
    plt.xlim(a, b); plt.ylim(lb, ub)
    plt.xlabel("x"); plt.ylabel("y")
    plt.title(f"Метод Монте-Карло ({len(dots)} точек) для {func_str}")
    plt.legend()
    plt.show()
