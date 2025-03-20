class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
      '''
      solution: 
      - sliding window (size 3) 
      - edge case: circular array

      Time: O(N)
      Space: O(1)
      '''
      ans = 0 
      n = len(colors)

      for i in range(n):
        prev = colors[i - 1]  
        curr = colors[i]
        next_ = colors[(i + 1) % n] 

        if curr != prev and curr != next_:
          ans += 1
      
      return ans 