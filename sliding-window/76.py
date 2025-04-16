class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Time: O(s + t)
        Space: O(s + t)  
        '''
        if not t or not s:
            return "" 
        
        count_t = Counter(t) 
        required = len(count_t) 

        l, r = 0, 0 

        formed = 0 

        window_counts = {} 

        res = inf, None, None 

        while r < len(s):
            char = s[r] 
            window_counts[char] = window_counts.get(char, 0) + 1 

            if char in count_t and window_counts[char] == count_t[char]:
                formed += 1 
            
            while l <= r and formed == required:
                char = s[l] 
                if r - l + 1 < res[0]:
                    res = (r - l + 1, l, r) 
                
                window_counts[char] -= 1 
                if char in count_t and window_counts[char] < count_t[char]:
                    formed -= 1 
                
                l += 1 

            r += 1 
        
        return "" if res[0] == inf else s[res[1] : res[2] + 1]