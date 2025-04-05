# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        2 pointers: add numbers as long as l1 or l2 or carry exists 

        Time: O(l1 + l2) 
        Space: O(N) 
        '''
        carry = 0
        res = ListNode(0) 
        curr = res 

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0 
            val2 = l2.val if l2 else 0 

            total = val1 + val2 + carry 
            digit = total % 10 
            carry = total // 10 

            curr.next = ListNode(digit) 
            curr = curr.next 

            if l1: l1 = l1.next 
            if l2: l2 = l2.next 
        
        return res.next 
        
