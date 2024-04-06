class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(n,n*2+1):
            if int(i %n) ==  0 and int(i%2)==0:
                return i
