class Solution:
    def isValid(self, s: str) -> bool:
        '''
        use stack to track open parentheses, pop when there's closed paren 
        Time: O(N) -> len(s) 
        Space: O(N) -> len(s) worst case
        '''
        stack = [] 

        parentheses = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for p in s:
            # closing paren 
            if p in parentheses:
                top = stack.pop() if stack else "#" 
                if parentheses[p] != top:
                    return False 
            else:
                stack.append(p) 
        
        return True if len(stack) == 0 else False 