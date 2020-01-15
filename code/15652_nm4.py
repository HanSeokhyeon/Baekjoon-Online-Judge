import sys
read = sys.stdin.readline

n, m = map(int, read().strip().split())


def array(arr, k):
    arr = sorted(arr)

    def generate(chosen, start):
        if len(chosen) == k:
            print(" ".join(map(str, chosen)))
            return

        for i in arr[start:]:
            chosen.append(i)
            generate(chosen, i-1)
            chosen.pop()

    generate([], 0)


array(list(range(1, n+1)), m)


# def sequence(n ,l, topick):
#     if topick == 0:
#         print(" ".join(map(str, l)))
#         return
#
#     if len(l) == 0:
#         smallest = 1
#     else:
#         smallest = l[-1]
#
#     for next_v in range(smallest, n+1):
#         l.append(next_v)
#         sequence(n, l, topick-1)
#         l.pop()
#
#
# if __name__ == '__main__':
#     n, m = map(int, input().split())
#
#     sequence(n, [], m)