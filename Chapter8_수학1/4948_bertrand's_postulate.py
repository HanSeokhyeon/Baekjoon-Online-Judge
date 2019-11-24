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


def check_prime_number_up_to(n):
    seive = [False, False] + [True] * (n-1)
    for i, e in enumerate(seive):
        if e:
            k = i * 2
            while k <= n:
                seive[k] = False
                k += i
    return seive


if __name__ == '__main__':
    case = []
    n = 1
    while n:
        n = int(input())
        case.append(n)
    case.pop()

    for n in case:
        primes = check_prime_number_up_to(2*n)[n+1:]
        print(sum(primes))
