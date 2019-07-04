import copy
n = int(input())
target = copy.deepcopy(n)
count = 1
while True:
    if n < 10:
        num = "0%d" % n
    else:
        num = str(n)
    res = int(num[0]) + int(num[1])
    if res < 10:
        res = "0%d" % res
    else:
        res = str(res)
    n = int("%s%s" % (num[1], res[1]))
    if n == target:
        break
    else:
        count += 1
print(count)