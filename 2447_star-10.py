def star(n):
    star_list = []
    if n == 3:
        star_list = [[1, 1, 1],
                     [1, 0, 1],
                     [1, 1, 1]]
    else:
        little_n = int(n/3)
        star_list = [[star[little_n], star[little_n], star[little_n]],
                     [star[little_n], [[0]*], star[little_n]],
                     [star[little_n], star[little_n], star[little_n]]]



def main():
    n = int(input())

    star(n)


if __name__ == '__main__':
    main()