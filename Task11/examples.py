import numpy as np
from typing import List, Tuple, Callable

class Example:
    def __init__(
        self,
        func: Callable[[np.ndarray], float],
        func_str: str,
        grad: Callable[[np.ndarray], np.ndarray],
        x0: np.ndarray,
        eq_cons: List[Tuple[Callable[[np.ndarray], float],
                           Callable[[np.ndarray], np.ndarray]]],
        ineq_cons: List[Tuple[Callable[[np.ndarray], float],
                             Callable[[np.ndarray], np.ndarray]]],
        cons_str: str,
        expected: np.ndarray = None
    ):
        self.func = func
        self.func_str = func_str
        self.grad = grad
        self.x0 = x0
        self.eq_cons = eq_cons        # psi(x)=0 ограничения
        self.ineq_cons = ineq_cons    # phi(x)<=0 ограничения
        self.cons_str = cons_str
        self.expected = expected

examples: List[Example] = []

func1      = lambda x: (x[0] - 1.0)**2 + (x[1] - 1.0)**2
grad1      = lambda x: np.array([2*(x[0] - 1.0), 2*(x[1] - 1.0)])
x0_1       = np.array([0.0, 0.0])
psi1       = lambda x: x[0] + x[1] - 2.0
grad_psi1  = lambda x: np.array([1.0, 1.0])
examples.append(
    Example(
        cons_str="x1+x2=2",
        func_str="(x1−1)^2 + (x2−1)^2",
        func=func1,
        grad=grad1,
        x0=x0_1,
        eq_cons=[(psi1, grad_psi1)],
        ineq_cons=[],
        expected=np.array([1.0, 1.0])
    )
)

func2       = lambda x: x[0]**2 + x[1]**2
grad2       = lambda x: np.array([2*x[0], 2*x[1]])
x0_2        = np.array([0.6, 0.6])
phi21       = lambda x: 1.0 - (x[0] + x[1])
grad_phi21  = lambda x: np.array([-1.0, -1.0])
examples.append(
    Example(
        cons_str="x1+x2>=1",
        func_str="x1^2 + x2^2",
        func=func2,
        grad=grad2,
        x0=x0_2,
        eq_cons=[],
        ineq_cons=[(phi21, grad_phi21)],
        expected=np.array([0.5, 0.5])
    )
)