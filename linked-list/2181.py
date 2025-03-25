# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Time: O(N)
        Space: O(1) 
        '''        
        dummy = ListNode(0) 
        temp = dummy # pointer for new list   
        curr = head.next 

        curr_sum = 0 
        while curr:
            if curr.val == 0:
                temp.next = ListNode(curr_sum) 
                temp = temp.next 
                curr_sum = 0 
            else:
                curr_sum += curr.val 
            curr = curr.next 

        return dummy.next 