class Solution {
    func rob(_ nums: [Int]) -> Int {
        // Edge case: if there are no houses, return 0
        if nums.isEmpty {
            return 0
        }
        
        // Edge case: if there's only one house, return the value of that house
        if nums.count == 1 {
            return nums[0]
        }
        
        // Initialize two variables to store the maximum profit up to the previous house and the one before it
        var prev1 = 0  // Max profit up to the previous house
        var prev2 = 0  // Max profit up to the house before the previous one
        
        // Loop through each house
        for num in nums {
            let current = max(prev1, prev2 + num)  // Decide whether to rob the current house or not
            prev2 = prev1  // Update prev2 to be the previous house
            prev1 = current  // Update prev1 to be the current max
        }
        
        // The result is stored in prev1
        return prev1
        
    }
}