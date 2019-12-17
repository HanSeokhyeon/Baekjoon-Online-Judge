if __name__ == '__main__':
    m = int(input())
    case = [list(map(int, input().split())) for i in range(m)]

    for h, w, n in case:
        room = (n-1) // h + 1
        floor = (n-1) % h + 1
        print("{0}{1:>02d}".format(floor, room))