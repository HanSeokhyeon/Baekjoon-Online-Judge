import sys
read = sys.stdin.readline

n, m = map(int, read().strip().split())


def permutations(arr, k):
    arr = sorted(arr)

    def generate(chosen):
        if len(chosen) == k:
            print(" ".join(map(str, chosen)))

        for i in arr:
            if i in chosen:
                continue
            chosen.append(i)
            generate(chosen)
            chosen.pop()

    generate([])


permutations(list(range(1, n+1)), m)
# def permutations(n, l, topick):
#     if topick == 0:
#         print(" ".join(map(str, l)))
#         return
#
#     residual = list(map(lambda x: x+1, range(n)))
#     for e in l:
#         residual.remove(e)
#     for next in residual:
#         l.append(next)
#         permutations(n, l, topick-1)
#         l.pop()
#
#
# if __name__ == '__main__':
#     n, m = map(int, input().split())
#
#     per = permutations(n, [], m)
