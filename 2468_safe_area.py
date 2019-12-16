#-*- coding:utf-8 -*-

"""
2차원 배열로 지역의 높이가 주어진다.
일정한 높이로 비가 오면 그 높이보다 낮은 지역은 물에 잠긴다.
잠기지 않은 영역의 최대인 경우를 출력하라.

알고리즘: DFS

1. 지역 높이의 min과 max를 구한다.
2. 물이 잠기는 상황을 높이 min+1부터 시작한다.
3. dfs로 탐색을 하는데 다음 노드로 넘어갈 때 물 높이보다 낮으면 다음 노드로 추가하지 않는다.
4. dfs가 실행된 횟수를 저장하고 이는 안전영역의 개수이다.
5. 물의 높이를 max-1까지 반복실행한다.
6. 안전영역의 개수중 최대값을 출력한다.
"""

import sys


def find_n_area(rain, area):
    visit = {}  # 방문을 체크하기 위한 딕셔너리

    def dfs(start):
        stack = [start]

        while stack:
            node = stack.pop()

            if node not in visit:
                visit[node] = True
                stack.extend(check_next(*node))
        return 1  # path마다 1씩 더해주기

    def check_next(x, y):
        next_list = []
        if x-1 >= 0 and area[x-1][y] > rain:
            next_list.append((x-1, y))  # 왼쪽 노드가 수면보다 높으면
        if y-1 >= 0 and area[x][y-1] > rain:
            next_list.append((x, y-1))  # 아래쪽
        if x+1 < len(area) and area[x+1][y] > rain:
            next_list.append((x+1, y))  # 오른쪽
        if y+1 < len(area) and area[x][y+1] > rain:
            next_list.append((x, y+1))  # 위쪽
        return next_list

    cnt = 0
    for i, row in enumerate(area):
        for j, v in enumerate(row):
            if (i, j) not in visit and area[i][j] > rain:
                cnt += dfs((i, j))  # 방문하지 않았고 수면보다 높으
    return cnt


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    area_data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    min_a, max_a = min(min(x) for x in area_data), max(max(x) for x in area_data)

    n_area = []
    for r in range(min_a-1, max_a):
        n_area.append(find_n_area(r, area_data))

    print(max(n_area))
