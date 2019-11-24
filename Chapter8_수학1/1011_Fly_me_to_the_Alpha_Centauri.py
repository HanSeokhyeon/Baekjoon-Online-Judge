if __name__ == '__main__':
    t = int(input())
    case = [list(map(int, input().split())) for _ in range(t)]

    for start, end in case:
        distance = end - start
        n = 0
        while n**2 <= distance:
            n += 1
        n -= 1

        if n**2 == distance:
            result = 2*n-1
        elif n**2 < distance <= n**2 + n:
            result = 2*n
        else:
            result = 2*n+1
        print(result)