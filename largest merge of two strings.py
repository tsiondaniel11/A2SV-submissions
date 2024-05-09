class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        merge =""
        i, j  = 0,0
        while i< len(word1) and j  < len(word2):
            if word1[i:] > word2[j:]:
                   merge+=(word1[i])
                  
                   i+=1
            else:
                   merge+=(word2[j])
                   
                   j+=1
        merge +=  word1[i:] + word2[j:]

        return merge
