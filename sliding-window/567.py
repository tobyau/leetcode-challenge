class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
    '''
    Solution: 
    - since the constraints are english letters, we can compare the total count of english letters in s1 and s2 
    - initialize freq count for s1 and s2 [0] * 26 
        - init first window count for s1 and s2 
    - sliding window over s2, keep count 
    - compare s1 == s2 

    Time: O(N)
    Space: O(1)  
    '''
    if len(s1) > len(s2):
        return False

    s1Count = [0] * 26
    s2Count = [0] * 26

    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1

    for i in range(len(s2) - len(s1)):
        if s1Count == s2Count:
            return True
        s2Count[ord(s2[i]) - ord('a')] -= 1
        s2Count[ord(s2[i + len(s1)]) - ord('a')] += 1

    return s1Count == s2Count