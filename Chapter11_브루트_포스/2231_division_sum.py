if __name__ == '__main__':
    n = int(input())
    result = 0
    for i in range(n):
        division_i = list(map(int, list(str(i))))
        division_sum = i + sum(division_i)
        if n == division_sum:
            result = i
            break
    print(result)