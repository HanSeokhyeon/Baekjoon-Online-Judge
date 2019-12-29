def sequence(n, l ,topick):
    if topick == 0:
        print(" ".join(map(str, l)))
        return

    for next in range(1, n+1):
        l.append(next)
        sequence(n, l, topick-1)
        l.pop()


if __name__ == '__main__':
    n, m = map(int, input().split())

    sequence(n, [], m)