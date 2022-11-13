"""
В известной компании Тындекс уже несколько лет работает очень популярный сервис Тындекс.Вода, занимающийся поливом людей, растений, зданий и всего остального, что можно полить без ущерба окружающим.
Пользователь указывает, что ему необходимо полить и сколько литров воды он готов на это потратить, после чего на место выезжает специальная бригада. В итоге для компании каждый заказ можно представить тройкой чисел:

время Start, когда бригада приняла заказ и выехала;
время End, когда бригада осуществила заказ и освободилась;
итоговая стоимость заказа Cost.
Для простоты обработки и хранения время задается одним целым числом, равным количеству минут, прошедших с начала запуска сервиса до искомого момента.
Продолжительность заказа считается равной величине End−Start.
Начальнику сервиса необходимо отчитаться перед вышестоящим начальством, поэтому он поручил вам несложную задачку — найти ответы на несколько запросов одного из двух типов:

Найти суммарную стоимость заказов, которые начались в заданный промежуток времени;
Найти суммарную продолжительность заказов, которые завершились в заданный промежуток времени;
В обеих статистиках промежутки считаются отрезками: в промежуток от Start до End входят все величины Start, Start+1, …, End−1, End.
"""
def rsq(arr, start, end):
    start_idx = -1
    left = 0
    right = len(arr)-1
    while left < right:
        mid = (left + right) // 2
        if start <= arr[mid][0]:
            right = mid
        else:
            left = mid + 1
    if left < len(arr) and start <= arr[left][0]:
        start_idx = left

    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right + 1) // 2
        if end >= arr[mid][0]:
            left = mid
        else:
            right = mid - 1
    end_idx = left

    res = 0
    if start_idx > 0 and end_idx >= 0:
        res = arr[end_idx][1] - arr[start_idx-1][1]
    return res


def execute_querys(start_costs, end_durations, querys):
    start_costs.sort()
    end_durations.sort()
    pref_cost = [(0, 0)] * (len(start_costs) + 1)
    pref_duration = [(0, 0)] * (len(start_costs) + 1)
    cost_sum = 0
    duration_sum = 0

    for i in range(1, len(pref_cost)):
        start, cost = start_costs[i-1]
        cost_sum += cost
        pref_cost[i] = (start, cost_sum)

        end, duration = end_durations[i-1]
        duration_sum += duration
        pref_duration[i] = (end, duration_sum)

    result = []
    for start, end, query_type in querys:
        if query_type == 1:
            result.append(str(rsq(pref_cost, start, end)))
        elif query_type == 2:
            result.append(str(rsq(pref_duration, start, end)))
    return result


def read_input():
    n = int(input())
    start_costs = [None] * n
    end_durations = [None] * n

    for i in range(n):
        start, end, cost = input().strip().split()
        start_costs[i] = (int(start), int(cost))
        end_durations[i] = (int(end), int(end) - int(start))

    q = int(input())
    querys = [
        (lambda s, e, t: (int(s), int(e), int(t)))(
            *input().strip().split()
        )
        for _ in range(q)
    ]

    return start_costs, end_durations, querys


if __name__ == '__main__':
    print(' '.join(execute_querys(*read_input())))
