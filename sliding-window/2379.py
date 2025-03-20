class Solution:
  def minimumRecolors(self, blocks: str, k: int) -> int:
    count_w = 0 
    left = right = 0 
    ans = float('inf')

    # iterate array to recolor 
    for right in range(len(blocks)):
      if blocks[right] == "W":
        count_w += 1 
      
      if (right - left + 1) == k:
        ans = min(ans, count_w) 
        if blocks[left] == "W":
          count_w -= 1 
        left += 1 
    
    return ans 