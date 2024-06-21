class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i =0
        j = n-1
        maxarea =0
        while i<j:
          currarea = min(height[i],height[j])*(j-i)
          maxarea = max(maxarea,currarea)
          if height[i] <height[j]:
            i+=1
          else:
            j-=1
        return maxarea  
