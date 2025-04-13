class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        Time: O(N * 2^N) -> iterate nums list, generate subsets 
        Space: O(N * 2^N) -> N elements and number of subsets 

        iterate nums and append curr number to previous subsets 
        '''
        res = [[]]

        for num in nums:
            newSubsets = [] 
            for curr in res:
                temp = curr.copy() 
                temp.append(num) 
                newSubsets.append(temp)
            for curr in newSubsets:
                res.append(curr)
        
        return res 