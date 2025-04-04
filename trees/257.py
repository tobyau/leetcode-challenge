# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        '''
        DFS
        Time: O(N)
        Space: O(N) 
        '''
        res = [] 

        def dfs(node, path):
            if not node:
                return 
            # leaf node -> append the path to result 
            if not node.left and not node.right:
                path += str(node.val)
                res.append(path)
                return 
            
            path += f"{node.val}->"

            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return res 