class Solution {
    func minCostClimbingStairs(_ cost: [Int]) -> Int {
        var dp = cost // Use the cost array as the DP table
        
        // Start the loop from the third step, since we can step from 0 or 1
        for i in 2..<cost.count {
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        }
        
        // The answer will be the minimum cost to reach either the last step or the step before it
        return min(dp[cost.count - 1], dp[cost.count - 2])
        
    }
}