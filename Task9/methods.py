import numpy as np

def solve_poisson(f_func, u_exact, Nx, Ny, tol=1e-6, max_iter=10000):
    x = np.linspace(0, 1, Nx)
    y = np.linspace(0, 1, Ny)
    h = x[1] - x[0]
    u = np.zeros((Nx, Ny))
    hx = 1/(Nx-1)
    hy = 1/(Ny-1)


    for i in range(Nx):
        u[i, 0] = u_exact(x[i], y[0])
        u[i, -1] = u_exact(x[i], y[-1])
    for j in range(Ny):
        u[0, j] = u_exact(x[0], y[j])
        u[-1, j] = u_exact(x[-1], y[j])


    f = np.zeros_like(u)
    for i in range(Nx):
        for j in range(Ny):
            f[i, j] = f_func(x[i], y[j])

    for _ in range(max_iter):
        max_diff = 0.0
        for i in range(1, Nx-1):
            for j in range(1, Ny-1):
                u_new = (
                    hy*hy*(u[i+1,j] + u[i-1,j]) +
                    hx*hx*(u[i,j+1] + u[i,j-1]) +
                    hx*hx*hy*hy * f[i,j]
                ) / (2*(hx*hx + hy*hy))
                max_diff = max(max_diff, abs(u_new - u[i,j]))
                u[i,j] = u_new
        if max_diff < tol:
            break
    return x, y, u