"""
2455 지능형 기차

역 4개를 지나가며 사람들이 내리고 타는데
기차에 가장 많은 사람이 탔을 때 사람 수를 출력하라.

알고리즘: 시뮬레이션

1. 4번 반복
    1. 내리는 사람 수 만큼 빼고
    2. 타는 사람 수 만큼 더하고
    3. 현재 인원을 최대 인원과 비교한다.
"""

import sys
read = sys.stdin.readline

max_passenger = 0
now_passenger = 0
for i in range(4):
    down, up = map(int, read().strip().split())
    now_passenger -= down
    now_passenger += up
    if now_passenger > max_passenger:
        max_passenger = now_passenger

print(max_passenger)