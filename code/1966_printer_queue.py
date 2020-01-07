"""
1966 프린터 큐

문서를 프린트하는데 중요도가 존재한다.
현재 문서보다 중요도가 높은 문서가 큐에 존재하면 현재 문서를 큐의 맨뒤로 보낸다.
어떤 한 문서가 몇번째로 인쇄되는지 출력하라.

알고리즘: 시뮬레이션

1. 가장 높은 중요도를 구한다.
2. 가장 높은 중요도가 나올때 까지 popleft와 append를 반복한다.
3. 가장 높은 중요도가 나오면 출력하고 cnt에 1을 더한다.
4. 원하는 문서의 중요도가 max가 되었고 큐에서 그 문서가 나오면 cnt를 출력한다.
"""

from collections import deque
import sys
read = sys.stdin.readline

t = int(read().strip())
for _ in range(t):
    n, m = map(int, read().strip().split())
    priority = list(map(int, read().strip().split()))
    max_prior = max(priority)

    q = deque()
    for i, p in enumerate(priority):
        q.append((i, p))

    cnt = 1

    while q:
        now, prior = q.popleft()
        if prior == max_prior:
            if now == m:
                print(cnt)
                break
            else:
                priority.remove(max_prior)
                max_prior = max(priority)
                cnt += 1
        else:
            q.append((now, prior))
