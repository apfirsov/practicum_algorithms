"""
Вот какую задачу Тимофей предложил на собеседовании одному из кандидатов.
Если вы с ней ещё не сталкивались, то наверняка столкнётесь - она довольно
популярная.

Дана скобочная последовательность. Нужно определить, правильная ли она.

Будем придерживаться такого определения:
- пустая строка - правильная скобочная последовательность;
- правильная скобочная последовательность, взятая в скобки одного
типа, –— правильная скобочная последовательность;
- правильная скобочная последовательность с приписанной слева или справа
правильной скобочной последовательностью —– тоже правильная.

На вход подаётся последовательность из скобок трёх видов: [], (), {}.
Напишите функцию is_correct_bracket_seq, которая принимает на вход скобочную
последовательность и возвращает True, если последовательность правильная,
а иначе False.

Формат ввода
На вход подаётся одна строка, содержащая скобочную последовательность.
Скобки записаны подряд, без пробелов.

Формат вывода
Выведите «True» или «False».
"""
from typing import Optional


class Stack:

    def __init__(self):
        self.items = []

    def push(self, item: str) -> None:
        self.items.append(item)

    def pop(self) -> Optional[str]:
        if not len(self.items):
            return None
        return self.items.pop()

    def is_empty(self) -> bool:
        return not len(self.items)


def main(seq: str) -> bool:
    stack = Stack()
    for symbol in seq:
        if symbol in '[{(':
            stack.push(symbol)
            continue

        item = stack.pop()
        if not item:
            return False

        if not (item == '[' and symbol == ']'
            or item == '{' and symbol == '}'
            or item == '(' and symbol == ')'):
            return False

    return stack.is_empty()


def read_input() -> str:
    return input()


def test():
    tests = [
        ('{[()]}', True),
        ('()', True),
        ('()[]{}', True),
        ('{[()}]', False),
        (')', False),
        ('{[)}', False),
    ]

    for seq, exp in tests:
        assert exp == main(seq)

    print('test - OK')


if __name__ == '__main__':
    print(main(read_input()))
