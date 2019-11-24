def check_prime_number(x):
    if x < 2:
        return False
    else:
        for i in range(2, x//2+1):
            if x % i == 0:
                return False
        return True


if __name__ == '__main__':
    m = int(input())
    n = int(input())
    prime_number = []
    for x in range(m, n+1):
        if check_prime_number(x):
            prime_number.append(x)
    if len(prime_number) == 0:
        print("-1")
    else:
        print(sum(prime_number))
        print(prime_number[0])