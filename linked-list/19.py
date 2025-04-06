class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        time: O(N)
        space: O(1) 
        solution: fast+slow pointer 

        n = 2 
        1 -> 2 -> 3 -> 4 -> None 
             ^              ^ 
             s              f 
            
        1 -> 2 -> 4 
        '''
        dummy = ListNode(0)
        dummy.next = head 
        first = dummy
        second = dummy 

        # increment first by n 
        for i in range(n+1):
            first = first.next 
        
        # iterate through list until the end 
        while first is not None:
            first = first.next 
            second = second.next 
        
        second.next = second.next.next 
        
        return dummy.next 