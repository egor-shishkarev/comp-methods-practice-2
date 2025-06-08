import numpy as np
import matplotlib.pyplot as plt
from examples import *
from methods import *
from utils import *

print("Задание 7. Краевая задача. Проекционные методы")

print("""
- Реализовать один проекционный и один вариационный методы.
  Для разных n.
- Попробовать сравнить.
""")

tasks = [task1, task2]

for i in range(len(tasks)):
    plot_method_comparison(tasks[i])
