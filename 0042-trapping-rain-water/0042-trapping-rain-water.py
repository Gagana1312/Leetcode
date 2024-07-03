class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if not height: return 0

        left, right =0, len(height)-1
        lmax, rmax = height[left], height[right]

        res =0

        while left < right:
            if lmax < rmax:
                left+=1
                lmax = max(lmax, height[left])
                res += lmax - height[left]
            else:
                right-=1
                rmax= max(rmax, height[right])
                res += rmax - height[right]
        return res


        