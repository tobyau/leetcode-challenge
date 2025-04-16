'''
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.
'''

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        '''
        | max - min | <= limit 

        solution: 2 deques + sliding window 
        '''
        max_dq = deque() 
        min_dq = deque() 
        left = 0 
        ans = 0 

        for right in range(len(nums)):
            # maintain max queue in decreasing order - max front 
            while max_dq and max_dq[-1] < nums[right]:
                max_dq.pop() 
            max_dq.append(nums[right])

            # maintain the min_deque in increasing order - min front 
            while min_dq and min_dq[-1] > nums[right]:
                min_dq.pop()
            min_dq.append(nums[right])

            while max_dq[0] - min_dq[0] > limit:
                if max_dq[0] == nums[left]:
                    max_dq.popleft() 
                if min_dq[0] == nums[left]:
                    min_dq.popleft()
                left += 1 
            
            ans = max(ans, right - left + 1)
        
        return ans 