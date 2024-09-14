class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # res=[0]*len(temperatures)
        # l,r= 0,1
        # while l<r and r<len(temperatures):
        #     if temperatures[l]<temperatures[r]:
        #         res[l]= r-l
        #         l+=1
        #         r=l+1
        #     else:
        #         r+=1
        # return res



        temp = temperatures
        n = len(temperatures)
        res=[0]*n
        stack =[]

        for i, t in enumerate(temp):
            while stack and stack[-1][0]<t:
                stack_t, stack_i = stack.pop()
                res[stack_i] = i - stack_i
            stack.append((t,i))
        return res
        