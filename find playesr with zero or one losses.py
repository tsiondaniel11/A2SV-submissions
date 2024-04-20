class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        loosers = set()
        repeated = set()
        result = [] 
        for j in matches:
            if j[1] not in repeated:
                loosers.add(j[1])
                repeated.add(j[1])
            else:
                loosers.discard(j[1])
        for i in matches:
            if i[0] not in repeated:
                winners.add(i[0])
        winlist = sorted(list(winners))
        lostlist = sorted(list(loosers))
        result.append(list(winlist))
        result.append(list(lostlist))

        return result
