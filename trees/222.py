# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        ans = 0 

        def dfs(node):
            nonlocal ans 
            if not node:
                return None 
            
            left, right = dfs(node.left), dfs(node.right) 
            ans += 1 

            return left or right 
        
        dfs(root)
        return ans 