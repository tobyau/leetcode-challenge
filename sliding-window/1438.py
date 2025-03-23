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