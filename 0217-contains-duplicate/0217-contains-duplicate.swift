class Solution {
    func containsDuplicate(_ nums: [Int]) -> Bool {
        if nums.count == Set(nums).count {
            return false
        } else {
            return true
        }
        
        
    }
}