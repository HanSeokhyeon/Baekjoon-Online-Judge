"""
15655 N과 M (6)

N개의 자연수 중에서 M개를 고른 수열
고른 수열은 오름차순이어야 한다.

시작 지점을 걸어주자.
"""

import sys
read = sys.stdin.readline

n, m = map(int, read().strip().split())
numbers = list(map(int, read().strip().split()))


def array(arr, k):
    arr = sorted(arr)

    def generate(chosen, start):
        if len(chosen) == k:
            print(" ".join(map(str, chosen)))
            return

        for i, num in enumerate(arr[start:]):

            chosen.append(num)
            generate(chosen, start+i+1)
            chosen.pop()

    generate([], 0)


array(numbers, m)
