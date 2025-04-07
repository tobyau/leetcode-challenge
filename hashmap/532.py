class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        '''
        hashmap to store num freq, then iterate numbers in hashmap 

        Time: O(N) -> create frequency hashmap + iterate keys in the hashmap
        Space: O(M) -> store unique nums, no duplicates 
        '''
        res = 0 
        counter = Counter(nums)

        for key in counter:
            if k > 0 and key + k in counter:
                res += 1 
            elif k == 0 and counter[key] > 1:
                res += 1 
        
        return res 