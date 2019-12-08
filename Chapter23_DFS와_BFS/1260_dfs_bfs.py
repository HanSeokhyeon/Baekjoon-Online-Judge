from queue import Queue


def dfs(graph, start_node):
    visit = {}
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit[node] = True
            next_nodes = reversed(graph[node])
            stack.extend(next_nodes)

    return visit.keys()


def bfs(graph, start_node):
    visit = {}
    q = Queue()

    q.put(start_node)

    while q.qsize() > 0:
        node = q.get()
        if node not in visit:
            visit[node] = True
            for next_node in graph[node]:
                q.put(next_node)

    return visit.keys()

if __name__ == '__main__':
    n, m, v = map(int, input().split())

    graph1 = {i: [] for i in range(1, n+1)}
    for _ in range(m):
        a, b = map(int, input().split())
        graph1[a].append(b)
        graph1[b].append(a)
    for l in graph1:
        graph1[l] = sorted(graph1[l])
    print(" ".join(map(str, dfs(graph1, v))))
    print(" ".join(map(str, bfs(graph1, v))))