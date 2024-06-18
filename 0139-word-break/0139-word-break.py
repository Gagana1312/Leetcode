class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # visited = set()

        # for word in wordDict:
        #     if word in s and word not in visited:
        #         visited.add(word)
        #         return True
        #     if word in s and word in visited:
        #         return False

        dp=[False]*(len(s)+1)
        dp[len(s)]=True

        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                if(i+len(word)) <= len(s) and s[i:i+len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
        return dp[0]
        
                

                
        