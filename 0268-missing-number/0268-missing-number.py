# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         res =0
#         nums.sort()
#         length = len(nums)-1
#         largest = nums[length]
        
#         for n in nums:
#             if largest - n in nums:
#                 continue
#             res = largest - n
#         return res

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)
#         total_sum = n * (n + 1) // 2
#         actual_sum = sum(nums)
#         return total_sum - actual_sum
            

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         length = len(nums)
        
#         for i in range(length):
#             if nums[i] != i:
#                 return i
        
#         return length

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
        return res

