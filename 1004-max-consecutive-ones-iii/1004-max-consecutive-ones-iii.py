class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        window =0
        numzeros = 0
        n = len(nums)
        l=0
        for r in range(n):
            if nums[r]==0:
                numzeros +=1
            while numzeros>k:
                if nums[l]==0:
                    numzeros-=1
                l+=1
            w = r-l+1
            window = max(window,w)
        return window


        