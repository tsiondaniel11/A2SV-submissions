class Solution: 
    def select(self, arr, i):
        index =i
        for j in range(i+1,n):
            if arr[j]<arr[index]:
                index =j
        arr[index],arr[i] = arr[i],arr[index]
    def selectionSort(self, arr,n):
        for i in range(n):
            self.select(arr,i)
        return arr
        
