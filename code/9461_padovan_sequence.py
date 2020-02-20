"""
9461 파도반 수열

1 1 1 2 2 3 4 5 7 9 12 16
을 보고 나는 점화식을
p[n] = p[n-1] + p[n-5]이라고 판단했는데
구글링하니 p[n] = p[n-2] + p[n-3]이라고 한다.

알고리즘: DP
"""

import sys
read = sys.stdin.readline

t = int(read().strip())
p = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16]

for _ in range(t):
    n = int(read().strip())
    if n <= len(p):
        print(p[n-1])
    else:
        for i in range(len(p)+1, n+1):
            p.append(p[i-2] + p[i-6])
        print(p[n-1])
