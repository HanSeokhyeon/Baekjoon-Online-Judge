t = int(input())

for i in range(t):
    num = map(int, input().split())
    print("Case #%d: %d" % (i+1, sum(num)))
