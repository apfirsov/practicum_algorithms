"""
ID: 72004790.
Альтернативное решение к задаче "b" с использованием дополнительной памяти.
"""
from dataclasses import dataclass
from typing import List


@dataclass
class Contestant:
    login: str
    decision: int
    fine: int

    def __gt__(self, other: 'Contestant'):
        if self.decision != other.decision:
            return self.decision > other.decision

        if self.fine != other.fine:
            return self.fine < other.fine

        return self.login < other.login

    def __str__(self):
        return self.login


def partition(contest_list, pivot):
    left = []
    center = []
    right = []
    for contestant in contest_list:
        if contestant > pivot:
            left.append(contestant)
        elif contestant < pivot:
            right.append(contestant)
        else:
            center.append(contestant)

    return left, center, right


def quicksort(contest_list: List[Contestant]):
    if len(contest_list) < 2:
        return contest_list
    else:
        pivot = contest_list[len(contest_list) // 2]
        left, center, right = partition(contest_list, pivot)
        return quicksort(left) + center + quicksort(right)


def main(contest_list: List[Contestant]):
    for contestant in quicksort(contest_list):
        print(contestant)


def read_input() -> List[Contestant]:
    n = int(input())
    contest_list = [
        Contestant(
            *(lambda a, b, c: (a, int(b), int(c)))(*input().strip().split())
        )
        for _ in range(n)
    ]

    return contest_list


if __name__ == '__main__':
    main(read_input())
