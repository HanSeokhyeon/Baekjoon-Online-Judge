def hansu(n):
    if n < 10:
        return True
    str_n = str(n)
    diff = int(str_n[0]) - int(str_n[1])
    for i in range(len(str_n)-1):
        if int(str_n[i]) - int(str_n[i+1]) != diff:
            return False
    return True


def main():
    n = int(input())
    count = 0
    for i in range(n):
        if hansu(i+1):
            count += 1
    print(count)


if __name__ == '__main__':
    main()
