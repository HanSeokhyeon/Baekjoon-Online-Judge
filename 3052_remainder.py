num = [int(input()) for i in range(10)]
remainder = [i % 42 for i in num]

remainder = set(remainder)

print(len(remainder))