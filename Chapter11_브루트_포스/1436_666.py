if __name__ == '__main__':
    n = int(input())
    count = 0
    now = 0
    while count != n:
        now += 1
        if str(now).count("666") != 0:
            count += 1
    print(now)