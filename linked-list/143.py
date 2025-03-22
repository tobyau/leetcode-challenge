class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        time: 
        space: 
        solution: fast slow pointer and merge sorted lists 
        """
        if not head: 
            return 

        # find mid point, slow = mid 
        slow = fast = head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        
        # reverse second part of the list in place 
        prev, curr = None, slow 
        while curr:
            curr.next, prev, curr = prev, curr, curr.next 
        
        # merge 2 sorted lists 
        first, second = head, prev 
        while second.next: 
            first.next, first = second, first.next 
            second.next, second = first, second.next 