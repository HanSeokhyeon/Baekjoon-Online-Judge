def stars(star):
    tmp = []
    length = len(star)
    for i in range(3 * length):
        if i // len(star)

if __name__ == '__main__':
    n = int(input())
    k = 1
    idx = 1
    while n != k:
        k = 3 ** idx
        idx += 1
    idx -= 1

    star = ["*"]
    for i in range(idx):
        star = stars(star)