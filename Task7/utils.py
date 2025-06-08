from examples import BoundaryTask
import numpy as np
import matplotlib.pyplot as plt
from methods import *

def plot_method_comparison(task: BoundaryTask):
    x_values = np.linspace(-1, 1, 1000)

    # Метод ритца
    plt.figure(figsize=(10, 6))
    plt.title(f"Метод Ритца (вариационный). Пример {task.task_string}")

    for n in range(task.start_n, task.end_n + 1):
        y = ritz_method(task, n)
        y_values = [y(x) for x in x_values]
        plt.plot(x_values, y_values, label=f"n={n}")

    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Метод коллокации
    plt.figure(figsize=(10, 6))
    plt.title(f"Метод коллокации (проекционный). Пример {task.task_string}")

    for n in range(task.start_n, task.end_n + 1):
        y = collocation(task, n)
        y_values = [y(x) for x in x_values]
        plt.plot(x_values, y_values, label=f"n={n}")

    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Сравнение при определенном n = 4
    comparison_number = 4
    plt.figure(figsize=(10, 6))
    plt.title(f"Сравнение методов при n={comparison_number}. Пример {task.task_string}")

    y_ritz = ritz_method(task, comparison_number)
    y_ritz_values = [y_ritz(x) for x in x_values]

    y_collocation = collocation(task, comparison_number)
    y_collocation_values = [y_collocation(x) for x in x_values]

    plt.plot(x_values, y_ritz_values, label=f'Метод Ритца', linestyle='-')
    plt.plot(x_values, y_collocation_values, label=f'Метод коллокации', linestyle='--')

    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.legend()
    plt.grid(True)
    plt.show()
