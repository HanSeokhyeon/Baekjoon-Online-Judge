save = {1: 0, 2: 1}


def frog(n):
    if n in save:
        return save[n]
    m = 1 + min(frog(n//2)+n%2, frog(n//3)+n%3)
    save[n] = m
    return m


k = int(input())
print(frog(k))