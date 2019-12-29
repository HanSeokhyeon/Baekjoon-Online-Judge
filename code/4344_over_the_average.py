c = int(input())

for i in range(c):
    tmp = list(map(int, input().split()))
    n = tmp[0]
    score = tmp[1:]
    average = sum(score) / len(score)
    over_the_average = [i for i in score if i > average]
    print('%.3f%%' % (len(over_the_average) / len(score) * 100))
