count = 0

def cut_chocolate(w, h):
    global count
    if w == 1 and h == 1:
        return
    count += 1
    if w >= h:
        if w % 2 == 0:
            cut_chocolate(w//2, h)
            cut_chocolate(w//2, h)
        else:
            cut_chocolate(w//2+1, h)
            cut_chocolate(w//2, h)
    else:
        if h % 2 == 0:
            cut_chocolate(w, h//2)
            cut_chocolate(w, h//2)
        else:
            cut_chocolate(w, h//2+1)
            cut_chocolate(w, h//2)

if __name__ == '__main__':
    n, m = map(int, input().split())

    cut_chocolate(n, m)
    print(count)