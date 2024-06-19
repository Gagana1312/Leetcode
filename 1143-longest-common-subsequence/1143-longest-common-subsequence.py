class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # res = 0

        # for ch in text2:
        #     if ch in text1:
        #         res+=1
        # return res

        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i]==text2[j]:
                    dp[i][j] = 1+ dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return dp[0][0]
        