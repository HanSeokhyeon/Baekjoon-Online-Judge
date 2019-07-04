n = int(input())
num = list(map(int, input().split()))

modified_num = [i / max(num) * 100 for i in num]
print(sum(modified_num)/len(modified_num))
