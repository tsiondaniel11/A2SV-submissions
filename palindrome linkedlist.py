class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ans =[]
        while head:
            ans.append(head.val)
            head = head.next
        i ,j =0,len(ans)-1
        while i<j:
            if ans[i] != ans[j]:
                return False 
            i+=1
            j-=1
            
        return True    
