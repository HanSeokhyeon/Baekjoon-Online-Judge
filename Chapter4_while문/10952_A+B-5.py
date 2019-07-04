num = list(map(int, input().split()))
while any(num) != 0:
    print(sum(num))
    num = list(map(int, input().split()))
