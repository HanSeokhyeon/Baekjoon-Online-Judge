"""
1707 이분그래프

정점의 집합을 둘로 나누었을때 정점끼리 인접하지 않는다면 그걸 이분그래프라고 한다.

알고리즘: DFS

"""

import sys
read = sys.stdin.readline


def bfs(start):
    q = [start]
    global g
    g[0][start] = True
    visit = {}
    group = True
    result = 'YES'
    while q:
        new_q = []
        for now in q:
            for nxt in graph[now]:
                if (now, nxt) not in visit:
                    visit[(now, nxt)] = True
                    visit[(nxt, now)] = True
                    new_q.append(nxt)
                    if nxt in g[group]:
                        result = 'NO'
                    g[not group][nxt] = True
        group = not group
        q = new_q

    return result, g


def dfs(start):
    q = [(start, True)]
    global g
    g[0][start] = True
    visit = {}
    result = 'YES'
    while q:
        now, group = q.pop()
        for nxt in graph[now]:
            if (now, nxt) not in visit:
                visit[(now, nxt)] = True
                visit[(nxt, now)] = True
                q.append((nxt, not group))
                if nxt in g[group]:
                    result = 'NO'
                g[not group][nxt] = True

    return result, g


for _ in range(int(read())):
    v, e = map(int, read().split())
    edges = [list(map(int, read().split())) for _ in range(e)]

    graph = {i+1:[] for i in range(v)}
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    g = [{}, {}]
    for i in range(1, v+1):
        if i in g[0] or i in g[1]:
            continue
        answer, (g1, g2) = dfs(i)
        if answer == 'NO':
            break
    print(answer)
