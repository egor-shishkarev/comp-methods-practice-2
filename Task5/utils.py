import random
from typing import List

def print_matrix(matrix: List[List[float]]):
    print()
    for row in matrix:
        formatted_row = [f"{x:8.3f}" for x in row]
        print("|", " ".join(formatted_row), "|")

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