"""
15663 N과 M (9)

N개의 자연수 중에서 M개를 고른 수열
"""

import sys
read = sys.stdin.readline

n, m = map(int, read().strip().split())
numbers = list(map(int, read().strip().split()))


def function(arr, k):
    arr = sorted(arr)

    def generate(chosen, remain):
        if len(chosen) == k:
            print(" ".join(map(str, chosen)))
            return

        for i, num in enumerate(sorted(set(remain))):
            chosen.append(num)
            remain.remove(num)
            generate(chosen, remain)
            remain.insert(i, num)
            chosen.pop()

    generate([], arr)


function(numbers, m)
