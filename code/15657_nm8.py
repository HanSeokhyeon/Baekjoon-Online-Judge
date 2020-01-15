"""
15657 N과 M (8)

N개의 자연수 중에서 M개를 고른 수열
같은 수를 여러번 골라도 된다.
고른 수열은 비내림차순이어야 한다.

start 지점을 설정하되 start-1로 설정하자.
"""

import sys
read = sys.stdin.readline

n, m = map(int, read().strip().split())
numbers = list(map(int, read().strip().split()))


def function(arr, k):
    arr = sorted(arr)

    def generate(chosen, start):
        if len(chosen) == k:
            print(" ".join(map(str, chosen)))
            return

        for i, num in enumerate(arr[start:]):
            chosen.append(num)
            generate(chosen, start + i)
            chosen.pop()

    generate([], 0)


function(numbers, m)
