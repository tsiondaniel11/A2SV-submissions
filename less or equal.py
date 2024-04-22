n,k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()

low = 1
high = 10**9
result = -1  #

while low <= high:
    mid = (low + high) // 2
    count = 0
    for num in a:
        if num <= mid:
            count += 1

    if count == k:
        result = mid
        break
    elif count < k:
        low = mid + 1
    else:
        high = mid - 1

print(result)
