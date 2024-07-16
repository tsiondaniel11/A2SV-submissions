class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefixsum =0
        prefix_sum =[]
        for i in range(len(nums)):
            prefixsum += nums[i]
            prefix_sum.append(prefixsum)
        return prefix_sum
