class Solution:
  def countKConstraintSubstrings(self, s: str, k: int) -> int:
    '''
    Time: O(N^2)
    Space: O(1)  
    '''
    ans = 0 
    left = 0 
    count_ones = 0 
    count_zeros = 0 

    for right in range(len(s)):
      if s[right] == "1":
        count_ones += 1 
      else:
        count_zeros += 1 

      while count_ones > k and count_zeros > k:
        if s[left] == "1":
          count_ones -= 1 
        else:
          count_zeros -= 1 
        left += 1 

      ans += right - left + 1  
    
    return ans 