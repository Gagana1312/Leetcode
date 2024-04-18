class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums
        nums_to_append = nums
        for i in range(len(nums)):
            ans.append(nums_to_append[i])
        return ans
        
    