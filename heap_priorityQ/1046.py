class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        turn stones negative to caculate as max heap
        iterate as long as heap is non empty 
        
        Time: O(nlogn) 
        Space: O(n) 
        '''
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones) 
            if second > first:
                heapq.heappush(stones, first - second) 
        
        return -heapq.heappop(stones) if stones else 0 