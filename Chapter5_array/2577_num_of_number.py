num = [input() for i in range(3)]

mul = str(eval('*'.join(num)))

num_of_num = [0] * 10
for n in mul:
    num_of_num[int(n)] += 1

for n in num_of_num:
    print(n)