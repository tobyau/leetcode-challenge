class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        turn into string and use 2 pointer 
        Time: O(N)
        Space: O(1) 
        '''
        x = str(x) 
        left, right = 0, len(x) - 1 

        while left < right:
            if x[left] != x[right]:
                return False 
            left += 1 
            right -= 1 
        
        return True  