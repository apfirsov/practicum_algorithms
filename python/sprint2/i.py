"""
Астрологи объявили день очередей ограниченного размера. Тимофею нужно написать
класс MyQueueSized, который принимает параметр max_size,
означающий максимально допустимое количество элементов в очереди.

Помогите ему —– реализуйте программу, которая будет эмулировать работу такой
очереди. Функции, которые надо поддержать, описаны в формате ввода.

Формат ввода
- В первой строке записано одно число — количество команд,
оно не превосходит 5000.
- Во второй строке задан максимально допустимый размер очереди,
он не превосходит 5000.
- Далее идут команды по одной на строке. Команды могут быть следующих видов:

push(x) — добавить число x в очередь;
pop() — удалить число из очереди и вывести на печать;
peek() — напечатать первое число в очереди;
size() — вернуть размер очереди;
При превышении допустимого размера очереди нужно вывести «error».
При вызове операций pop() или peek() для пустой очереди нужно вывести «None».

Формат вывода
Напечатайте результаты выполнения нужных команд, по одному на строке.
"""
from typing import List, Optional, Tuple
from timeit import timeit

class MyQueueSized:

    def __init__(self, max_size: int):
        self.queue: List[Optional[str]] = [None] * max_size
        self.max_size: int = max_size
        self.head: int = 0
        self.tail: int = 0
        self.size: int = 0

    def push(self, item: str) -> None:
        if self.size == self.max_size:
            print('error')
            return

        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def pop(self) -> Optional[str]:
        item = self.peek()
        if item == None:
            return item
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return item

    def peek(self) -> Optional[str]:
        if not self.size:
            return None
        return self.queue[self.head]

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
