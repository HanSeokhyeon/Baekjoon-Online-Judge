from queue import Queue

visit = {}


def bfs(graph, start):
    global visit
    visit_tmp = {}
    q = Queue()

    q.put(start)

    while q.qsize() > 0:
        node = q.get()

        if node not in visit_tmp:
            visit[node] = True
            visit_tmp[node] = True
            for next_node in graph[node]:
                q.put(next_node)

    return len(visit_tmp.keys())

if __name__ == '__main__':
    n = int(input())
    map = [list(map(int, input())) for _ in range(n)]

    graph1 = {(i, j): set() for i in range(n) for j in range(n) if map[i][j] != 0}
    for i, value in enumerate(graph1):
        left = (value[0], value[1] - 1)
        if left in graph1:
            graph1[value].add(left)
            graph1[left].add(value)
        right = (value[0], value[1] + 1)
        if right in graph1:
            graph1[value].add(right)
            graph1[right].add(value)
        up = (value[0] + 1, value[1])
        if up in graph1:
            graph1[value].add(up)
            graph1[up].add(value)
        down = (value[0] - 1, value[1])
        if down in graph1:
            graph1[value].add(down)
            graph1[down].add(value)

    answer = []
    for i, value in enumerate(graph1):
        if value not in visit:
            answer.append(bfs(graph1, value))
    answer.sort()
    print(len(answer))
    for v in answer:
        print(v)