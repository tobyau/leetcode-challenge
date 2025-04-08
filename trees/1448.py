# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0 

        def dfs(node, max_so_far):
            nonlocal good
            if not node:
                return 
            
            if node.val >= max_so_far:
                good += 1 
            
            if node.left:
                dfs(node.left, max(node.val, max_so_far))
            
            if node.right:
                dfs(node.right, max(node.val, max_so_far)) 
        
        dfs(root, -inf)
        return good 