class Solution:
  def maximumBeauty(self, nums: List[int], k: int) -> int:
    '''
    Problem: find largest group of overlapping ranges 
    Observation: nums[i] => nums[i] - k, nums[i] + k]
    Solution: 
    - sort array bcos close numbers have higher chance of overlapping ranges 
    - each number has a range of 2 * k 

    Time: O(NlogN) -> sorting + iterating array  
    Space: O(1) 
    '''
    nums.sort() 
    left = 0 
    ans = 0 

    for right in range(len(nums)):
      while nums[right] - nums[left] > 2 * k:
        left += 1 
      
      ans = max(ans, right - left + 1) 
    
    return ans 