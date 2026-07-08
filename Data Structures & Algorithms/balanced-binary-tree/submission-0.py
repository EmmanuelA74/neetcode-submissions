# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #return height of l/r subtrees then check if abs(difference) > 1
        #approach one, two DFS functions
        def height(node):
            if not node:
                return 0
            
            left = height(node.left)
            right = height(node.right)

            return 1 + max(left, right)
        
        
        if not root:
            return True
        
        left = height(root.left)
        right = height(root.right)

        if abs(left - right) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)