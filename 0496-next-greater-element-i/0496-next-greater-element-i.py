class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
       
        # x=[]
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i]==nums2[j]:
        #             if j<len(nums2)-1 and nums2[j+1]>nums1[i]:
        #                 x.append(nums2[j+1])
        #             else:
        #                 x.append(-1)
        # return x

        nums1Idx = { n:i for i,n in enumerate(nums1)}
        res = [-1]*len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in nums1Idx:
                continue
            for j in range(i+1, len(nums2)):
                if nums2[j]>nums2[i]:
                    idx = nums1Idx[nums2[i]]
                    res[idx]= nums2[j]
                    break
        return res
                    

