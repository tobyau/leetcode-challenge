# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        create a helper func to reverse nodes in k-group 
        - return head (original head), head.next = next node 
        
        - move curr pointer k times to move to next group 
            - if curr pointer is None, break and return head 
        '''
        ptr = head 
        ktail = None 

        new_head = None 

        while ptr:
            count = 0 

            ptr = head 

            while count < k and ptr:
                ptr = ptr.next 
                count += 1 
            
            if count == k:
                reverseHead = self.reverseKList(head, k)

                # new_head is head of final linked list 
                if not new_head:
                    new_head = reverseHead 
                
                if ktail:
                    ktail.next = reverseHead 
                
                ktail = head 
                head = ptr 
        
        if ktail:
            ktail.next = head 
        
        return new_head if new_head else head 

    
    def reverseKList(self, head, k):
        new_head, ptr = None, head 

        while k: 
            next_node = ptr.next 
            ptr.next = new_head 
            new_head = ptr 

            ptr = next_node 
            k -= 1 

        return new_head 