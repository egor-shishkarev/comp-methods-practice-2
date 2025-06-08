import numpy as np
from examples import *

def solve_heat_implicit(task: ThermalConductivityTask):
    """
        u_t = kappa * u_xx + f(x, t)

        (`un - un) / tau = kappa / h ** 2 * (`un-1 - 2`un + `un+1) + f(xn, `t), `u, `t - смещение вперед по времени
    """
    kappa = task.kappa
    a = task.a
    T = task.T
    N = task.N
    M = task.M
    mu = task.mu
    mu1 = task.mu1
    mu2 = task.mu2
    f = task.f
    
    h = a / N
    tau = T / M
    r = kappa * tau / h**2

    x = np.linspace(0, a, N+1)
    t = np.linspace(0, T, M+1)

    U = np.zeros((M+1, N+1))
    U[0, :] = mu(x) # условие u(x, 0) = mu(x)
    for n in range(M+1):
        U[n, 0] = mu1(t[n])     # два граничных 
        U[n, -1] = mu2(t[n])    # условия

    # Строим трехдиагональную матрицу
    main_diag = (1 + 2*r) * np.ones(N-1)
    off_diag  = -r * np.ones(N-2)
    A = np.diag(main_diag) + np.diag(off_diag, k=-1) + np.diag(off_diag, k=1)

    # "Шагаем" по времени
    for n in range(M):
        b = U[n, 1:-1] + tau * f(x[1:-1], t[n+1])
        b[0]  += r * U[n+1, 0]
        b[-1] += r * U[n+1, -1]
        U[n+1, 1:-1] = np.linalg.solve(A, b)

    return x, t, U

def solve_heat_explicit(task: ThermalConductivityTask):
    """
    Устойчиво при 2 * kappa * tau <= h ** 2 или при r <= 1/2
    """
    kappa = task.kappa
    a = task.a
    T = task.T
    N = task.N
    M = task.M
    mu = task.mu
    mu1 = task.mu1
    mu2 = task.mu2
    f = task.f
    h = a / N
    tau = T / M

    r = kappa * tau / h**2
    x = np.linspace(0, a, N+1)
    t = np.linspace(0, T, M+1)
    U = np.zeros((M+1, N+1))
    U[0, :] = mu(x)
    for n in range(M+1):
        U[n, 0]  = mu1(t[n])
        U[n, -1] = mu2(t[n])
    for n in range(M):
        # compute interior nodes
        U[n+1, 1:-1] = (
            U[n, 1:-1]
            + r * (U[n, :-2] - 2*U[n, 1:-1] + U[n, 2:])
            + tau * f(x[1:-1], t[n])
        )
    return x, t, U
