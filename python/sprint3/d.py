from typing import List, Tuple


def get_result(kids: List[int], cookies: List[int]) -> int:
    kids.sort(reverse=True)
    cookies.sort(reverse=True)
    i = 0
    for kid in kids:
        if i < len(cookies) and kid <= cookies[i]:
            i += 1
    return i

def read_input() -> Tuple[List[int], List[int]]:
    _ = int(input())
    kids = [int(i) for i in input().split()]
    _ = int(input())
    cookies = [int(i) for i in input().split()]
    return kids, cookies


def main() -> None:
    print(get_result(*read_input()))


if __name__ == '__main__':
    main()
