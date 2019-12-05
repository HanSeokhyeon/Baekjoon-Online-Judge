if __name__ == '__main__':
    n = int(input())
    data = [int(input()) for _ in range(n)]
    data = sorted(data)

    print("\n".join(map(str, data)))