class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        maxLength = 0
        charsSet = set()

        while j < len(s):
            if s[j] in charsSet:
              charsSet.remove(s[i])
              i += 1
            else:
               charsSet.add(s[j])
               length = j - i + 1
               maxLength = max(maxLength, length)
               j += 1
        return maxLength       
