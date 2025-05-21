from typing import List

def print_matrix(matrix: List[List[float]]):
    print()
    for row in matrix:
        formatted_row = [f"{x:8.3f}" for x in row]
        print("|", " ".join(formatted_row), "|")