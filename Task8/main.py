import numpy as np
from methods import *
from examples import * 
from utils import *

print("Задание 8. Уравнение теплопроводности")

print("""
- Реализовать решение уравнения теплопроводности по двум схемам:
  одной из неявных и явной.
- Посмотреть на поведение решения по явной схеме при несоблюдении
  условий устойчивости. (Для наглядности лучше рассмотреть
  несколько вариаций: когда условие устойчивости не соблюдается
  чуть-чуть, когда немного побольше, когда сильно не соблюдается.)
- Результаты выводить либо графически (поверхность) —
  предпочтительно, либо численно (матрицу значений).
""")

tasks = [task1, task2,task3,task4]

for task in tasks:
    r = task.kappa * (task.T / task.M) / (task.a / task.N)**2
    x, t, U_approx = solve_heat_implicit(task)
    show_meshgrid(x, t, U_approx, "чисто неявная схема" ,task.u_exact, r)
    x, t, U_approx = solve_heat_explicit(task)
    show_meshgrid(x, t, U_approx, "явная схема", task.u_exact, r)
