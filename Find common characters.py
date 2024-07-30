class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
       res = Counter(words[0])
       for i in words:
            res = res & Counter(i)
       return list(res.elements())


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = Counter(words[0])
        for w in words:
            curr_cnt = Counter(w)
            for c in cnt:
                cnt[c] = min(cnt[c],curr_cnt[c])
        res =[]
        for c in cnt:
            for i in range(cnt[c]):
                res.append(c)
        return res
