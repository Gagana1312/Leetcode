class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        ## top down
        # memo={(0,0):1}

        # def paths(i,j):

        #     if (i,j) in memo:
        #         return  memo[(i,j)]
        #     elif i<0 or j<0 or i==m or j==n:
        #         return 0
        #     else:
        #         val= paths(i,j-1)+paths(i-1,j)
        #         memo[(i,j)]= val
        #         return val
        
        # return paths(m-1,n-1)


        # dp=[]
        # for _ in range(m):
        #     dp.append([0]*n)
        
        # dp[0][0] =1
        # for i in range(m):
        #     for j in range(n):
        #         if i==j==0:
        #             continue
        #         val=0
        #         if i>0:
        #             val+=dp[i-1][j]
        #         if j>0:
        #             val += dp[i][j-1]
                
        #         dp[i][j]= val
        # return dp[m-1][n-1]

        memo={(0,0):1}



        def path(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            elif i<0 or j<0 or i==m or j==n:
                return 0
            else:
                val = path(i,j-1)+path(i-1,j)
                memo[(i,j)]=val
                return val
        
        return path(m-1,n-1)


        


        
        