class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        df = [[0 for _ in range(len(text2) + 1) ] for _ in range(len(text1) + 1)]


        for ch1 in range(len(df) - 2, -1, -1):
            for ch2 in range(len(df[0]) - 2, -1, -1):
                if text1[ch1] == text2[ch2]:
                    df[ch1][ch2] = 1 + df[ch1 + 1][ch2 + 1]
                else:
                    df[ch1][ch2] = max(df[ch1 + 1][ch2], df[ch1][ch2 + 1])
    
        return df[0][0]
