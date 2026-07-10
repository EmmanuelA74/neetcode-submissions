# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #O(n*m) sol
        def sameTree(node, subnode):
            if not node and not subnode:
                return True

            if not node or not subnode:
                return False
            
            if node.val != subnode.val:
                return False
            
            left = sameTree(node.left, subnode.left)
            right = sameTree(node.right, subnode.right)
            return left and right

        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False
        
        #check if they are the same tree
        if root.val == subRoot.val and sameTree(root, subRoot):
            return True 

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right