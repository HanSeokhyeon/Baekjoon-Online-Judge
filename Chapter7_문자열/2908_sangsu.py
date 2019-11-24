if __name__ == '__main__':
    n1, n2 = map(lambda x: x[::-1], input().split())
    print(max(n1, n2))
