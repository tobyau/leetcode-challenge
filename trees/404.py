# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, isLeft):
            if not node:
                return 0 
            
            if not node.left and not node.right:
                if isLeft:
                    return node.val 
                else:
                    return 0 
            
            left_sum = dfs(node.left, True) 
            right_sum = dfs(node.right, False) 
            return left_sum + right_sum 
        
        return dfs(root, False)