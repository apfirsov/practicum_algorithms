"""
L. Два велосипеда
Вася решил накопить денег на два одинаковых велосипеда — себе и сестре.
У Васи есть копилка, в которую каждый день он может добавлять деньги (если,
конечно, у него есть такая финансовая возможность).
В процессе накопления Вася не вынимает деньги из копилки.

У вас есть информация о росте Васиных накоплений — сколько у Васи в копилке
было денег в каждый из дней.

Ваша задача — по заданной стоимости велосипеда определить

первый день, в которой Вася смог бы купить один велосипед,
и первый день, в который Вася смог бы купить два велосипеда.
Подсказка: решение должно работать за O(log n).

Формат ввода
В первой строке дано число дней n, по которым велись наблюдения за Васиными
накоплениями. 1 ≤ n ≤ 106.
В следующей строке записаны n целых неотрицательных чисел.
Числа идут в порядке неубывания. Каждое из чисел не превосходит 106.
В третьей строке записано целое положительное число s — стоимость велосипеда.
Это число не превосходит 106.

Формат вывода
Нужно вывести два числа — номера дней по условию задачи.

Если необходимой суммы в копилке не нашлось, нужно вернуть -1
вместо номера дня.
"""
from typing import List, Tuple


def search(array: List[int], price: int, left: int, right: int) -> int:
    if right < left:
        return -1
    elif right == left and price <= array[right]:
        return right + 1

    mid = (left + right) // 2
    if price <= array[mid]:
        return search(array, price, left, mid)
    else:
        return search(array, price, mid+1, right)


def main(array: List[int], price: int) -> None:
    one = search(array, price, 0, len(array)-1)
    if one == -1:
        print(one, one)
    else:
        two = search(array, 2*price, one, len(array)-1)
        print(one, two)


def read_input() -> Tuple[List[int], int]:
    _ = int(input())
    array = [int(x) for x in input().strip().split()]
    price = int(input())

    return array, price


if __name__ == '__main__':
    main(*read_input())
