"""
Игра «Тренажёр для скоростной печати» представляет собой поле из клавиш 4x4.
В нём на каждом раунде появляется конфигурация цифр и точек.
На клавише написана либо точка, либо цифра от 1 до 9.

В момент времени t игрок должен одновременно нажать на все клавиши,
на которых написана цифра t.
Гоша и Тимофей могут нажать в один момент времени на k клавиш каждый.
Если в момент времени t нажаты все нужные клавиши, то игроки получают 1 балл.

Найдите число баллов, которое смогут заработать Гоша и Тимофей,
если будут нажимать на клавиши вдвоём.

Формат ввода
В первой строке дано целое число k (1 ≤ k ≤ 5).

В четырёх следующих строках задан вид тренажёра –— по 4 символа в каждой
строке. Каждый символ —– либо точка, либо цифра от 1 до 9.
Символы одной строки идут подряд и не разделены пробелами.

Формат вывода
Выведите единственное число –— максимальное количество баллов,
которое смогут набрать Гоша и Тимофей.
"""
from typing import Dict, Tuple


def get_max_point(k: int, data: str) -> int:
    """ID: 70476238."""
    buttons: Dict[str, int] = {}
    players: int  = 2
    for symbol in data:
        if symbol in buttons:
            buttons[symbol] += 1
        else:
            buttons[symbol] = 1

    points: int = 0
    for symbol, count in buttons.items():
        if symbol != '.' and count <= k * players:
            points += 1

    return points


def read_input() -> Tuple[int, str]:
    k = int(input())
    data = ''
    for _ in range(4):
        data = data + input()

    return k, data


if __name__ == '__main__':
    print(get_max_point(*read_input()))