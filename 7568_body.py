def check_bigger(m1, m2):
    if m1[0] < m2[0]:
        if m1[1] < m2[1]:
            return 1
    return 0

if __name__ == '__main__':
    n = int(input())
    people = [list(map(int, input().split())) for _ in range(n)]

    score = []
    for i, p1 in enumerate(people):
        big = 0
        for p2 in people[:i] + people[i+1:]:
            big += check_bigger(p1, p2)
        score.append(big+1)

    print(" ".join(map(str, score)))