#-*- coding:utf-8 -*-

"""
14502 연구소

NxM인 구역에 바이러스, 벽, 빈 칸이 존재한다.
바이러스는 2, 벽은 1, 빈 칸은 0이다.
바이러스를 벽으로 감싸지 않는다면 전부 바이러스로 퍼지게된다.
벽은 3개 세울 수 있으면 3개를 꼭 전부 세워야한다.
안전 영역은 바이러스가 퍼지고 남은 빈 칸이다.
안전 영역이 최댓값을 구하자.

알고리즘: DFS

1. 바이러스의 위치를 확인한다.
2. 벽을 세울 위치 3개를 정한 후 dfs로 안전영역을 찾는다.
3. dfs로 안전영억을 찾을 때는 영역에 주변에 2가 존재하면 감염 구역으로 여긴다.
"""
from copy import deepcopy


def dfs(start, graph):
    stack = [start]
    virus = False  # virus가 포함된 경로라면 안전영역을 카운트할 때 쓰이면 안되서 flag를 추가
    cnt = 0

    while stack:
        node = stack.pop()

        if graph[node[0]][node[1]] == 2:  # 현재 node가 2라면 virus flag를 True
            virus = True

        if graph[node[0]][node[1]] != 1:  # 현재 node가 1이면 이미 방문
            graph[node[0]][node[1]] = 1  # 방문한 node를 1로 대입
            stack.extend(check_next(*node, graph))  # 가능한 다음 node를 stack에 추가

            cnt += 1  # 방문하지 않은 node를 탐색할 때마다 count

    if virus:  # virus가 포함된 경로면 return 0
        return 0
    else:  # 안전 영역이면 return cnt
        return cnt


def check_next(x, y, graph):
    next_list = []
    if x-1 >= 0 and graph[x-1][y] % 2 == 0:  # 왼쪽 노드가 값이 0이나 2면
        next_list.append((x-1, y))
    if y-1 >= 0 and graph[x][y-1] % 2 == 0:  # 아래쪽 노드가 값이 0이나 2면
        next_list.append((x, y-1))
    if x+1 < len(graph) and graph[x+1][y] % 2 == 0:  # 오른쪽 노드가 값이 0이나 2면
        next_list.append((x+1, y))
    if y+1 < len(graph[0]) and graph[x][y+1] % 2 == 0:  # 위쪽 노드가 값이 0이나 2면
        next_list.append((x, y+1))
    return next_list


if __name__ == '__main__':
    n, m = map(int, input().split())
    lab = [list(map(int, input().split())) for _ in range(n)]

    zeros = []
    for i, row in enumerate(lab):
        for j, v in enumerate(row):
            if v == 0:
                zeros.append((i, j))  # 벽을 놓을 수 있는 0의 위치를 모두 저장

    result = []
    for i in range(0, len(zeros)):  # 첫번째 벽
        for j in range(i+1, len(zeros)):  # 두번째 벽
            for k in range(j+1, len(zeros)):  # 세번째 벽
                lab_with_wall = deepcopy(lab)  # 원래 연구실을 복사
                lab_with_wall[zeros[i][0]][zeros[i][1]] = 1  # 벽1
                lab_with_wall[zeros[j][0]][zeros[j][1]] = 1  # 벽2
                lab_with_wall[zeros[k][0]][zeros[k][1]] = 1  # 벽3

                safe = 0  # 안전 영역 넓이

                for l, row in enumerate(lab_with_wall):
                    for m, v in enumerate(row):
                        if v != 1:  # 시작 노드가 벽이 아니라면
                            safe += dfs((l, m), lab_with_wall)

                result.append(safe)

    print(max(result))  # 가장 큰 안전 영역 넓이를 출력
