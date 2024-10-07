class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        # l=0
        # for r in range(1, len(arr)):
        #     summ = abs(arr[l])+abs(arr[r])
        #     if summ>=k:
        #         if (summ % k) ==0:
        #             return True
        #     l+=1
        # return False

        remainder_count = [0] * k
        for num in arr:
            remainder = num % k
            remainder_count[remainder] += 1
        for i in range(1, k):
            if remainder_count[i] != remainder_count[k - i]:
                return False
        return remainder_count[0] % 2 == 0
        

        