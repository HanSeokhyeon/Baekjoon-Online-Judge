"""
11403 경로 찾기

가중치 없는 그래프 G
모든 정점 i, j에 대해서 i에서 j로 가는 경로가 존재하는지 리턴

알고리즘: DFS

1. 출력할 NxN 배열 선언
2. 입력 받은 graph를 dfs로 경로가 있는지 없는지 확인
"""


def dfs(x, y, graph):
    visit = {}
    stack = [x]
    first = True  # x -> x로 가는 경로를 찾을 때 first flag가 없으면 출발하자마자 도착으로 인지하기 때문에 first flag를 만들어준다.

    while stack:
        node = stack.pop()
        if node == y and not first:  # node가 도착지고 처음이 아니면
            return 1

        if node not in visit:
            visit[node] = True
            stack.extend(check_next(graph[node]))  # 다음 node로 올 수 있는 것들을 확인하여 stack에 추가
            first = False  # 처음은 지나갔으므로 first flag를 False

    return 0


def check_next(arr):  # arr는 node에 대한 1xN
    next_list = []
    for idx, v in enumerate(arr):
        if v == 1:
            next_list.append(idx)
    return next_list


if __name__ == '__main__':
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i, m in enumerate(matrix):
        for j, v in enumerate(m):
            result[i][j] = dfs(i, j, matrix)

    for i, m in enumerate(result):
        print(" ".join(map(str, m)))