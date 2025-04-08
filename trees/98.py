# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        keep track of high low 
        DFS 
        '''
        def dfs(node, low, high):
            if not node:
                return True 

            # node value is between low and high 
            if node.val <= low or node.val >= high:
                return False 
            
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        
        return dfs(root, -inf, inf)