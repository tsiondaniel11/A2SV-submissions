n = int(input())
a = list(map(int,input().split()))
current_num = 0
swap_num = 0
for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] > a[j + 1]:
            current_num = a[j]
            a[j] = a[j + 1]
            a[j + 1] = current_num
            swap_num += 1
a = sorted(a)
print(f"Array is sorted in {swap_num} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[len(a) - 1]}")
