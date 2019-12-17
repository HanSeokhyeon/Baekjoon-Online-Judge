if __name__ == '__main__':
    x, y, w, h = map(int, input().split())
    x_dis = [w - x, x]
    y_dis = [h - y, y]
    print(min(x_dis + y_dis))