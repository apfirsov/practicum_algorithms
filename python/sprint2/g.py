"""
Реализуйте класс StackMaxEffective, поддерживающий операцию определения
максимума среди элементов в стеке. Сложность операции должна быть O(1).
Для пустого стека операция должна возвращать None. При этом push(x) и pop()
также должны выполняться за константное время.

Формат ввода
В первой строке записано одно число — количество команд,
оно не превосходит 100000. Далее идут команды по одной в строке.
Команды могут быть следующих видов:
push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max нужно напечатать «None»,
для команды pop — «error».
Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения.
Если стек пустой, для команды get_max() напечатайте «None».
Если происходит удаление из пустого стека — напечатайте «error».
"""
from io import StringIO
import sys
from typing import Dict, List, Optional


class StackMaxEffective:

    def __init__(self):
        self.items = []
        self.max_items = []

    def push(self, item: int) -> None:
        self.items.append(item)
        if len(self.max_items) == 0 or item >= self.max_items[-1]:
            self.max_items.append(item)

    def pop(self) -> Optional[int]:
        if not len(self.items):
            return None
        item = self.items.pop()
        if self.max_items[-1] == item:
            self.max_items.pop()
        return item


    def get_max(self) -> Optional[int]:
        if not len(self.max_items):
            return None
        return self.max_items[-1]


def main(commands: List[List[str]]) -> None:
    stack = StackMaxEffective()
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
            'error\nerror\n4\nNone\n': [['10'], ['pop'], ['pop'],
                                        ['push', '4'], ['push', '-5'],
                                        ['push', '7'], ['pop'], ['pop'],
                                        ['get_max'], ['pop'], ['get_max']],
            'None\nerror\nNone\n2\n': [['10'], ['get_max'], ['push', '-6'],
                                       ['pop'], ['pop'], ['get_max'],
                                       ['push', '2'], ['get_max'], ['pop'],
                                       ['push', '-2'], ['push', '-6']]
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
