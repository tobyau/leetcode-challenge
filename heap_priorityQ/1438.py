class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        '''
        using 2 heaps to maintain max and min values 
        - as long as number is between valid max and min values, it is part of a good subarray 
        - once we reach an invalid subarray, move left pointer to the right and remove items from heap until window is valid 
        '''
        min_heap = [] 
        max_heap = [] 
        longest = 0 
        left = 0 

        for right in range(len(nums)):
            heapq.heappush(min_heap, (nums[right], right))
            heapq.heappush(max_heap, (-nums[right], right)) 

            # invalid window 
            while -max_heap[0][0] - min_heap[0][0] > limit:
                # increment left pointer 
                left = min(max_heap[0][1], min_heap[0][1]) + 1 
                # remove items from heap while window is invalid 
                while max_heap[0][1] < left:
                    heapq.heappop(max_heap) 
                while min_heap[0][1] < left:
                    heapq.heappop(min_heap) 
            
            # valid window, set longest subarray 
            longest = max(longest, right - left + 1) 
        
        return longest 