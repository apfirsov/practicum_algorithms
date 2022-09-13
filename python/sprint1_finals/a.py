"""
Тимофей ищет место, чтобы построить себе дом. Улица, на которой он хочет жить,
имеет длину n, то есть состоит из n одинаковых идущих подряд участков.
Каждый участок либо пустой, либо на нём уже построен дом.

Общительный Тимофей не хочет жить далеко от других людей на этой улице.
Поэтому ему важно для каждого участка знать расстояние до ближайшего пустого
участка. Если участок пустой, эта величина будет равна нулю — расстояние до
самого себя.

Помогите Тимофею посчитать искомые расстояния.
Для этого у вас есть карта улицы.
Дома в городе Тимофея нумеровались в том порядке, в котором строились,
поэтому их номера на карте никак не упорядочены.
Пустые участки обозначены нулями.

Формат ввода
В первой строке дана длина улицы —– n (1 ≤ n ≤ 10^6).
В следующей строке записаны n целых неотрицательных чисел — номера домов
и обозначения пустых участков на карте (нули).
Гарантируется, что в последовательности есть хотя бы один ноль.
Номера домов (положительные числа) уникальны и не превосходят 10^9.

Формат вывода
Для каждого из участков выведите расстояние до ближайшего нуля.
Числа выводите в одну строку, разделяя их пробелами.
"""
from typing import List, Optional, Tuple


def get_nearest_zeros(street: List[int]) -> List[int]:
    """
    Оптимизированная версия наивного алгоритма.
    O(n): N + k*N, где k принадлежит [0, 1)
    ID:70381570.
    """
    a: Optional[int] = None
    for index, value in enumerate(street):
        if value == 0:
            a = 0
            b: int = 1
            while (index >= b
                   and (street[index-b] is None or b < street[index-b])):
                street[index-b] = b
                b += 1
        else:
            street[index] = a

        if a is not None:
            a += 1

    return street

def get_nearest_zeros_naive(street: List[int]) -> List[int]:
    """
    Первая версия наивного алгоритма.
    O(n): 2N.
    ID:70381472.
    """
    a: Optional[int] = None
    for index, value in enumerate(street):
        if value == 0:
            a = 0
        else:
            street[index] = a
        if a is not None:
            a += 1

    n: int = len(street)
    b: int = street[n-1]
    for i in range(n-1, -1, -1):
        if street[i] == 0:
            b = 0
        elif street[i] is None or b < street[i]:
            street[i] = b
        b += 1

    return street


def read_input() -> List[int]:
    _ = input()
    street = list(map(int, input().strip().split()))
    return street


print(" ".join(map(str, get_nearest_zeros(read_input()))))
