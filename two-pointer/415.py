class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        '''
        Solution: 2 pointer, ASCII, store result in list, add from left to right 

        4 5 6 
          7 7
        -----
        [5, 3, 3]
        '''
        p1, p2 = len(num1) - 1, len(num2) - 1
        carry = 0 
        res = deque() 

        while p1 >= 0 or p2 >= 0:
            # convert char to number using ascii 
            n1 = ord(num1[p1]) - ord("0") if p1 >= 0 else 0 
            n2 = ord(num2[p2]) - ord("0") if p2 >= 0 else 0 

            value = (n1 + n2 + carry) % 10
            carry  = (n1 + n2 + carry) // 10

            res.appendleft(str(value))

            p1 -= 1 
            p2 -= 1 
        
        if carry:
            res.appendleft(str(carry))
        
        return ''.join(res) 