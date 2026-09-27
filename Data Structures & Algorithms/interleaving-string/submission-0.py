class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1Len, s2Len  = len(s1), len(s2)
        if s1Len + s2Len != len(s3):
            return False
        
        #Init dp table
        dp = [[False for _ in range(s2Len + 1)] for _ in range(s1Len + 1)]
        dp[s1Len][s2Len] = True
        for i in range(s1Len, -1, -1):
            for j in range(s2Len, -1, -1):
                if i < s1Len and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < s2Len and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]