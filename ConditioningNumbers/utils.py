import random
import numpy as np

def create_random_matrix(rows: int, columns: int = None):
    if columns is None:
        columns = rows

    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(random.randint(1, 100) / random.randint(1, 100))
        matrix.append(row)

    return matrix

def print_system(matrix: np.ndarray, x: np.ndarray, b: np.ndarray, precision: int = 2):
    rows, cols = matrix.shape

    for i in range(rows):
        row_str = " ".join(f"{matrix[i][j]:8.{precision}f}" for j in range(cols))
        x_str = f"| x{i+1} = {x[i]:8.{precision}f}"
        b_str = f"| b = {b[i]:8.{precision}f}"
        print(f"[ {row_str} ] {x_str} {b_str}")
