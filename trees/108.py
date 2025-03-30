# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.helper(nums, 0, len(nums))
        
    def helper(self, nums, lower, upper):
        if lower >= upper:
            return 
        
        mid = (lower + upper) // 2 

        node = TreeNode(nums[mid])
        node.left = self.helper(nums, lower, mid)
        node.right = self.helper(nums, mid+1, upper)
        
        return node 