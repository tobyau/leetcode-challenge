class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        solution: 2 pointer from left to right isalnum(), if isalnum() move to the next char 
        time: O(N)
        space: O(1) 
        '''
        if s.strip() == "":
            return True 
        
        left, right = 0, len(s) - 1

        while left < right: 
            while left < right and not s[left].isalnum():
                left += 1 
            while left < right and not s[right].isalnum():
                right -= 1 
            
            if s[left].lower() != s[right].lower():
                return False 
            left += 1 
            right -= 1 
        
        return True 