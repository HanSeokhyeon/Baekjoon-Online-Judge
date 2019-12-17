num = list(map(int, input().split()))

num_sorted = sorted(num)
num_reverse = list(reversed(num_sorted))

if num == num_sorted:
    print("ascending")
else:
    if num == num_reverse:
        print("descending")
    else:
        print("mixed")

