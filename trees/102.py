# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        BFS 
        '''
        if not root:
            return [] 
            
        q = deque([root])
        res = [] 

        while q:
            # get level by len(q) 
            level = [] 

            for i in range(len(q)):
                node = q.popleft() 
                level.append(node.val) 

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right) 
            res.append(level) 
        
        return res 
                
