"""
2751 수 정렬하기 2

정렬하자
"""
import heapq
import sys
read = sys.stdin.readline

n = int(read())
hq = []
for _ in range(n):
    heapq.heappush(hq, int(read()))
for _ in range(n):
    print(heapq.heappop(hq))