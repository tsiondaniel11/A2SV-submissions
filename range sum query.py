class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0]
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            self.prefix_sum.append(prefix_sum)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right+1 ] - self.prefix_sum[left]

