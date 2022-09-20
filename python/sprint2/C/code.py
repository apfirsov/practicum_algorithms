"""
Вася размышляет, что ему можно не делать из того списка дел, который он
составил. Но, кажется, все пункты очень важные! Вася решает загадать число и
удалить дело, которое идёт под этим номером. Список дел представлен в виде
односвязного списка. Напишите функцию solution, которая принимает на вход
голову списка и номер удаляемого дела и возвращает голову обновлённого списка.
Внимание: в этой задаче не нужно считывать входные данные. Нужно написать
только функцию, которая принимает на вход голову списка и номер удаляемого
элемента и возвращает голову обновлённого списка.

Решение надо отправлять только в виде файла с расширением, которое
соответствует вашему языку. Иначе даже корректно написанное решение не пройдет
тесты.

Формат ввода
Функция принимает голову списка и индекс элемента, который надо
удалить (нумерация с нуля). Список содержит не более 5000 элементов.
Список не бывает пустым.

Формат вывода
Верните голову списка, в котором удален нужный элемент.
"""
# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node, idx):
    if idx == 0:
        return node.next_item

    i = 0
    prev_item = node
    while i < idx-1:
        if prev_item is None:
            return node

        prev_item = prev_item.next_item
        i += 1

    if prev_item.next_item is not None:
        prev_item.next_item = prev_item.next_item.next_item

    return node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


def test_second():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 2)
    assert new_head is node0
    assert new_head.next_item is node1
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node1 -> node3


if __name__ == '__main__':
    test()
    test_second()
