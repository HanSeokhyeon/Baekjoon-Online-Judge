"""
1094 막대기

막대기를 규칙에 따라 잘라서 Xcm의 막대를 만들고 싶다.
처음 막대는 64
1. 막대 길이를 모두 더하고 합이 X보다 크면
    1. 가지고 있는 막대 중 가장 작은 걸 절반으로 자른다.
    2. 만약 자른 막대중 작은걸 하나 버리고 막대 길이의 합이 X와 같거나 크면 버리고 다시 반복

알고리즘: 시뮬레이션
"""

import sys
read = sys.stdin.readline

x = int(read().strip())
now = [64]
while sum(now) != x:
    divide = [now[-1]//2, now[-1]//2]
    if len(now) == 1:
        if sum(divide[:1]) >= x:
            now = divide[:1]
        else:
            now = divide
    else:
        tmp = now[:-1] + divide
        if sum(tmp[:-1]) >= x:
            now = tmp[:-1]
        else:
            now = tmp

print(len(now))