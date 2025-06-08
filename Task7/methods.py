import functools
import numpy as np
import scipy as sp
import math
from examples import *
import numdifftools as nd

def ritz_method(task: BoundaryTask, n):
    p_func, q_func, r_func, f_func = task.p_func, task.q_func, task.r_func, task.f_func

    omegas = [coordinates(i) for i in range(n)]

    # Матрица системы: (Lφ_j, φ_i)
    matrix = np.zeros((n, n))
    # Вектор правой части: (f, φ_i)
    vector = np.zeros(n)

    for i in range(n):
        for j in range(n):
            # Вычисление (Lφ_j, φ_i)
            integrand = lambda x: (-p_func(x) * df(omegas[j], 2)(x) + q_func(x) * df(omegas[j])(x) + r_func(x) * omegas[j](x)) * omegas[i](x)
            matrix[i, j] = sp.integrate.quad(integrand, -1, 1)[0]
        # Вычисление (f, φ_i)
        vector[i] = sp.integrate.quad(lambda x: f_func(x) * omegas[i](x), -1, 1)[0]

    # Решение системы
    try:
        c = np.linalg.solve(matrix, vector)
        return lambda x: sum(c[i] * omegas[i](x) for i in range(n))
    except np.linalg.LinAlgError:
        print(f"Ошибка: не удалось решить систему для метода Ритца с n={n}")
        return lambda x: 0

def collocation(task: BoundaryTask, n):
    p_func, q_func, r_func, f_func = task.p_func, task.q_func, task.r_func, task.f_func

    t_values = [math.cos((2 * i + 1) * math.pi / (2 * n)) for i in range(n)]  # Правильные узлы Чебышева
    L = lambda y: lambda x: - p_func(x) * df(y, 2)(x) + q_func(x) * df(y)(x) + r_func(x) * y(x)
    L = np.vectorize(L)

    omegas = [coordinates(i) for i in range(n)]
    Lw = L(omegas)

    matrix = np.zeros((n, n))
    vector = np.zeros(n)

    for i in range(n):
        for j in range(n):
            matrix[i, j] = Lw[j](t_values[i])
        vector[i] = f_func(t_values[i])

    # Добавление проверки ранга матрицы
    if np.linalg.matrix_rank(matrix) < n:
        print(f"Предупреждение: матрица для n={n} вырождена")
        return lambda x: 0  # Возвращаем нулевую функцию или обработку ошибки

    try:
        c = np.linalg.solve(matrix, vector)
        return lambda x: sum(c[i] * omegas[i](x) for i in range(n))
    except np.linalg.LinAlgError:
        print(f"Ошибка: не удалось решить систему для метода коллокации с n={n}")
        return lambda x: 0 
    
def df(f, ord=1):
    return nd.Derivative(f, step=1e-2, n=ord)

@functools.lru_cache(maxsize=None)
def coordinates(n):
    return lambda x: ((1 - x ** 2) * sp.special.eval_jacobi(n, 1, 1, x))