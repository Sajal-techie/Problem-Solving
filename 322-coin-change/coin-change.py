class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount + 1)
        dp[0] = 0
        print(dp)
        for i in range(1, amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i-c]+1, dp[i])
        print(dp)
        return dp[amount] if dp[amount] <= amount else -1