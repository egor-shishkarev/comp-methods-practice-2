import matplotlib.pyplot as plt
from examples import EllipticalEquation

def show_plot(X, Y, U_num, task: EllipticalEquation):
    
    fig = plt.figure(figsize=(18, 6))

    fig.suptitle(f'\nЭллиптическое уравнение\nТочное решение: {task.u_exact_str}\nПравая часть: {task.f_str}')

    # Numerical solution
    ax1 = fig.add_subplot(131, projection='3d')
    ax1.plot_surface(X, Y, U_num)
    ax1.set_title('Численное решение')
    ax1.set_xlabel('x'); ax1.set_ylabel('y'); ax1.set_zlabel('u_num')

    ax2 = fig.add_subplot(132, projection='3d')
    U_exact = task.u_exact(X, Y)
    ax2.plot_surface(X, Y, U_exact)
    ax2.set_title('Точное решение')
    ax2.set_xlabel('x'); ax2.set_ylabel('y'); ax2.set_zlabel('u_exact')

    ax3 = fig.add_subplot(133, projection='3d')
    ax3.plot_surface(X, Y, U_num - U_exact)
    ax3.set_title('Погрешность')
    ax3.set_xlabel('x'); ax3.set_ylabel('y'); ax3.set_zlabel('error')

    plt.tight_layout()
    plt.show()
