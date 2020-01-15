"""
15666 N과 M (12)

N개의 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다.

before로 중복 제거하고
start 거는데 -1을 해준다.
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

        before = -1
        for i, num in enumerate(arr[start:]):
            if before == num:
                continue
            chosen.append(num)
            generate(chosen, start+i)
            chosen.pop()
            before = num

    generate([], 0)


function(numbers, m)
