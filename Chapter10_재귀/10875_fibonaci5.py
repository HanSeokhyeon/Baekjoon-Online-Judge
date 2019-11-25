def fibonaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonaci(n-1) + fibonaci(n-2)


if __name__ == '__main__':
    m = int(input())
    print(fibonaci(m))