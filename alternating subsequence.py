t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    maximum = a[0]
    total =0
    for i in range(1,n):
        if a[i] *a[i-1]>= 0:
            maximum = max(maximum,a[i])
        else:
            total += maximum
            maximum = a[i]

    print(total +maximum)
