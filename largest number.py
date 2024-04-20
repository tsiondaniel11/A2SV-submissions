class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        n = len(nums)
        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] + nums[j + 1] < nums[j + 1] + nums[j]:
                   nums[j], nums[j + 1] = nums[j + 1], nums[j]

   
        largest_num = ''.join(nums)
 
    
        if largest_num[0] == '0':
           return '0'

        return largest_num
