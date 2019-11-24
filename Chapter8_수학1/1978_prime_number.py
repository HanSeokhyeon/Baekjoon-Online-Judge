def check_prime_number(x):
    if x < 2:
        return False
    else:
        for i in range(2, x//2+1):
            if x % i == 0:
                return False
        return True


if __name__ == '__main__':
    n = int(input())
    case = map(int, input().split())
    count = 0
    for m in case:
        count += check_prime_number(m)
    print(count)