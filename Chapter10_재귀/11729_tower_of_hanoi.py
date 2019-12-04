def hanoi(n, from_pos, to_pos, aux_pos, step):
    if n == 1:
        step.append([from_pos, to_pos])
        return
    hanoi(n-1, from_pos, aux_pos, to_pos, step)
    step.append([from_pos, to_pos])
    hanoi(n-1, aux_pos, to_pos, from_pos, step)


if __name__ == '__main__':
    n = int(input())

    step = []
    hanoi(n, 1, 3, 2, step)
    print(len(step))
    for from_pos, to_pos in step:
        print("{} {}".format(from_pos, to_pos))

