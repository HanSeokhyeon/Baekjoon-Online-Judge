def apt(k, n):
    if k == 0:
        return n
    elif n == 1:
        return 1
    else:
        return apt(k-1, n) + apt(k, n-1)


def apt_iter(k, n):
    floor = list(range(1, n+1))
    for i in range(k-1):
        sum_n = 0
        next_floor = []
        for j in floor:
            sum_n += j
            next_floor.append(sum_n)
        floor = next_floor
    return sum(floor)


if __name__ == '__main__':
    t = int(input())
    case = [int(input()) for _ in range(t*2)]
    case = [(case[2*i], case[2*i+1]) for i in range(t)]

    for k, n in case:
        people = apt_iter(k, n)
        print(people)