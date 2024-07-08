class Solution {
    func topKFrequent(_ nums: [Int], _ k: Int) -> [Int] {
        var count = [Int: Int]() // Dictionary to store counts
        var freq = Array(repeating: [Int](), count: nums.count + 1) // Array of empty arrays
        
        // Count the occurrences of each number in nums
        for n in nums {
            count[n, default: 0] += 1
        }
        
        // Populate the freq array with numbers grouped by their frequency
        for (n, c) in count {
            if c < freq.count {
                freq[c].append(n)
            }
        }
        
        // Construct the result array res by collecting numbers in descending order of frequency
        var res = [Int]()
        for i in stride(from: freq.count - 1, through: 1, by: -1) {
            for n in freq[i] {
                res.append(n)
                if res.count == k {
                    return res
                }
            }
        }
        
        return res
       



        
    }
}


    //    count = {}
    //     freq = [[] for i in range(len(nums) + 1)]

    //     for n in nums:
    //         count[n] = 1 + count.get(n, 0)
    //     for n, c in count.items():
    //         freq[c].append(n)

    //     res = []
    //     for i in range(len(freq) - 1, 0, -1):
    //         for n in freq[i]:
    //             res.append(n)
    //             if len(res) == k:
    //                 return res
