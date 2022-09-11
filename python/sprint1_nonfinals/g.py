"""
Вася реализовал функцию, которая переводит целое число из десятичной системы
в двоичную. Но, кажется, она получилась не очень оптимальной.

Попробуйте написать более эффективную программу.
Не используйте встроенные средства языка по переводу чисел в бинарное
представление.

Формат ввода
На вход подаётся целое число в диапазоне от 0 до 10000.

Формат вывода
Выведите двоичное представление этого числа.
"""
def to_binary(number: int) -> str:
    """ID: 70306568."""
    result: str = ''
    while number > 0:
        result = str(number % 2) + result
        number = number // 2
    return result if result else '0'


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
