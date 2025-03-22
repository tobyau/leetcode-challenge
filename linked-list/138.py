class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        time: O(N) 
        space: O(N)
        solution: create hashmap to store new nodes, iterate list 2nd time to populate nodes.next and random in the hashmap 
        '''
        if not head:
            return None 

        old_to_new = {}

        # iterate list to populate old to new hashmap { currNode : val }
        curr = head 
        while curr:
            old_to_new[curr] = Node(curr.val) 
            curr = curr.next 
        
        curr = head 
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next) 
            old_to_new[curr].random = old_to_new.get(curr.random) 
            curr = curr.next 
        
        return old_to_new[head]