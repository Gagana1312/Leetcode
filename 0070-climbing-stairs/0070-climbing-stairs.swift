class Solution {
    func climbStairs(_ n: Int) -> Int {
        if n == 1 {
        return 1
    }
    
    var first = 1
    var second = 2
    
    if n == 2 {
        return second
    }
    
    for _ in 3...n {
        let third = first + second
        first = second
        second = third
    }
    
    return second
        
    }
}