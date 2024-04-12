class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            index = i
            for j in range(i,len(nums)):
                if nums[index] > nums[j]:
                   index =j
            nums[i], nums[index] = nums[index], nums[i] 
        
