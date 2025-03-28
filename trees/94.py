# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        time: O(N)
        space: O(N)
        solution: recursion -> left, root, right 
        '''
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []