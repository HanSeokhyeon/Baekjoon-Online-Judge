"""
15665 N과 M (11)

N개의 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.

전과 같은 수면 건너띈다.
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

        before = -1
        for num in sorted(set(arr)):
            if before == num:
                continue
            chosen.append(num)
            generate(chosen)
            chosen.pop()

    generate([])


function(numbers, m)
