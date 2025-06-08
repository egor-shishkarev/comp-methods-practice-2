from dataclasses import dataclass
import numpy as np
from typing import Callable

@dataclass
class BoundaryTask:
    u_exact: Callable[[float], float] 
    q_func: Callable[[float], float]
    r_func: Callable[[float], float]
    f_func: Callable[[float], float]
    a: float
    b: float
    alpha: float
    beta: float
    alpha_1: float
    alpha_2: float
    beta_1: float
    beta_2: float
    task_string: str
    boundary_string: str

# Первая задача
def q_func1(x):
    return 0

def r_func1(x):
    return 0

def f_func1(x):
    return 2

def u_exact1(x):
    return x ** 2

a1 = 0
b1 = 1
alpha1 = 0
beta1 = 1
alpha_1_1 = 1
alpha_2_1 = 0
beta_1_1 = 1
beta_2_1 = 0
task_string1 = "u''(x) = 2"
boundary_string1 = "u(a) = 0, u(b) = 1, [a = 0, b = 1]"

task1 = BoundaryTask(u_exact1, q_func1, r_func1, f_func1, a1, b1, alpha1, beta1, alpha_1_1, alpha_2_1, beta_1_1, beta_2_1, task_string1, boundary_string1)

# Вторая задача
def q_func2(x):
    return 0.0

def r_func2(x):
    return 1.0 + x

def f_func2(x):
    return -x * np.exp(x)

def u_exact2(x):
    return np.exp(x)

a2 = 0.0
b2 = 1.0
alpha2 = 1.0
beta2  = np.e
alpha_1_2 = 1.0
alpha_2_2 = 0.0
beta_1_2  = 1.0
beta_2_2  = 0.0

task_string2    = "u''(x) - (1+x)u(x) = -x e^x"
boundary_string2 = "u(0)=1, u(1)=e, [a=0, b=1]"

task2 = BoundaryTask(
    u_exact2, q_func2, r_func2, f_func2,
    a2, b2,
    alpha2, beta2,
    alpha_1_2, alpha_2_2, beta_1_2, beta_2_2,
    task_string2, boundary_string2
)

# Третья задача 
def q_func3(x):
    return 2.0 * x

def r_func3(x):
    return 1.0 + x**2

def f_func3(x):
    return (-np.pi**2 * np.sin(np.pi * x)
            + 2*x * np.pi * np.cos(np.pi * x)
            - (1 + x**2) * np.sin(np.pi * x))

def u_exact3(x):
    return np.sin(np.pi * x)

a3 = 0.0
b3 = 1.0
# Дирихле: u(0)=0, u(1)=0
alpha3 = 0.0
beta3  = 0.0
alpha_1_3 = 1.0
alpha_2_3 = 0.0
beta_1_3  = 1.0
beta_2_3  = 0.0

task_string3    = "u'' + 2x * u' - (1+x^2)u = f(x)"
boundary_string3 = "u(0)=0, u(1)=0, [a=0, b=1]"

task3 = BoundaryTask(
    u_exact3, q_func3, r_func3, f_func3,
    a3, b3,
    alpha3, beta3,
    alpha_1_3, alpha_2_3, beta_1_3, beta_2_3,
    task_string3, boundary_string3
)