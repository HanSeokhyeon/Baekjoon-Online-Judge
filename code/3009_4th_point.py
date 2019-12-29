if __name__ == '__main__':
    points = [list(map(int, input().split())) for _ in range(3)]

    points = list(map(list, zip(*points)))

    new_points = []

    for x in points[0]:
        if points[0].count(x) is 1:
            new_points.append(x)
            break

    for y in points[1]:
        if points[1].count(y) is 1:
            new_points.append(y)
            break

    print("{} {}".format(*new_points))
