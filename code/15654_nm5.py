"""
15654 N과 M (5)

N개의 자연수 중에서 M개를 고른 수열
즉, 조합을 말한다.
"""

import sys
read = sys.stdin.readline

n, m = map(int, read().strip().split())
numbers = list(map(int, read().strip().split()))


def combinations(arr, k):
    arr = sorted(arr)

    def generate(chosen):
        if len(chosen) == k:
            print(" ".join(map(str, chosen)))
            return

        for i in arr:
            if i in chosen:
                continue
            chosen.append(i)
            generate(chosen)
            chosen.pop()

    generate([])


combinations(numbers, m)
