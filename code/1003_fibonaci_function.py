#-*- coding:utf-8 -*-

"""
1003 피보나치 함수

int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}

fibonacci(3)을 호출하면 0이 1번 리턴되고 1이 2번 리턴된다.
fibonacci(n)이 호출되면 0과 1이 각각 몇번 리턴되는지 구하라.
"""

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000)


def fibonacci(n):
    r = [(1, 0), (0, 1)]
    for a in range(n-1):
        r.append((r[a][0] + r[a+1][0], r[a][1] + r[a+1][1]))
    return r[n]


t = int(read().strip())
case = []
for i in range(t):
    case.append(int(read().strip()))

for c in case:
    print(" ".join(map(str, fibonacci(c))))
