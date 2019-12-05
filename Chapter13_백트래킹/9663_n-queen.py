def n_queen(chess, case, n):
    if n == 0:
        case.append(1)
        return

    for i, row in enumerate(chess):
        for j, v in enumerate(row):
            if v == 0:
                place_queen(chess, j, i)
                n_queen(chess, case, n-1)


def place_queen(chess, x, y):
    for i, row in enumerate(chess):
        chess[i][x] = 1
    for j, v in enumerate(chess[y]):
        chess[y][j] = 1
    if x < y:
        small = x
    else:
        small = y
    y_now = y - small
    x_now = x - small
    while not (y_now == len(chess) or x_now == len(chess)):
        chess[y_now][x_now] = 1
        y_now += 1
        x_now += 1

    y_now = y + x
    x_now = 0
    while not (y_now == -1 or x_now == len(chess)):
        chess[y_now][x_now] = 1
        y_now -= 1
        x_now += 1

    return


if __name__ == '__main__':
    k = int(input())

    l = [[0 for _ in range(k)] for _ in range(k)]

    case = []

    n_queen(l, case, k)
    print(case)
