n = int(input())

for i in range(n):
    print("%s%s" % (" " * (n-(i+1)), "*" * (i+1)))
