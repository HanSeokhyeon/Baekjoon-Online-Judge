if __name__ == '__main__':
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    all_alphabet = croatia_alphabet + alphabet
    word = input()
    count_alphabet = []
    for a in all_alphabet:
        count_alphabet.append(word.count(a))
        word = word.replace(a, '_')
    count_alphabet = map(lambda x: x+1 if x == -1 else x, count_alphabet)
    print(sum(count_alphabet))