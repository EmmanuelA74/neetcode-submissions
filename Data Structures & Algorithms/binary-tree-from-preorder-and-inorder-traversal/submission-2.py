# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #O(n) sol
        indices = {val: index for index, val in enumerate(inorder)}
        self.preorder_index = 0

        #l,r for the inorder range
        def dfs(l, r):
            if l > r:
                return None
            
            root_val = preorder[self.preorder_index]
            root = TreeNode(root_val)
            self.preorder_index += 1
            mid = indices[root_val]

            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root


        return dfs(0, len(inorder) - 1)
