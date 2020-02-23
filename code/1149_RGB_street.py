"""
1149 RGB 거리

색을 RGB로 칠할 예정인데 이웃집이랑 색이 같으면 안된다.
각 집마다 RGB로 칠하는 가격이 주어질 때
최소 금액을 구해라.

알고리즘: DP

1. 처음 시작을 무엇으로 하냐에 따라 경우가 나뉜다. 3가지
2. R을 택했으면 그다음은 GB중 작은 값이된다.
"""

import sys
read = sys.stdin.readline

n = int(read().strip())
dp = [list(map(int, read().strip().split()))]
for i in range(1, n):
    r, g, b = map(int, read().strip().split())
    nxt_r = r + min(dp[i-1][1], dp[i-1][2])
    nxt_g = g + min(dp[i-1][0], dp[i-1][2])
    nxt_b = b + min(dp[i-1][0], dp[i-1][1])
    dp.append([nxt_r, nxt_g, nxt_b])

print(min(dp[n-1]))
