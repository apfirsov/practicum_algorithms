"""
Отправка ID: 71420508.

Гоша реализовал структуру данных Дек, максимальный размер которого
определяется заданным числом. Методы push_back(x), push_front(x), pop_back(),
pop_front() работали корректно. Но, если в деке было много элементов,
программа работала очень долго. Дело в том, что не все операции выполнялись
за O(1). Помогите Гоше! Напишите эффективную реализацию.

Внимание: при реализации используйте кольцевой буфер.

Формат ввода
В первой строке записано количество команд n — целое число,
не превосходящее 100000. Во второй строке записано число m — максимальный
размер дека. Он не превосходит 50000.
В следующих n строках записана одна из команд:
- push_back(value) – добавить элемент в конец дека.
Если в деке уже находитсямаксимальное число элементов, вывести «error».
- push_front(value) – добавить элемент в начало дека.
Если в деке уже находится максимальное число элементов, вывести «error».
- pop_front() – вывести первый элемент дека и удалить его.
Если дек был пуст, то вывести «error».
- pop_back() – вывести последний элемент дека и удалить его.
Если дек был пуст, то вывести «error».

Value — целое число, по модулю не превосходящее 1000.

Формат вывода
Выведите результат выполнения каждой команды на отдельной строке.
Для успешных запросов push_back(x) и push_front(x) ничего выводить не надо.
"""
from io import StringIO
import sys
from typing import List, Optional, Tuple


class MyDeque:

    def __init__(self, max_size: int):
        self.deque: List[Optional[int]] = [None] * max_size
        self.max_size: int = max_size
        self.head: int = 0
        self.tail: int = 0
        self.size: int = 0

    def push_front(self, item: int) -> None:
        if self.size == self.max_size:
            print('error')
            return
        self.head = (self.head - 1) % self.max_size
        self.deque[self.head] = item
        self.size += 1

    def push_back(self, item: int) -> None:
        if self.size == self.max_size:
            print('error')
            return
        self.deque[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def pop_front(self) -> Optional[int]:
        if not self.size:
            return None

        item = self.deque[self.head]
        self.deque[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return item

    def pop_back(self) -> Optional[int]:
        if not self.size:
            return None

        self.tail = (self.tail - 1) % self.max_size
        item = self.deque[self.tail]
        self.deque[self.tail] = None
        self.size -= 1
        return item


def main(max_size: int, commands: List[List[str]]) -> None:
    """ID: 71420508."""
    my_deque = MyDeque(max_size)
    for command in commands:
        if command[0] == 'push_back':
            my_deque.push_back(int(command[1]))
        elif command[0] == 'push_front':
            my_deque.push_front(int(command[1]))
        elif command[0] == 'pop_back':
            item = my_deque.pop_back()
            if item is None:
                print('error')
            else:
                print(item)
        elif command[0] == 'pop_front':
            item = my_deque.pop_front()
            if item is None:
                print('error')
            else:
                print(item)


def read_input() -> Tuple[int, List[List[str]]]:
    n = int(input())
    max_size = int(input())
    commands = [input().strip().split() for _ in range(n)]

    return max_size, commands


def test() -> None:
    cases: List[Tuple[int, List[List[str]], str]] = [
        (4,
         [['push_front', '861'], ['push_front', '-819'], ['pop_back'],
          ['pop_back']],
         '861\n-819\n'),
        (10,
         [['push_front', '-855'], ['push_front', '0'], ['pop_back'],
          ['pop_back'], ['push_back', '844'], ['pop_back'],
          ['push_back', '823']],
         '-855\n0\n844\n'),
        (6,
         [['push_front', '-201'], ['push_back', '959'], ['push_back', '102'],
          ['push_front', '20'], ['pop_front'], ['pop_back']],
         '20\n102\n'),
        (7,
         [['pop_front'], ['pop_front'], ['push_front', '741'],
          ['push_front', '648'], ['pop_front'], ['pop_back'], ['pop_front']],
         'error\nerror\n648\n741\nerror\n'),
    ]

    for max_size, commands, exp in cases:
        out = StringIO()
        sys.stdout = out
        main(max_size, commands)
        sys.stdout = sys.__stdout__
        result = out.getvalue()
        assert result == exp, f'WA: {result} != {exp}'

    print('test - OK')


if __name__ == '__main__':
    main(*read_input())
