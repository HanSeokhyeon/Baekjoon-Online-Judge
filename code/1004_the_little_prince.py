"""
1004 어린왕자

출발해서 도착까지 최소로 행성계의 경계를 지나라.

1. 모든 행성계에 대해
    1. 출발점과 도착점에 대해 속한지 안속하는지 구하라.
    2. r > d
"""

import sys
read = sys.stdin.readline


def get_distance(x_1, y_1, x_2, y_2):
    return ((x_1-x_2)**2 + (y_1-y_2)**2)**0.5


for _ in range(int(read())):
    x1, y1, x2, y2 = map(int, read().split())
    cnt = 0
    n = int(read())
    for _ in range(n):
        cx, cy, r = map(int, read().split())
        d1, d2 = get_distance(x1, y1, cx, cy), get_distance(x2, y2, cx, cy)
        if (d1 < r) != (d2 < r):
            cnt += 1

    print(cnt)
