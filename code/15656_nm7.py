"""
15656 N과 M (7)

N개의 자연수 중에서 M개를 고른 수열
같은 수를 여러번 골라도 된다.

아무 조건 없이 돌리자.
"""

import sys
read = sys.stdin.readline

n, m = map(int, read().strip().split())
numbers = list(map(int, read().strip().split()))


def function(arr, k):
    arr = sorted(arr)

    def generate(chosen):
        if len(chosen) == k:
            print(" ".join(map(str, chosen)))
            return

        for num in arr:
            chosen.append(num)
            generate(chosen)
            chosen.pop()

    generate([])


function(numbers, m)
