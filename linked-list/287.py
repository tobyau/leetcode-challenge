class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Don't modify array + using O(1) space 

        Time: O(N)
        Space: O(1) 

        Solution
        - cycle detection, slow fast pointers 
        - linked list cycle 
        ''' 
        slow, fast = 0, 0 

        while True: 
            fast = nums[fast] 
            slow = nums[nums[slow]] 
            if slow == fast:
                break

        slow2 = 0 
        while True: 
            slow = nums[slow] 
            slow2 = nums[slow2] 
            if slow == slow2:
                return slow 