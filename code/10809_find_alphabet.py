if __name__ == '__main__':
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    word = input()
    idx = []

    for a in alphabet:
        idx.append(word.find(a))

    idx = list(map(str, idx))
    print(" ".join(idx))