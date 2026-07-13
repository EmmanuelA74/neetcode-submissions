# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            
            good = 0
            if node.val >= max_val:
                max_val = node.val
                good += 1
            
            left = dfs(node.left, max_val)
            right = dfs(node.right, max_val)

            good += (left + right)

            return good
        
        return dfs(root, float("-inf"))