import numpy as np
import matplotlib.pyplot as plt

def show_meshgrid(x, t, U_approx, method_name, u_exact=None, r=None):
    X, T_grid = np.meshgrid(x, t)

    if callable(u_exact):
        U_exact = u_exact(X, T_grid)
    else:
        raise ValueError(
            "Exact solution function u_exact(x,t) must be provided for comparison."
        )

    error = np.abs(U_exact - U_approx)
    max_error = np.max(error)
    print(f"Max absolute error: {max_error:.3e}")

    fig = plt.figure(figsize=(10, 7))
    
    # Добавляем общий заголовок
    if r is not None:
        fig.suptitle(f'Решение уравнения теплопроводности (r = {r:.2f})', fontsize=16)
    
    ax1 = fig.add_subplot(131, projection='3d')
    ax1.plot_surface(X, T_grid, U_approx, cmap='viridis')
    ax1.set_title(f'Приближенно ({method_name})')
    ax1.set_xlabel('x'); ax1.set_ylabel('t'); ax1.set_zlabel('u')

    ax2 = fig.add_subplot(132, projection='3d')
    ax2.plot_surface(X, T_grid, U_exact, cmap='viridis')
    ax2.set_title('Точное решение')
    ax2.set_xlabel('x'); ax2.set_ylabel('t'); ax2.set_zlabel('u')

    ax3 = fig.add_subplot(133, projection='3d')
    ax3.plot_surface(X, T_grid, error, cmap='inferno')
    ax3.set_title('Погрешность')
    ax3.set_xlabel('x'); ax3.set_ylabel('t'); ax3.set_zlabel('error')

    plt.tight_layout()
    plt.show()