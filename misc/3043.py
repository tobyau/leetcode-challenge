class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        '''
        use hashset to store prefixes of each element 
        '''
        arr1_prefixes = set() 

        # build all prefixes from arr1 
        for v in arr1:
            while v not in arr1_prefixes and v > 0:
                arr1_prefixes.add(v) 
                v //= 10 
        
        longest_prefix = 0

        # check arr2 for matching prefixes 
        for v in arr2:
            while v not in arr1_prefixes and v > 0:
                v //= 10 
            
            if v > 0:
                longest_prefix = max(longest_prefix, len(str(v)))
        
        return longest_prefix