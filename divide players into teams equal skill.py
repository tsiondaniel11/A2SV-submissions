def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i ,j = 0,len(skill)-1
        ans = 0
        while i <j:
            if skill[0] +skill[-1] != skill[i] + skill[j]:
                return -1
            ans += skill[i] * skill[j]
            i += 1
            j -=1
        return ans
        
