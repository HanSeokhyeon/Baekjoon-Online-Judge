def permutations(n, l, topick):
    if topick == 0:
        print(" ".join(map(str, l)))
        return

    residual = list(map(lambda x: x+1, range(n)))
    for e in l:
        residual.remove(e)
    for next in residual:
        l.append(next)
        permutations(n, l, topick-1)
        l.pop()


if __name__ == '__main__':
    n, m = map(int, input().split())

    per = permutations(n, [], m)
