n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
less_elements =[]

for i in b:
    count = 0
    for j in a:
        if i > j:
            count += 1
    less_elements.append(count)
print(less_elements)
