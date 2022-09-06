"""
Вася занимается строительством лесенок из блоков. Лесенка состоит из ступенек, при этом i-ая ступенька должна состоять ровно из i блоков.

По заданному числу блоков n определите максимальное количество ступенек в лесенке, которую можно построить из этих блоков.

Формат ввода
Ввводится одно число n (1 ≤ n ≤ 2^31 - 1).

Формат вывода
Выведите одно число — количество ступенек в лесенке.
"""

import time


def get_count_slow(n: int) -> int:
    a = 0
    i = 0
    while a < n:
        if a + i + 1 > n:
            break
        i += 1
        a += i
    return i


def read_input() -> int:
    return int(input())


def test() -> None:
    for n in range(10):
        print(n, get_count_slow(n))


def speed_test() -> None:
    n = 2**31 - 1
    start = time.time()
    get_count_slow(n)
    print(time.time() - start)
# test()
# speed_test()
print(get_count_slow(read_input()))
