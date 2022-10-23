"""
C. Подпоследовательность
"""

def is_subsequence(s: str, t: str) -> bool:
    i = -1
    for symbol in s:
        i = t.find(symbol, i + 1)
        if i == -1:
            return False
    return True


def main() -> None:
    print(is_subsequence(input(), input()))


if __name__ == '__main__':
    main()