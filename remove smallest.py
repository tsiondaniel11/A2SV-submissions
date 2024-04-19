t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(len(a) - 1):
        if abs(a[i] - a[i + 1]) > 1:
            ans.append("No")
            break
    else:
        ans.append("yes")
for k in range(len(ans)):
    print(ans[k])
