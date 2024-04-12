def counting_sort(arr):
    frequency = [0] * 100
    for num in arr:
        frequency[num] += 1
    
    return frequency
def main():
    n = int(input().strip())  
    arr = list(map(int, input().split()))  
    result = counting_sort(arr)
    for freq in result:
        print(freq, end=' ')
main()
