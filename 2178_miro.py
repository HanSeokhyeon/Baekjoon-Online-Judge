from queue import Queue

count = 0


# def bfs_paths(miro, x, y):
#     miro[x][y] = 0
#     result = []
#     q = Queue()
#
#     q.put((start, [start]))
#
#     while q.qsize() > 0:
#         node, path = q.get()
#
#         if node == end:
#             result.append(path)
#             break
#         else:
#             for m in graph[node] - set(path):
#                 q.put((m, path + [m]))
#
#     return len(result[0])


if __name__ == '__main__':
    n, m = map(int, input().split())
    miro = [list(map(int, input())) for _ in range(n)]

    # for
    # print(bfs_paths(, (1, 1), (n, m)))
