'''
424. Longest Repeating Character Replacement
'''

class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    '''
    Solution:
    - find most freq letter (most likely to yield longest repeat) 
    - sliding window maintaining less than k non freq chars 

    Time: O(N) -> creating freq hashmap and iterating entire string 
    Space: O(N) -> freq hashmap 
    '''
    count = {}
    res = 0
    
    l = 0
    maxf = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])

        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)

    return res