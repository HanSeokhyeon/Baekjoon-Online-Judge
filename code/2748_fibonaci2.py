#-*- coding:utf-8 -*-

"""
2748 피보나치 수 2

0, 1, 1, 2, 3, 4, 8, 13, ...
n번째 피보나치수를 구하라.

알고리즘: 다이나믹 프로그래밍

1. 재귀호출로 이미 계산하였던 n번째 피보나치수를 다시 계산하는것은 계산 낭비다.
2. 계산한 값은 저장해두자.
"""

import sys
read = sys.stdin.readline

n = int(read().strip())
r = [0, 1]
for i in range(n-1):
    r.append(r[i+1] + r[i])

print(r[-1])