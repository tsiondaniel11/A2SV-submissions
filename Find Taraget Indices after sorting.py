class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        sortednums = sorted(nums)
        for i in range(len(sortednums)):
            if sortednums[i] == target:
                ans.append(i)
        return ans
