if __name__ == '__main__':
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))

    max_result = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                result = cards[i] + cards[j] + cards[k]
                if result <= m and max_result < result:
                    max_result = result
    print(max_result)