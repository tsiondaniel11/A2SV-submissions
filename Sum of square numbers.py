class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a ,b=0,0
        while a*a +b*b <= c:
                if a * a + b * b == c:
                   return True
                b += 1
                a += 1
        return False

