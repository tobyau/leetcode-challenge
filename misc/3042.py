class Solution:
    def isPrefixAndSuffix(self, str1, str2):
        return str2.startswith(str1) and str2.endswith(str1)

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0 
        n = len(words) 

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                str1, str2 = words[i], words[j] 
                if len(str1) > len(str2):
                    continue 
                if self.isPrefixAndSuffix(str1, str2):
                    print("hello")
                    res += 1 
        
        return res 