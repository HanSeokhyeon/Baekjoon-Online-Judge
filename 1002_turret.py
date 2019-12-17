if __name__ == '__main__':
    t = int(input())
    case = [map(int, input().split()) for _ in range(t)]

    for x1, y1, r1, x2, y2, r2 in case:
        d = ((x2-x1)**2 + (y2-y1)**2)**0.5
        if r1 > r2:
            longer = r1
            smaller = r2
        else:
            longer = r2
            smaller = r1

        if longer < d:
            sum_r = longer + smaller
            if sum_r > d:
                point = 2
            elif sum_r == d:
                point = 1
            elif sum_r < d:
                point = 0
        else:
            if longer - smaller < d:
                point = 2
            elif longer - smaller == d:
                if d == 0:
                    point = -1
                else:
                    point = 1
            elif longer - smaller > d:
                point = 0



        print(point)