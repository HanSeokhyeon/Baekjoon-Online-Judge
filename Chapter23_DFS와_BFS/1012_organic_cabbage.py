from queue import Queue

global_visit = {}


def bfs(graph, start):
    global global_visit
    q = Queue()
    q.put(start)

    while q.qsize() > 0:
        node = q.get()

        if node not in global_visit:
            global_visit[node] = True
            for next_node in graph[node]:
                q.put(next_node)

    return 1


if __name__ == '__main__':
    t = int(input())
    case = []
    for i in range(t):
        global_visit = {}
        m, n, k = map(int, input().split())
        bat = {}
        for _ in range(k):
            a, b = map(int, input().split())
            bat[(a, b)] = set()

        for v in bat:
            left = (v[0], v[1] - 1)
            if left in bat:
                bat[v].add(left)
                bat[left].add(v)
            right = (v[0], v[1] + 1)
            if right in bat:
                bat[v].add(right)
                bat[right].add(v)
            up = (v[0] + 1, v[1])
            if up in bat:
                bat[v].add(up)
                bat[up].add(v)
            down = (v[0] - 1, v[1])
            if down in bat:
                bat[v].add(down)
                bat[down].add(v)

        count = 0

        for value in bat:
            if value not in global_visit:
                count += bfs(bat, value)

        case.append(count)

    for c in case:
        print(c)