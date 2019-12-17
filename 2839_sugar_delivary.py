if __name__ == '__main__':
    n = int(input())
    result = -1
    for a in range(n//5, -1, -1):
        b = (n - a * 5) / 3
        if b == int(b):
            result = a + b
            break
    print(int(result))