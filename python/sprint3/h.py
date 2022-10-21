"""
Вечером ребята решили поиграть в игру «Большое число».
Даны числа.
Нужно определить, какое самое большое число можно из них составить.

Формат ввода
В первой строке записано n — количество чисел. Оно не превосходит 100.
Во второй строке через пробел записаны n неотрицательных чисел, каждое из
которых не превосходит 1000.

Формат вывода
Нужно вывести самое большое число, которое можно составить из данных чисел.
"""
from typing import List


def gt_comporator(item: str, other: str) -> bool:
    return int(item + other) > int(other + item)


def insertion_sort(arr: List[str]) -> None:
    for i in range(len(arr)):
        item = arr[i]
        j = i
        while j > 0 and gt_comporator(item, arr[j-1]):
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = item


_ = input()
arr = input().strip().split()
insertion_sort(arr)
print(''.join(arr))
