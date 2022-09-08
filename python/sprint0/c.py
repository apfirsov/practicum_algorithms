"""
Вам дана статистика по числу запросов в секунду к вашему любимому рекомендательному сервису.
Измерения велись n секунд.
В секунду i поступает qi запросов.
Примените метод скользящего среднего с длиной окна k к этим данным и выведите результат.

Формат ввода
В первой строке передаётся натуральное число n, количество секунд, в течение которых велись измерения. 1 ≤ n ≤ 10^5
Во второй строке через пробел записаны n целых неотрицательных чисел qi, каждое лежит в диапазоне от 0 до 10^3.
В третьей строке записано натуральное число k (1 ≤ k ≤ n) —– окно сглаживания.

Формат вывода
Выведите через пробел результат применения метода скользящего среднего к серии измерений.
Должно быть выведено n - k + 1 элементов, каждый элемент -— вещественное (дробное) число.
"""
from typing import List, Tuple

def moving_average(n: int, arr: List[int], window_size: int) -> List[float]:
        result = []
        current_sum = sum(arr[0:window_size])
        result.append(current_sum / window_size)
        for i in range(0, n - window_size):
            current_sum -= arr[i]
            current_sum += arr[i + window_size]
            current_avg = current_sum / window_size
            result.append(current_avg)
        return result

def read_input() -> Tuple[int, List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return n, arr, window_size

print(" ".join(map(str, moving_average(*read_input()))))
