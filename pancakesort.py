class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        n = len(arr)
        for target in range(n, 1, -1):
            idx = arr.index(target)
            arr[:idx+1] = reversed(arr[:idx+1])
            result.append(idx + 1)
            arr[:target] = reversed(arr[:target])
            result.append(target)
    
        return result
