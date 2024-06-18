class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #DP bottom up DP[0]=0 DP[1]=1 others are greater than 1, DP[2]=1+1 rest are >2
      # DP[3]=1 DP[4]=1 DP[5]=1 DP[6]=2 so DP[7]=1+DP[6]=1+2=3 
        dp = [amount+1]*(amount+1) 
        dp[0]=0

        for a in range(1, amount+1):
            for c in coins:
                if a-c>=0:
                    dp[a]=min(dp[a],1+dp[a-c])
        return dp[amount] if dp[amount]!= amount+1 else -1

        