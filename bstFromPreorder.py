# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        size = len(preorder)
        root = TreeNode(preorder[0])
        
        s = []
        s.append(root)
        i = 1
        while (i < size):
            temp = None
            
            while(len(s)>0 and preorder[i] > s[-1].val):
                temp = s.pop()
                
            if (temp != None):
                temp.right = TreeNode(preorder[i])
                s.append(temp.right)
            
            else:
                temp = s[-1]
                temp.left = TreeNode(preorder[i])
                s.append(temp.left)
            i = i+1
        
        return root
