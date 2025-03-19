class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    '''
    Solution: 
    - use hashset to keep track of unique chars
    - sliding window: if found dup, slide window

    Time: O(N) -> iterate entire array
    Space: O(N) -> worst case: all chars are unique and stored in set
    '''
    ans = 0 
    unique = set() 
    left = 0 

    for right in range(len(s)):
      while s[right] in unique:
        unique.remove(s[left])
        left += 1 
      
      unique.add(s[right])
      ans = max(ans, right - left + 1) 
    
    return ans 