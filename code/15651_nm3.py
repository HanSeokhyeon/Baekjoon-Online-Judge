import sys
read = sys.stdin.readline

n, m = map(int, read().strip().split())


def array(arr, k):
    arr = sorted(arr)

    def generate(chosen):
        if len(chosen) == k:
            print(" ".join(map(str, chosen)))
            return

        for i in arr:
            chosen.append(i)
            generate(chosen)
            chosen.pop()

    generate([])


array(list(range(1, n+1)), m)


# def sequence(n, l ,topick):
#     if topick == 0:
#         print(" ".join(map(str, l)))
#         return
#
#     for next in range(1, n+1):
#         l.append(next)
#         sequence(n, l, topick-1)
#         l.pop()
#
#
# if __name__ == '__main__':
#     n, m = map(int, input().split())
#
#     sequence(n, [], m)