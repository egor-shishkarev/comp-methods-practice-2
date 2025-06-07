import numpy as np
from scipy.linalg import norm

def generate_grid(a, b, n):
    """Генерирует равномерную сетку с n+1 точками на [a,b]"""
    h = (b - a) / n
    x_values = {i: a + i * h for i in range(n + 1)}
    return h, x_values

def setup_tridiagonal_system(problem, n, h, x_values):
    """Настройка коэффициентов для трехдиагональной системы"""
    A = {}  # Коэффициенты для u_{i-1}
    B = {}  # Коэффициенты для u_i
    C = {}  # Коэффициенты для u_{i+1}
    G = {}  # Правая часть

    for i in range(n + 1):
        x_i = x_values[i]

        if i == 0:  # Левая граница
            A[i] = 0
            B[i] = h * problem.alpha_1 + problem.alpha_2
            C[i] = problem.alpha_2
            G[i] = -h * problem.alpha
        elif i == n:  # Правая граница
            A[i] = problem.beta_2
            B[i] = h * problem.beta_1 + problem.beta_2
            C[i] = 0
            G[i] = -h * problem.beta
        else:  # Внутренний узел
            A[i] = problem.p_func(x_i) - problem.q_func(x_i) * h / 2
            C[i] = problem.p_func(x_i) + problem.q_func(x_i) * h / 2
            B[i] = A[i] + C[i] - (h ** 2) * problem.r_func(x_i)
            G[i] = h ** 2 * problem.f_func(x_i)

    return A, B, C, G

def thomas_algorithm(A, B, C, G, n):
    """
    Решение трехдиагональной системы методом прогонки (алгоритм Томаса)
    """
    # Прямая прогонка: вычисляем коэффициенты s и t
    s = {}  # Коэффициенты s_i для u_i = s_i * u_{i+1} + t_i
    t = {}  # Коэффициенты t_i

    for i in range(n + 1):
        if i == 0:
            s[i] = C[i] / B[i]
            t[i] = -G[i] / B[i]
        else:
            s[i] = C[i] / (B[i] - A[i] * s[i - 1])
            t[i] = (A[i] * t[i - 1] - G[i]) / (B[i] - A[i] * s[i - 1])

    # Обратная прогонка: вычисляем значения решения
    u = {}
    for i in range(n, -1, -1):
        if i == n:
            u[i] = t[i]
        else:
            u[i] = s[i] * u[i + 1] + t[i]

    return u

def calculate_richardson_error(u_current, u_previous, n):
    """
    Вычисление погрешности по методу Ричардсона
    """
    max_error = -1
    u_improved = u_current.copy()

    for i in range(0, n + 1, 2):
        error_i = abs((u_current[i] - u_previous[i // 2]) / (2 ** 1 - 1))
        u_improved[i] += error_i

        if error_i > max_error:
            max_error = error_i

    return max_error, u_improved

def solve_bvp(problem, n_start=10, n_max=10 ** 6, tol=1e-6):
    """
    Решение краевой задачи методом конечных разностей с экстраполяцией Ричардсона
    """
    n = n_start
    errors = {}
    u_values_prev = {}

    while n <= n_max:
        h, x_values = generate_grid(problem.a, problem.b, n)
        A, B, C, G = setup_tridiagonal_system(problem, n, h, x_values)
        u_values = thomas_algorithm(A, B, C, G, n)

        if u_values_prev:
            max_error, u_improved = calculate_richardson_error(u_values, u_values_prev, n)
            errors[n] = max_error

            if max_error < tol:
                break

        u_values_prev = u_values.copy()
        n *= 2

    if n > n_start:
        n = n // 2

    return x_values, u_values, errors, n 