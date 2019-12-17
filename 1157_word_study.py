if __name__ == '__main__':
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    word = input().lower()
    result = []
    for a in alphabet:
        result.append(word.count(a))
    result_sorted = sorted(result)
    if result_sorted[-1] == result_sorted[-2]:
        print("?")
    else:
        print(alphabet[max(zip(result, range(len(result))))[1]].upper())
