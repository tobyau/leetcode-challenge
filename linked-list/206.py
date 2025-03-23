# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        solution: iterative 
        Time: O(N)
        Space: O(1) 

        1 -> 2 -> 3
        None <- 1 
        '''
        prev = None 
        curr = head 

        while curr:
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp 
        
        return prev