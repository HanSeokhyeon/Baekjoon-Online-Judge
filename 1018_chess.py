def check_black(chess):
    count = 0
    for y, line in enumerate(chess):
        for x, c in enumerate(line):
            if (y+x) % 2 == 0:
                if c != 'B':
                    count += 1
            else:
                if c != 'W':
                    count += 1
    return count


def check_white(chess):
    count = 0
    for y, line in enumerate(chess):
        for x, c in enumerate(line):
            if (y+x) % 2 == 0:
                if c != 'W':
                    count += 1
            else:
                if c != 'B':
                    count += 1
    return count


if __name__ == '__main__':
    n, m = map(int, input().split())

    input_chess = []

    for i in range(n):
        input_chess.append(input())

    result = 1000000000000
    for i in range(n-7):
        for j in range(m-7):
            chess = []
            for k in range(8):
                chess.append(input_chess[i+k][j:j+8])
            white_error = check_white(chess)
            black_error = check_black(chess)
            result = min(result, min(white_error, black_error))

    print(result)
