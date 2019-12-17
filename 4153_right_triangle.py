if __name__ == '__main__':
    a = b = c = 1
    case = []
    while a + b + c is not 0:
        a, b, c = map(int, input().split())
        case.append([a, b, c])
    case.pop()

    for abc in case:
        abc.sort()
        if abc[0]**2 + abc[1]**2 == abc[2]**2:
            print("right")
        else:
            print("wrong")
