class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # coins.sort()
        # count=0
        # for n in coins[::-1]:
        #     while amount >=n:
        #         amount -=  n
        #         count+=1
        # if amount ==0:
        #     return count
        # else:
        #     return -1

        coins.sort()
        memo = {0:0}

        def min_coins(amt):
            if amt in memo:
                return memo[amt]
            minn = float('inf')
            for coin in coins:
                diff= amt - coin
                if diff<0:
                    break
                minn = min(minn, 1+min_coins(diff))
            memo[amt] = minn
                
            return minn
        result =min_coins(amount)
        if result <float('inf'):
            return result
        else:
            return -1
        

        