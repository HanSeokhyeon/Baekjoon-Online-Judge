n = int(input())

for i in range(n):
    results = input()
    score, count = 0, 0
    for result in results:
        if result == 'O':
            score += 1 + count
            count += 1
        else:
            count = 0
    print(score)