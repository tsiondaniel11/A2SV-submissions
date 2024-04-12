class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxsum = window_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            window_sum += nums[i]- nums[i-k]
            maxsum = max(maxsum, window_sum)
  
        return maxsum/k
