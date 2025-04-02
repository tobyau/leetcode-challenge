class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        '''
        Solution
        - every divisor comes in pairs, the number below square root of num will give the largest factor, so we just have to iterate numbers between 1 and sqrt(num) 
        
        Time: O(N * sqrt(M)) -> iterate nums and sqrt(m) 
        Space: O(1)
        '''
        ans = 0 

        for num in nums:
            # use set to avoid duplicates 
            divisor = set() 
            for i in range(1, floor(sqrt(num)) + 1):
                if num % i == 0:
                    # add divisor pairs to set 
                    divisor.add(num//i)
                    divisor.add(i) 
                if len(divisor) > 4:
                    break 
            
            if len(divisor) == 4:
                ans += sum(divisor) 
        
        return ans 