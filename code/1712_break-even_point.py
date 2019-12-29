if __name__ == '__main__':
    a, b, c = map(int, input().split())
    if b >= c:
        n = -1
    else:
        n = int(a/(c-b))+1
    print(n)