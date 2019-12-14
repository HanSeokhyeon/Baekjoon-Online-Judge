def check_rect(rect):
    d = []
    for i in range(len(rect)):
        for j in range(i+1, len(rect)):
            d.append(get_length(*rect[i], *rect[j]))

    d = sorted(d)
    if d[0] == d[1] == d[2] == d[3]:
        if d[4] == d[5]:
            if int(d[0]*(2**0.5)*10000000) == int(d[4]*10000000):
                return 1
    return 0


def get_length(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5


if __name__ == '__main__':
    c = int(input())

    for i in range(c):
        rectangle = [tuple(map(int, input().split())) for _ in range(4)]

        print(check_rect(rectangle))
