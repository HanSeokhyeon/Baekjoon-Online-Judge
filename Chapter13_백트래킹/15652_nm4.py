def sequence(n ,l, topick):
    if topick == 0:
        print(" ".join(map(str, l)))
        return

    if len(l) == 0:
        smallest = 1
    else:
        smallest = l[-1]

    for next_v in range(smallest, n+1):
        l.append(next_v)
        sequence(n, l, topick-1)
        l.pop()


if __name__ == '__main__':
    n, m = map(int, input().split())

    sequence(n, [], m)