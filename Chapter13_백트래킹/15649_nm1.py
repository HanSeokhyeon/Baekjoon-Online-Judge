import itertools


if __name__ == '__main__':
    n, m = map(int, input().split())

    per = list(itertools.permutations(list(range(n)), m))

    for p in per:
        p = map(lambda x: x+1, p)
        print(" ".join(map(str, p)))


