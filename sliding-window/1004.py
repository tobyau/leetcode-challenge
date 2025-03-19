'''
1004. Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
'''

class Solution:
  def longestOnes(self, nums: List[int], k: int) -> int:
    '''
    sliding window 
    - keep track of zeros to maintain the window with k zeros 

    Time: O(N)
    Space: O(1) 
    '''
    ans = float('-inf')
    left = 0 
    zeros = 0 

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1 
        # increment left pointer to maintain window with k zeros 
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1 
            left += 1 
        
        ans = max(ans, right - left + 1)
    
    return ans 