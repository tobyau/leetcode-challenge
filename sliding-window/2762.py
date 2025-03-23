class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        '''
        condition: | nums[i] - nums[j] | <= 2 

        Time: O(N) 
        Space: O(1) -> freq map stores elements within the window 
        '''
        freq = {} 
        left = right = 0 
        count = 0 

        while right < len(nums):
            freq[nums[right]] = freq.get(nums[right], 0) + 1 

            # if window is not valid: 
            while max(freq) - min(freq) > 2:
                freq[nums[left]] -= 1 
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1 
            
            # each window contributes right - left + 1 subarrays 
            count += right - left + 1 
            right += 1 
        
        return count 