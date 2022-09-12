"""
Васе очень нравятся задачи про строки, поэтому он придумал свою.
Есть 2 строки s и t, состоящие только из строчных букв.
Строка t получена перемешиванием букв строки s и добавлением 1 буквы
в случайную позицию. Нужно найти добавленную букву.

Формат ввода
На вход подаются строки s и t, разделённые переносом строки.
Длины строк не превосходят 1000 символов. Строки не бывают пустыми.

Формат вывода
Выведите лишнюю букву.
"""

from typing import Tuple, List


def get_excessive_letter(shorter: str, longer: str) -> str:
    """ID: 70329426."""
    shorter_list: List[str] = list(shorter)
    longer_list: List[str] = list(longer)
    shorter_list.sort()
    longer_list.sort()
    max_index: int = len(shorter)-1
    for i, symbol in enumerate(longer_list):
        if i > max_index or shorter_list[i] != symbol:
            return symbol


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
