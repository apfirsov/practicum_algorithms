"""
Нужно реализовать класс StackMax, который поддерживает операцию определения
максимума среди всех элементов в стеке.
Класс должен поддерживать операции push(x),
где x – целое число, pop() и get_max().

Формат ввода
В первой строке записано одно число n — количество команд, которое
не превосходит 10000. В следующих n строках идут команды.
Команды могут быть следующих видов:

push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max() нужно напечатать «None»,
для команды pop() — «error».

Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения.
Если стек пустой, для команды get_max() напечатайте «None».
Если происходит удаление из пустого стека — напечатайте «error».
"""
from io import StringIO
import sys
from typing import Dict, List, Optional

class StackMax:

    def __init__(self):
        self.items = []

    def push(self, item: int) -> None:
        self.items.append(item)

    def pop(self) -> Optional[int]:
        if not len(self.items):
            return None
        return self.items.pop()

    def get_max(self) -> Optional[int]:
        return max(self.items, default=None)


def main(commands: List[List[str]]) -> None:
    stack = StackMax()
    for command in commands:
        if command[0] == 'push':
            stack.push(int(command[1]))
        elif command[0] == 'pop':
            if stack.pop() is None:
                print('error')

        elif command[0] == 'get_max':
            print(stack.get_max())


def read_input() -> List[List[str]]:
    n = int(input())
    commands = [input().strip().split() for _ in range(n)]
    return commands


def test():
    tests: Dict[str, List[List[str]]] = {
            'None\n-2\n-2\n':
                [['get_max'],['push', '7'],['pop'],['push', '-2'],
                 ['push', '-1'],['pop'],['get_max'],['get_max'],],
            'None\nerror\nerror\nerror\n10\n':
                [['get_max'],['pop'],['pop'],['pop'],['push', '10'],
                 ['get_max'],['push', '-9']]
    }

    for exp, commands in tests.items():
        out = StringIO()
        sys.stdout = out
        main(commands)
        sys.stdout = sys.__stdout__
        assert out.getvalue() == exp, 'WA'

    print('test - OK')


if __name__ == '__main__':
    main(read_input())
