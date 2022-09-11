"""
Тимофей записал два числа в двоичной системе счисления и попросил Гошу вывести
их сумму, также в двоичной системе. Встроенную в язык программирования
возможность сложения двоичных чисел применять нельзя.
Помогите Гоше решить задачу.

Решение должно работать за O(N),
где N –— количество разрядов максимального числа на входе.

Формат ввода
Два числа в двоичной системе счисления, каждое на отдельной строке.
Длина каждого числа не превосходит 10 000 символов.

Формат вывода
Одно число в двоичной системе счисления.
"""
from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:
    "ID: 70308966."
    first_i = len(first_number) - 1
    second_i = len(second_number) - 1

    result = ''
    memory = False
    while first_i >= 0 or second_i >= 0 or memory:
        num = 0
        if first_i >= 0 and first_number[first_i] == '1':
            num += 1

        if second_i >= 0 and second_number[second_i] == '1':
            num += 1

        if memory:
            num += 1

        memory = num >= 2
        result = ('1' if num == 3 or num == 1 else '0') + result
        first_i -= 1
        second_i -= 1

    return result if result else '0'



def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
