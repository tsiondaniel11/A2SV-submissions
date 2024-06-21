class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start =0
        end =0
        for i in range (len(nums)):
            if(nums[i] == 0):
                k-=1
            while(k<0):
                k+=1-nums[start]
                start +=1
            end = max(end, i-start+1)
        return end
