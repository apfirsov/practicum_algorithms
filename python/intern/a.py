if __name__ == '__main__':
    n = int(input())
    result = []
    for _ in range(n):
        f, i, o, d, m, y = input().strip().split(',')
        symbols = set(f + i + o)
        sum = 0
        for symbol in d + m:
            sum += int(symbol)
        res = hex(len(symbols) + (ord(f.lower()[0])-96) * 256 + sum * 64)
        result.append(str(res)[-3:])
    print(' '.join(result))
