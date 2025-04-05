class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        if s[i-1] < s[i]: s[i] - s[i-1] 
        right to left 
        '''
        numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000 
        }
        res = 0 
        i = len(s) - 1 

        while i >= 0:
            if i > 0 and numerals[s[i-1]] < numerals[s[i]]:
                res += numerals[s[i]] - numerals[s[i-1]] 
                i -= 2 
            else:
                res += numerals[s[i]] 
                i -= 1 

        return res 