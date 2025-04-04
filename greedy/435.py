class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        greedy
        - sort intervals by end range: x[1] 
        - if end of an interval is < end range, can remove 
        
        Time: O(N log N) -> sort intervals and iterate intervals 
        Space: O(N) -> python sort is O(N) while other languages are log n...
        '''
        intervals.sort(key=lambda x: x[1])
        res = 0 
        end_range = -inf 

        for start, end in intervals:
            if start >= end_range:
                end_range = end 
            else:
                res += 1 
        
        return res 