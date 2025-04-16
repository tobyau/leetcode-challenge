class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        return max values in window as it slides to the end 
        '''
        q = deque() 
        res = [] 

        for i, num in enumerate(nums):
            # maintain q in descending order by removing smaller elements on the right 
            while q and q[-1] < num:
                q.pop() 
            q.append(num) 

            if i >= k and nums[i - k] == q[0]:
                q.popleft() 
            
            if i >= k - 1:
                res.append(q[0])
        
        return res 

