"""
Отправка ID: 71599947.

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
from typing import List, Optional, Tuple


class DequeOverFlow(Exception):
    pass


class DequeEmpty(Exception):
    pass


class Deque:

    def __init__(self, max_size: int):
        self.__deque: List[Optional[int]] = [None] * max_size
        self.__max_size: int = max_size
        self.__head: int = 0
        self.__tail: int = 0
        self.__size: int = 0

    def __push(self, item: int, position: int) -> None:
        self.__deque[position] = item
        self.__size += 1

    def __pop(self, position: int) -> int:
        item = self.__deque[position]
        self.__deque[position] = None
        self.__size -= 1
        return item

    def __update_index(self,
                       head: Optional[int] = None,
                       tail: Optional[int] = None) -> None:
        if head is not None:
            self.__head = (self.__head + head) % self.__max_size
        if tail is not None:
            self.__tail = (self.__tail + tail) % self.__max_size

    def push_front(self, item: int) -> None:
        if self.__size == self.__max_size:
            raise DequeOverFlow()
        self.__update_index(head=-1)
        self.__push(item, self.__head)

    def push_back(self, item: int) -> None:
        if self.__size == self.__max_size:
            raise DequeOverFlow()
        self.__push(item, self.__tail)
        self.__update_index(tail=1)

    def pop_front(self) -> int:
        if not self.__size:
            raise DequeEmpty()
        item = self.__pop(self.__head)
        self.__update_index(head=1)
        return item

    def pop_back(self) -> int:
        if not self.__size:
            raise DequeEmpty()
        self.__update_index(tail=-1)
        return self.__pop(self.__tail)


def main(max_size: int, commands: List[List[str]]) -> None:
    deque = Deque(max_size)

    for command in commands:
        args: List[int] = [int(command[i]) for i in range(1, len(command))]
        try:
            result = getattr(deque, command[0])(*args)
            if result is not None:
                print(result)
        except Exception:
            print('error')


def read_input() -> Tuple[int, List[List[str]]]:
    n = int(input())
    max_size = int(input())
    commands = [input().strip().split() for _ in range(n)]

    return max_size, commands


if __name__ == '__main__':
    main(*read_input())
