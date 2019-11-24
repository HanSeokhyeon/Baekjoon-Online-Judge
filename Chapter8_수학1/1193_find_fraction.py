if __name__ == '__main__':
    x = int(input())
    sum_digonal = 0
    i = 1
    while x > sum_digonal:
        sum_digonal = sum(range(i))
        i += 1
    i -= 2
    remain = x - sum(range(i)) - 1
    a, b = 1+remain, i-remain
    if i % 2 == 1:
        a, b = b, a
    print("{}/{}".format(a, b))