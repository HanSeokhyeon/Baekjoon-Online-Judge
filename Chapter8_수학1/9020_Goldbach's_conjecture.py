def check_prime_number(x):
    if x < 2:
        return False
    if x in (2, 3):
        return True
    if x % 2 is 0 or x % 3 is 0:
        return False
    if x < 9:
        return True
    k, l = 5, x**0.5
    while k <= l:
        if x % k is 0 or x % (k+2) is 0:
            return False
        k += 6
    return True


if __name__ == '__main__':
    t = int(input())
    case = [int(input()) for _ in range(t)]

    for n in case:
        a = b = n//2
        while a > 1:
            if check_prime_number(a) and check_prime_number(b):
                break
            else:
                a -= 1
                b += 1
        print("{} {}".format(a, b))