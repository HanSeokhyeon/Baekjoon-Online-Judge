import math

def check_prime_number(x):
    if x < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(x)+1)):
            if x % i == 0:
                return False
        return True


if __name__ == '__main__':
    m, n = map(int, input().split())
    for x in range(m, n+1):
        if check_prime_number(x):
            print(x)