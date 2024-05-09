class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s = list(s)
        edited =[]
        j =0
        for i in range(len(s)) :
            if j < len(spaces) and i == spaces[j]:
                   edited.append(" ")
                   j+=1
            edited.append(s[i])
        return  "".join(edited)
