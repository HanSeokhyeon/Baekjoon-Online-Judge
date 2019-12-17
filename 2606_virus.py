def dfs(graph, start):
    visit = {}
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visit:
            visit[node] = True
            next_node = reversed(graph[node])
            stack.extend(next_node)

    return visit.keys()

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    graph1 = {i+1: [] for i in range(n)}
    for _ in range(m):
        a, b = map(int, input().split())
        graph1[a].append(b)
        graph1[b].append(a)

    print(len(dfs(graph1, 1))-1)
