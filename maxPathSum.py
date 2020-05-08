# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def _pathSum(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left = self._pathSum(root.left)
        right = self._pathSum(root.right)
        max_s = max(max(left,right) + root.val,root.val)
        max_t = max(max_s, left+right+root.val)
        self.res = max(self.res,max_t)
        return max_s
    
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float("-inf")
        self._pathSum(root)
        return self.res
    
