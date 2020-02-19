"""
9095 1, 2, 3 더하기

숫자 N을 1, 2, 3을 더해 만들 수 있는 조합의 수를 출력

알고리즘: DP

top-down 전략
"""

save = {1: 1, 2: 1, 3: 2, 4: 7}


def frog(n):
    if n in save:
        return save[n]
    m = frog(n-1) + frog(n-2) + frog(n-3) + 1
    save[n] = m
    return m


t = int(input())
for _ in range(t):
    k = int(input())
    print(frog(k))
