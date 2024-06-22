class Solution:
    def hammingWeight(self, n: int) -> int:

#         res =0
#         while n:
#             res += n%2
#             n = n>>1
#         return res
        rse = 0
        while n:
            n = n&(n-1)
            rse+=1
        return rse
        