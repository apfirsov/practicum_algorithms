"""
Любимый вариант очереди Тимофея — очередь, написанная с использованием
связного списка. Помогите ему с реализацией. Очередь должна поддерживать
выполнение трёх команд:

- get() — вывести элемент, находящийся в голове очереди, и удалить его.
Если очередь пуста, то вывести «error».
- put(x) — добавить число x в очередь
- size() — вывести текущий размер очереди

Формат ввода
В первой строке записано количество команд n — целое число,
не превосходящее 1000. В каждой из следующих n строк записаны команды
по одной строке.

Формат вывода
Выведите ответ на каждый запрос по одному в строке.
"""
#!!! НЕ ДОДЕЛАНО
from typing import List, Optional, Tuple
from timeit import timeit

class MyListQueue:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def put(self, tail) -> None:
        self.next = tail
        tail.prev = self

    def get(self, head):
        head.prev.next = None
        return head.value, head.prev

    def get_size(self) -> int:
        return self.size


def main(max_lenght: int, commands: List[List[str]]) -> None:
    my_queue = MyQueueSized(max_lenght)
    for command in commands:
        if command[0] == 'push':
            my_queue.push(command[1])
        elif command[0] == 'pop':
            print(my_queue.pop())
        elif command[0] == 'peek':
            print(my_queue.peek())
        elif command[0] == 'size':
            print(my_queue.get_size())


def read_input() -> Tuple[int, List[List[str]]]:
    n = int(input())
    max_size = int(input())
    commands = [input().strip().split() for _ in range(n)]

    return max_size, commands

if __name__ == '__main__':
    max_size, commands = read_input()
    print(timeit('main(max_size, commands)', number=1, globals=globals()))
