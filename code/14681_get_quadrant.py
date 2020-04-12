"""
14681 사분면 고르기

좌표가 주어지면 사분면을 출력하면 된다.
"""

x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)