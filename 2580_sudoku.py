#-*- coding:utf-8 -*-

"""
2580 스도쿠

규칙은 기존 스도쿠와 같다.
빈칸 대신 0으로 주어졌을때
정답을 출력하라.

알고리즘: 백트래킹? DFS?

1. 스도쿠의 값이 0인 경우를 찾아 (k, l)를 저장한다.
2. (k, l)를 하나씩 호출한다.
3. 후보는 1-9로 만들어 놓고 가로, 세로, 사각형에서 나온 숫자들을 False로 바꿔서 후보에서 제외시킨다.
4. 리턴 받은 후보들로 0을 바꾸고 다시 dfs를 실행한다.
5. 모든 0을 확인하면 print하고 종료한다.
"""

import sys
r = sys.stdin.readline
s = [list(map(int, r().split())) for _ in range(9)]
zeros = []

for k, row in enumerate(s):
    for l, v in enumerate(row):
        if not v:
            zeros.append((k, l))


def make_candidate(pos):
    nums = [False] + [True for _ in range(9)]

    x = (pos[0]//3)*3
    y = (pos[1]//3)*3
    for i in range(x, x+3):
        for j in range(y, y+3):
            if s[i][j]:
                nums[s[i][j]] = False

    for i in range(9):
        if s[pos[0]][i]:
            nums[s[pos[0]][i]] = False
        if s[i][pos[1]]:
            nums[s[i][pos[1]]] = False

    return [i for i, e in enumerate(nums) if e]


def dfs(cnt):
    if cnt == len(zeros):
        for row_ in s:
            print(" ".join(map(str, row_)))
        sys.exit(0)
    else:
        for num in make_candidate(zeros[cnt]):
            s[zeros[cnt][0]][zeros[cnt][1]] = num
            dfs(cnt+1)
            s[zeros[cnt][0]][zeros[cnt][1]] = 0


dfs(0)
