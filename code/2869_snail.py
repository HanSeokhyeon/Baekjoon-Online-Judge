import math

if __name__ == '__main__':
    a, b, v = map(int, input().split())
    day = (v-b) / (a-b)
    v = a * day - b * (day-1)
    print(math.ceil(day))