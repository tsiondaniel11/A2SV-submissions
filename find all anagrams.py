class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
            result = []
            if len(s) < len(p):
                return result
            p_count = {}
            s_count = {}
            for i in range(len(p)):
                p_count[p[i]] = p_count.get(p[i],0)+1
                s_count[s[i]] = s_count.get(s[i], 0) + 1
            if len(p_count) == len(s_count) and all(s_count.get(char, 0) == p_count[char] for char in p_count):
                    result.append(0)
            for i in range(len(p), len(s)):
                if s[i - len(p)] in s_count:
                   s_count[s[i - len(p)]] -= 1
                   if s_count[s[i - len(p)]] == 0:
                       del s_count[s[i - len(p)]]
                s_count[s[i]] = s_count.get(s[i], 0) + 1
                if len(p_count) == len(s_count) and all(s_count.get(char, 0) == p_count[char] for char in p_count):
                    result.append(i - len(p) + 1)
        
            return result
