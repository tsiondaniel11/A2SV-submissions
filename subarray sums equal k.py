class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        prefixsum =0
        count =0
        for num in nums:
            prefixsum += num
            diff = prefixsum- k
            if diff in dic:
                count += dic[diff]
            if prefixsum not in dic:
                dic[prefixsum] =1
            else:
                dic[prefixsum] += 1
                    
        return count
