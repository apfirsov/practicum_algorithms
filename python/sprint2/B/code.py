"""
Васе нужно распечатать свой список дел на сегодня. Помогите ему:
напишите функцию, которая печатает все его дела.
Известно, что дел у Васи не больше 5000.

Внимание: в этой задаче не нужно считывать входные данные. Нужно написать
только функцию, которая принимает на вход голову списка и печатает его
элементы. Ниже дано описание структуры, которая задаёт узел списка.

Решение надо отправлять только в виде файла с расширением, которое
соответствует вашему языку. Иначе даже корректно написанное решение не пройдет
тесты.

Формат ввода
В качестве ответа сдайте только код функции, которая печатает элементы списка.
Длина списка не превосходит 5000 элементов. Список не бывает пустым.
Следуйте следующим правилам при отправке решений:

- По умолчанию выбран компилятор Make, выбор компилятора в данной задаче
недоступен.
- Решение нужно отправлять в виде файла с расширением соответствующем вашему
языку программирования.
- Для Java файл должен называться Solution.java, для C# – Solution.cs
- Для остальных языков программирования это имя использовать нельзя
(имя «solution» тоже).
- Для Go укажите package main.
Формат вывода
Функция должна напечатать элементы списка по одному в строке.
"""
# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:  
        def __init__(self, value, next_item=None):  
            self.value = value  
            self.next_item = next_item

def solution(node):
    while node:
        print(node.value)
        node = node.next_item

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    solution(node0)
    # Output is:
    # node0
    # node1
    # node2
    # node3

if __name__ == '__main__':
    test()
    