from methods import *
from equations import *
from utils import *

print('Задание 6. Краевая задача. Сеточные методы')

print("""
Реализовать решение ОДУ сеточным методом.
- Можно построить уравнение самостоятельно, взяв известное u(x).
  (и тут сразу будет ясно, к какому ответу нужно прийти).
- Начинать вычисления с грубой сетки; измельчать сетку и
  уточнять по Ричардсону. В идеале — до момента выхода на
  ошибки округления. Отследить, какая точность достигнута при
  каком шаге сетки.
- Выводить полученное приближение. Можно на картинке
""")

tasks = [task1, task2, task3]

for i in range(len(tasks)):
    print(f"\nЗадача №{i + 1}\n")
    print("Обыкновенное дифференциальное уравнение:")
    print(tasks[i].task_string)
    print("\nКраевые условия:")
    print(tasks[i].boundary_string)
    x_values, u_values, inaccuracies, n = solve_bvp(tasks[i], tol=1e-6)
    print_table(inaccuracies)

    plot_error(inaccuracies)
    plot_solution(tasks[i], x_values, u_values)
