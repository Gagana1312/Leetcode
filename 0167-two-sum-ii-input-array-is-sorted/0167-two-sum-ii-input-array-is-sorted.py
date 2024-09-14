class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # USE POINTERS
        l,r= 0, len(numbers)-1
        res=[]

        while l<r:
            summ = numbers[l]+numbers[r]
            if summ == target:
                return [l+1,r+1]
            elif summ<target:
                l+=1
            else:
                r-=1
        
        



        # res =[]
        # HashSet hs = set<int>
        # for n in numbers:
        #     diff = target- n
        #     if diff in numbers:
        #         res = [numbers.index(diff)+1,numbers.index(n)+1]
        #     if diff in numbers and diff == n:
        #         res = [numbers.index(n),numbers.index(n)]
        # return res


        