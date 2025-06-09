import numpy as np

def print_results(method_name: str, example, x: np.ndarray, f_val: float, m: dict):
    print("\n" + "="*60)
    print(f"Метод       : {method_name}")
    print(f"Уравнение   : {example.func_str}")
    print(f"Ограничения : {example.cons_str}")
    if example.expected is not None:
        print(f"Ожидалось   : {np.round(example.expected, 6)}")
    print(f"Найдено x*  : {np.round(x, 6)}")
    print(f"f(x*)       : {f_val:.6e}")
    print(f"Итераций    : {m['iter']}")
    print(f"Время, с    : {m['time']:.4f}")
    print("="*60)
