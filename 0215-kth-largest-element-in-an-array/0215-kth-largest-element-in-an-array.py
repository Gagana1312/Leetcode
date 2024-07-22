class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        return nums[len(nums)-k]

        # Quick Select Algorithm (More efficient)

        # k = len(nums)-k
        # def quickSelect( l , r ):
        #     pivot,pointer = nums[r],l
        #     for i in range(l,r):
        #         if nums[i] <= pivot:
        #             nums[pointer],nums[i] = nums[i],nums[pointer]
        #             pointer += 1
        #     nums[pointer],nums[r] = nums[r], nums[pointer]

        #     if pointer > k: return quickSelect(l,pointer - 1)
        #     elif pointer < k: return quickSelect(pointer + 1, r)
        #     else: return nums[pointer]
        
        # return quickSelect(0,len(nums)-1)
# class Solution:
#     def partition(self, nums: List[int], left: int, right: int) -> int:
#         pivot, fill = nums[right], left

#         for i in range(left, right):
#             if nums[i] <= pivot:
#                 nums[fill], nums[i] = nums[i], nums[fill]
#                 fill += 1

#         nums[fill], nums[right] = nums[right], nums[fill]

#         return fill

#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         k = len(nums) - k
#         left, right = 0, len(nums) - 1

#         while left < right:
#             pivot = self.partition(nums, left, right)

#             if pivot < k:
#                 left = pivot + 1
#             elif pivot > k:
#                 right = pivot - 1
#             else:
#                 break

#         return nums[k]





        
        