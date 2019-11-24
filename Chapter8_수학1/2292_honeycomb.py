if __name__ == '__main__':
    n = int(input()) - 1
    i = 1
    while n > 0:
        n -= 6*i
        i += 1
    print(i)