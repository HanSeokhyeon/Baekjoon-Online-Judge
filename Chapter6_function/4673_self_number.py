def d(n, list_all):
    str_n = str(n)
    res = n + eval('+'.join(str_n))
    if res <= 10000:
        list_all.append(res)


if __name__ == '__main__':
    list_all = []
    for i in range(10000):
        d(i+1, list_all)
    set_all = set(list_all)

    self_number = [i+1 for i in range(10000)]

    for tmp in set_all:
        self_number.remove(tmp)

    for tmp in self_number:
        print(tmp)