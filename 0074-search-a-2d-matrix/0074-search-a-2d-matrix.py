class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #linear search
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         if target in matrix[i]:
        #             return True
        # return False

        # Binary search
        if not matrix:
            return False
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows*cols-1

        while l<= r:
            mid = r+(l-r)//2
            midmat = matrix[mid //cols][mid%cols]

            if midmat < target:
                l = mid+1
            elif midmat > target:
                r= mid-1
            else:
                return True




        