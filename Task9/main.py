print("Задание 9. Эллиптическое уравнение")

print("""
Реализовать решение эллиптического уравнения (для функции двух
переменных; с заданными граничными условиями) разностным
методом. Систему уравнений решать каким-либо итерационным
методом.
Условия:
- лучше задать самостоятельно (взяв u(x, y) и определив f(x, y))
""")


from utils import *
from examples import *
from methods import *

tasks = [task1, task2]

for task in tasks:
    x, y, U_num = solve_poisson(task.f, task.u_exact, task.Nx, task.Ny)
    X, Y = np.meshgrid(x, y, indexing='ij')
    show_plot(X, Y, U_num, task)
