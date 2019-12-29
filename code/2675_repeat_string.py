if __name__ == '__main__':
    n = int(input())
    m, word = [], []
    for i in range(n):
        tmp = input().split()
        m.append(int(tmp[0]))
        word.append(tmp[1])

    for m_, word_ in zip(m, word):
        result = list(map(lambda x: x*m_, word_))
        print("".join(result))