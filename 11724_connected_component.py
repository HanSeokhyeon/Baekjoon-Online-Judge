#-*- coding:utf-8 -*-

"""
11724 연결 요소의 개수

방향이 없는 그래프
연결 요소의 개수를 출력하라.
N은 정점의 개수
M은 간선의 개수

알고리즘: DFS

1. 입력을 받아 그래프를 만든다.
2. DFS를 실행하며 실행 횟수를 저장한다.
3. 실행 횟수를 출력한다.

#############실패 요인###############
stack을 이용해 dfs를 구현하면 시간초과가 뜨고
재귀를 통해 dfs를 구현하면 런타임 에러가 떴다.

런타임 에러는
>>>sys.setrecursionlimit(10000)
로 재귀 제한 횟수를 늘려주면서 해결하였다.

이후 시간초과는
>>>input()
대신
>>>sys.stdin.readline()
을 이용하면서 해결하였다.
"""
import sys
sys.setrecursionlimit(10000)


def dfs(v):
    visit[v] = True

    for e in graph[v]:
        if not (visit[e]):
            dfs(e)


n, m = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n+1)]
visit = [False] * (n+1)
cnt = 0

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    if not (visit[i]):
        cnt += 1
        dfs(i)
print(cnt)
