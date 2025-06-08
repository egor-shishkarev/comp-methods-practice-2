from equations import BoundaryTask

def generate_grid(a, b, n):
    h = (b - a) / n
    x_values = {i: a + i * h for i in range(n + 1)}
    return h, x_values

def setup_tridiagonal_system(problem: BoundaryTask, n, h, x_values):
    A = {}  # Коэффициенты для u_{i-1}
    B = {}  # Коэффициенты для u_i
    C = {}  # Коэффициенты для u_{i+1}
    G = {}  # Правая часть

    for i in range(n + 1):
        x_i = x_values[i]

        if i == 0:
            A[i] = 0
            B[i] = problem.alpha_1
            C[i] = problem.alpha_2
            G[i] = problem.alpha
        elif i == n:
            A[i] = - problem.beta_2 / h
            B[i] = problem.beta_1
            C[i] = 0
            G[i] = problem.beta
        else:
            A[i] = 1 / h ** 2 - problem.q_func(x_i) / (2 * h)
            C[i] = 1 / h ** 2  + problem.q_func(x_i) / (2 * h)
            B[i] = - 2 / (h ** 2) - problem.r_func(x_i)
            G[i] = problem.f_func(x_i)

    return A, B, C, G

def thomas_algorithm(A, B, C, G, n):
    # Прямая прогонка
    s = {}  # Коэффициенты s_i для u_i = s_i * u_{i+1} + t_i
    t = {}  # Коэффициенты t_i

    for i in range(n + 1):
        if i == 0:
            s[i] = C[i] / B[i]
            t[i] = G[i] / B[i]
        else:
            denom = (B[i] - A[i] * s[i - 1])
            s[i] = C[i] / denom
            t[i] = (G[i] - A[i] * t[i - 1]) / denom

    # Обратная прогонка
    u = {}
    for i in range(n, -1, -1):
        if i == n:
            u[i] = t[i]
        else:
            u[i] = t[i] - s[i] * u[i + 1]

    return u

def calculate_richardson_error(u_current, u_previous, n):
    max_error = -1
    u_improved = u_current.copy()

    for i in range(0, n + 1, 2):
        error_i = abs((u_current[i] - u_previous[i // 2]) / (2 ** 1 - 1))
        u_improved[i] += error_i

        if error_i > max_error:
            max_error = error_i

    return max_error, u_improved

def solve_bvp(problem, n_start=10, n_max=10 ** 6, tol=1e-6):
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