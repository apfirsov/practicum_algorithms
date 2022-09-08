"""
Обратите внимание на ограничения в этой задаче. (1 c.)

Рита и Гоша играют в игру. У Риты есть n фишек, на каждой из которых написано
количество очков. Фишки лежат на столе в порядке неубывания очков на них.
Сначала Гоша называет число k, затем Рита должна выбрать две фишки, сумма очков
на которых равна заданному числу.

Рите надоело искать фишки самой, и она решила применить свои навыки
программирования для решения этой задачи. Помогите ей написать программу для
поиска нужных фишек.

Формат ввода
В первой строке записано количество фишек n, 2 ≤ n ≤ 10^5.
Во второй строке записано n целых чисел в порядке неубывания —– очки на фишках
Риты в диапазоне от -105 до 105.
В третьей строке —– загаданное Гошей целое число k, -10^5 ≤ k ≤ 10^5.

Формат вывода
Нужно вывести два числа —– очки на двух фишках, в сумме дающие k.
Если таких пар несколько, то можно вывести любую из них.
Если таких пар не существует, то вывести «None».
"""
from typing import List, Tuple, Optional

def two_sum_with_set(
        n:int, arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    """С загрузкой памяти."""
    cache: set = set()
    for i in range(n):
        value = arr[i]
        second_value = target_sum - value
        if second_value in cache:
            return second_value, value
        cache.add(value)
    return None


def two_sum_with_two_pointers(
        n:int, arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    """С двумя указателями."""
    if n < 2:
        return None

    arr.sort()
    start: int = 0
    end: int = n - 1

    while start < end:
        sum = arr[start] + arr[end]
        if sum == target_sum:
            return arr[start], arr[end]

        if sum > target_sum:
            end -= 1
        else:
            start += 1

    return None


def read_input() -> Tuple[int, List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return n, arr, target_sum


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))


def test() -> None:
    data: List[Tuple[int, List[int], int]] = [
        (6, [-9, -7, -6, -1, -1, 3], 2),
        (8, [-3, 1, 1, 2, 6, 6, 8, 10], 100),
    ]
    for args in data:
        print_result(two_sum_with_set(*args))
        print_result(two_sum_with_two_pointers(*args))

print_result(two_sum_with_two_pointers(*read_input()))
# test()
