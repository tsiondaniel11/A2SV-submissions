class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count =0
        prefixsum =0
        prefix_map ={0:1}
        for num in nums:
            prefixsum += num 
            remain = prefixsum % k
            if remain < 0:
                prefixsum += k
            if  remain in prefix_map:
                count += prefix_map[remain]
                prefix_map[remain] +=1
            else:
                prefix_map[remain] =1
        return count
