class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if  not root:
            return True
        return self.symmetric(root.left,root.right)
    def symmetric(self,leftr,rightr):
        if not leftr and not rightr:
            return True
        if not leftr or not rightr:
            return False
        if leftr.val != rightr.val:
            return False
        return self.symmetric(leftr.left,rightr.right) and self.symmetric(leftr.right,rightr.left)
        
