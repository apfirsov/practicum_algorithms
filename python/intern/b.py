def calculate_rocket_time(log):
    log.sort()
    rockets_time = {}
    for timestamp, status, id in log:
        if id not in rockets_time:
            rockets_time[id] = (0, 0)
        # Порядок гарантирвоан
        if status == 'A':
            rockets_time[id] = (rockets_time[id][0], timestamp)
        elif status in ('S', 'C'):
            rockets_time[id] = (
                rockets_time[id][0] + timestamp - rockets_time[id][1],
                0
            )

    return [str(rockets_time[id][0]) for id in sorted(rockets_time.keys())]


def read_input():
    n = int(input())
    log = [
        (lambda d, h, m, i, s: (int(d)*24*60 + int(h)*60 + int(m), s, int(i)))(
            *input().strip().split()
        )
        for _ in range(n)
    ]
    return log


if __name__ == '__main__':
    print(' '.join(calculate_rocket_time(read_input())))
