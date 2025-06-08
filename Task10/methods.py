from time import time
from scipy.linalg import norm
import numpy as np
from numpy import array

from utils import ConsoleHelper

def create_identity_vector(n):
    return array([1 for _ in range(n)], dtype="float64")

def gradient_descent(expr, epsilon, x, y, x_prev):
    x_prev = x
    grad = expr.gradient(x_prev)
    x = x_prev - expr.gamma * grad
    return x, None, x_prev, "Градиентного спуска"


def heavy_ball(expr, epsilon, x, y, x_prev):
    prev_x = x
    prev_prev_x = prev_x
    grad = expr.gradient(prev_x)
    x = prev_x - expr.alpha * grad + expr.beta * (prev_x - prev_prev_x)

    return x, None, prev_x, "Шарика"


def nesterov(expr, epsilon, x, y, x_prev):
    x_prev = x
    y_prev = y
    grad = expr.gradient(y_prev)
    x = y_prev - expr.alpha * grad
    y = x + expr.beta * (x - x_prev)

    return x, y, None, "Нестерова"


def newton(expr, epsilon, x, y, x_prev):
    val = expr(x)
    grad = expr.gradient(x)
    hess = expr.hess(x)

    try:
        delta = np.linalg.solve(hess, -grad)
    except np.linalg.LinAlgError:
        delta = -grad

    alpha = 1.0
    while True:
        x_new = x + alpha * delta
        val_new = expr(x_new)
        if val_new < val + 1e-4 * alpha * grad.dot(delta) or alpha < 1e-10:
            break
        alpha *= 0.5
    x = x_new

    return x, y, None, "Ньютона"


def optimization_loop(step, expr, epsilon=0.01, timeout=5):
    x, x_prev, y = [create_identity_vector(expr.dim())] * 3

    start = time()
    iterations = 0
    while time() - start < timeout:
        iterations += 1
        x, y, x_prev, method = step(expr, epsilon, x, y, x_prev)
        if norm(expr.gradient(x)) < epsilon:
            break

    minimum = ConsoleHelper(x, norm(expr.gradient(x)), iterations, time() - start, method)
    return minimum