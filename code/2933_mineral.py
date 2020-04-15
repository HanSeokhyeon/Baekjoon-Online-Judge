"""
2933 미네랄

왼쪽 오른쪽 번갈아가며 막대를 던진다.
미네랄을 만나면 파괴된다.
미네랄이 공중에 떠 있으면 아래로 떨어진다.
주어진대로 막대를 던진 후의 모습을 출력하라.

알고리즘: DFS or BFS

8 8
........
........
...x.xx.
...xxx..
..xxx...
..x.xxx.
..x...x.
.xxx..x.
5
6 6 4 3 1

왼6
........
........
.....xx.
....xx..
..x.x...
..xxxxx.
..xx..x.
.xxx..x.

오6
........
........
.....x..
...xxx..
..xxx...
..x.xxx.
..x...x.
.xxx..x.

왼4
........
........
.....x..
...xxx..
...xx...
..x.xxx.
..x...x.
.xxx..x.

오3
........
........
.....x..
...xxx..
...xx...
..x.xxx.
..x...x.
.xxx..x.

왼1
........
........
........
........
.....x..
..xxxx..
..xxx.x.
..xxxxx.
"""