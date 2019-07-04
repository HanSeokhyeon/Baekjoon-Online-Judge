t = int(input())

for i in range(t):
    num = list(map(int, input().split()))
    print("Case #%d: %d + %d = %d" % (i+1, num[0], num[1], sum(num)))