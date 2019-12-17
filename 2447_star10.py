def stars(star):
    tmp = []
    length = len(star)
    for i in range(3 * length):
        if i // length == 1:
            tmp.append(star[i % length] + " " * length + star[i % length])
        else:
            tmp.append(star[i % length] * 3)
    return tmp

if __name__ == '__main__':
    n = int(input())
    k = 1
    idx = 1
    while n != k:
        k = 3 ** idx
        idx += 1
    idx -= 2

    star = ["***", "* *", "***"]
    for i in range(idx):
        star = stars(star)

    for i in star:
        print(i)