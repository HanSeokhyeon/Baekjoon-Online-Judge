#-*- coding:utf-8 -*-

"""
1463 1로 만들기

1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나우어 떨어지면, 2로 나눈다.
3. 1을 뺀다.

N을 위의 3 연산으로 1을 만드는 최소연산 횟수는?

1 <= N <= 1000000

알고리즘: 다이나믹 프로그래밍

1. Rn = Pi + min(Rn-1)
2. 1부터 출발해서 N까지 도착하는데 중간에 들리는 곳이 이미 최소횟수로 방문 되었다면 계산하지 않고 바로 저장해놓은 값을 더해서 쓴다.

1에서 N까지 간다.
2까지 가는데는 1+1(1)만가능
3까지 가는데는 2+1(2), 1*3(1) 가능
4까지 가는데는 3+1(2), 2*2(2) 가능
"""

import sys
read = sys.stdin.readline

n = int(read().strip())

r = [0 for _ in range(0, n+1)]


def dp(result, target, cnt):
    global r
    if result == 1:
        if r[target] == 0:
            r[target] = cnt
        else:
            r[target] = min(cnt, r[target])
        return
    else:
        if result % 3 == 0:
            if r[result // 3]:
                dp(1, target, cnt+r[result//3]+1)
            else:
                dp(result//3, target, cnt+1)
        if result % 2 == 0:
            if r[result // 2]:
                dp(1, target, cnt+r[result//2]+1)
            else:
                dp(result//2, target, cnt+1)
        if r[result-1]:
            dp(1, target, cnt+r[result-1]+1)
        else:
            dp(result-1, target, cnt+1)


for i in range(2, n+1):
    dp(i, i, 0)

print(r[n])
