#-*- coding:utf-8 -*-

"""
독일 로또는 1-49 중 6개를 고른다.
49가지 수 중 k개의 수를 골라 그 수만 가지고 번호를 고른다.
k=8이면 28가지가 나온다.
집합 S와 k가 주어지면, 수를 고르는 모든 방법 출력

알고리즘: DFS, 완전 탐색

1. DFS를 재귀로 만들어 트리를 계속 탐색한다.
"""
import sys
from itertools import combinations


def main_use_combination(lotto_set):
    comb = list(combinations(lotto_set, 6))
    for c in comb:
        print(" ".join(c))


def combination(arr, r):
    # arr = sorted(arr)

    def generate(chosen):
        if len(chosen) == r:
            print(" ".join(chosen))
            return

        if chosen:
            start = arr.index(chosen[-1]) + 1
        else:
            start = 0

        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()

    generate([])


def main_combination(lotto_set):
    combination(lotto_set, 6)


if __name__ == '__main__':
    n = 1
    while n != 0:
        line = sys.stdin.readline().split()
        n = int(line[0])
        s = list(line[1:])
        # main_use_combination(n, s)
        main_combination(n, s)
        print()
