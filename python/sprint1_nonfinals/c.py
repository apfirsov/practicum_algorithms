"""
Дана матрица.
Нужно написать функцию, которая для элемента возвращает всех его соседей.
Соседним считается элемент, находящийся от текущего на одну ячейку влево,
вправо, вверх или вниз. Диагональные элементы соседними не считаются.

Формат ввода
В первой строке задано n — количество строк матрицы.
Во второй — количество столбцов m. Числа m и n не превосходят 1000.
В следующих n строках задана матрица. Элементы матрицы — целые числа,
по модулю не превосходящие 1000.
В последних двух строках записаны координаты элемента,
соседей которого нужно найти. Индексация начинается с нуля.

Формат вывода
Напечатайте нужные числа в возрастающем порядке через пробел.
"""
from typing import List, Tuple


def get_neighbours(matrix: List[List[int]],
                   row: int, col: int, n: int, m: int) -> List[int]:
    """ID:70284441."""
    result: List[int] = []
    if 0 < row < n:
        result.append(matrix[row-1][col])
    if row < n-1:
        result.append(matrix[row+1][col])
    if 0 < col < m:
        result.append(matrix[row][col-1])
    if col < m-1:
        result.append(matrix[row][col+1])
    result.sort()

    return result


def read_input() -> Tuple[List[List[int]], int, int, int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col, n, m


print(" ".join(map(str, get_neighbours(*read_input()))))
