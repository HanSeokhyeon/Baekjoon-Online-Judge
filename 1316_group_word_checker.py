if __name__ == '__main__':
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    count = 0
    for word in words:
        no_repeat_word = [word[0]]
        before = word[0]
        for i, c in enumerate(word):
            if c == before:
                continue
            else:
                no_repeat_word.append(c)
            before = c
        no_repeat_word_set = set(no_repeat_word)
        if len(no_repeat_word) == len(no_repeat_word_set):
            count += 1

    print(count)