class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        time: O(coins * amount)
        space: O(amount + 1) 

        Using DP to keep track of how many coins needed to reach amount 
        - each index represents target amount 
        - dp[i - coin] represents the other coin amount that is used to reach target amount 
        '''
        # use amount + 1 to represent an arbritrary max value for each amount
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0 

        for c in coins:
            # for each coin, calculate how many coins needed to reach amount (index) 
            for i in range(c, amount + 1):
                # i - c because we know there is a combination that adds up to amount that is less than the current i amount 
                # using what we calculated in previous amounts 
                dp[i] = min(dp[i], dp[i - c] + 1) 
        
        return dp[amount] if dp[amount] != amount + 1 else -1 