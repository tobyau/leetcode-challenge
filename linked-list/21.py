# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        assign dummy head next to lowest val beween list1 / list2 

        edge case: lists will have extra at the tail 
        - assign dummy next to the list 
        - will be None if lists are at the end, nbd 

        Time: O(N) -> shorter list 
        Space: O(list1 + list2) -> merging 2 lists 
        '''
        head = ListNode(0) 
        temp = head 

        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1 
                list1 = list1.next 
            else:
                temp.next = list2 
                list2 = list2.next 
            temp = temp.next 
        
        temp.next = list1 if list1 else list2 
        
        return head.next 