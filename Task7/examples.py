from dataclasses import dataclass
from typing import Callable
import math

@dataclass
class BoundaryTask:
    # Lu = p(x)u'' + q(x)u' + r(x)u = f(x)
    # lou = a0u(a) + b0u'(a) = gamma0
    # l1u = a1u(b) + b1u'(b) = gamma1
    # если ai = 1, bi = 0 - первый род
    # ai = 0, bi = 1 - второй род
    # ai != 0, bi != 0 - третий род
    p_func: Callable[[float], float]
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
    start_n: int
    end_n: int

a = -1
b = 1
alpha_1 = 1
alpha_2 = 0
alpha = 0
beta_1 = 1
beta_2 = 0
beta = 0

start_n = 3
end_n = 7

p_func_1 = lambda x: 1
q_func_1 = lambda x: 2 / (x + 1.5)
r_func_1 = lambda x: 1 * math.exp(2 * x)
f_func_1 = lambda x: - x

p_func_2 = lambda x: 1 / (x + 2)
q_func_2 = lambda x: (x - 1)
r_func_2 = lambda x: 1 - math.sin(x)
f_func_2 = lambda x: x ** 2 + 1

task1 = BoundaryTask(
    p_func_1, q_func_1, r_func_1, f_func_1, 
    a, b, alpha, beta, alpha_1, alpha_2, beta_1, beta_2, 
    "u'' + 2/(x+1.5)u' + exp(2x)u = -x", 
    "u(-1) = 0, u(1) = 0", 
    start_n, end_n
)

task2 = BoundaryTask(
    p_func_2, q_func_2, r_func_2, f_func_2, 
    a, b, alpha, beta, alpha_1, alpha_2, beta_1, beta_2, 
    "1/(x+2)u'' + (x-1)u' + (1-sin(x))u = x² + 1", 
    "u(-1) = 0, u(1) = 0", 
    start_n, end_n
)
