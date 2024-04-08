if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    newarr =[]
    maxnum = max(arr)
    for i in arr:
        if i != maxnum:
            newarr.append(i)
    print(max(newarr))
