"""
15664 N과 M (10)

N개의 자연수 중에서 M개를 고른 수열
고른 수열은 비내림차순이어야 한다.

chosen과 remain으로 나누어 공략하자.
remain을 set으로 바꾸어 중복을 제거하자.
start를 이전꺼 다음으로 설정하자.
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
            generate(chosen, start+i+1)
            chosen.pop()
            before = num

    generate([], 0)


function(numbers, m)
