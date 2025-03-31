class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        time: O(word1 + word2) 
        space: O(1) 
        solution: 2 pointer 
        '''
        p1 = p2 = 0 
        merged_string = "" 

        while p1 < len(word1) and p2 < len(word2):
            merged_string += word1[p1]
            p1 += 1 
            merged_string += word2[p2]
            p2 += 1 

        if p1 == len(word1) and p2 < len(word2):
            merged_string += word2[p2:]
        else:
            merged_string += word1[p1:]
        
        return merged_string