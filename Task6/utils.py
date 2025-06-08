import matplotlib.pyplot as plt
import numpy as np
from equations import BoundaryTask

def plot_error(errors):
    plt.figure(figsize=(10, 6))
    plt.title("Зависимость погрешности от кол-ва делений")
    plt.xlabel('Количество делений отрезка')
    plt.ylabel('Погрешность')
    plt.xscale('log', base = 10)
    plt.yscale('log', base = 10)
    plt.grid(True)
    plt.plot(sorted(errors.keys()), [errors[i] for i in sorted(errors.keys())], 'o-')
    plt.show()

def plot_solution(problem, x_values, u_values):
    plt.figure(figsize=(10, 6))
    
    # Построение численного решения
    x_numerical = [x_values[i] for i in range(len(x_values))]
    u_numerical = [u_values[i] for i in range(len(u_values))]

    plt.plot(x_numerical, u_numerical, 'o-', label='Численное')
    
    # Построение точного решения
    x_exact = np.linspace(problem.a, problem.b, 1000)
    plt.plot(x_exact, problem.u_exact(x_exact), '--', label='Точное')
    
    plt.xlabel('x')
    plt.ylabel('u(x)')
    plt.title('Решение краевой задачи')
    plt.legend()
    plt.grid(True)
    plt.show()

def print_table(inaccuracies):
    print()
    print("|{:^20}|{:^25}|".format("Кол-во делений", "Макс. погрешность"))
    print("-" * 46)
    for n, inaccuracy in inaccuracies.items():
        print("|{:^20}|{:^25.15e}|".format(n, inaccuracy))