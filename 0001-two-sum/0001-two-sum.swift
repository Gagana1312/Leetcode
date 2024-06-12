class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var prevMap = [Int: Int]()
        for (i, n) in nums.enumerated() {
            let dif = target - n
            if let index = prevMap[dif] {
                return [index, i]
            }
            prevMap[n] = i
        }
        return []
    }
}
//  prevMap = {} #map that contains both key:value

//         for i,n in enumerate(nums):
//             difference = target - n
//             if difference in prevMap:
//                 return [prevMap[difference],i]
//             prevMap[n]=i
//         return