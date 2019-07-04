n, x = input().split()
n, x = map(int, [n, x])

a = list(map(int, input().split()))

b = [str(i) for i in a if i < x]

print(" ".join(b))