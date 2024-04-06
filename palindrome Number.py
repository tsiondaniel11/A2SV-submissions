class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        num =0
        temp = x
        while temp != 0:
            n = temp %10
            num = num*10 +n
            temp //=10

        return num == x
