class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        res = []
        for x in asteroids:
            while res and x < 0 and res[-1] > 0:
                y = res[-1]  
                if abs(x) > abs(y):
                    res.pop() 
                elif abs(x) == abs(y):
                    res.pop()  
                    break
                else:
                    break
            else:
                res.append(x)
        return res



        