class Solution:
    def countBits(self, n: int) -> List[int]:   
        # res = []
        # for i in range(n + 1):
        #     oneCount = bin(i).count('1')
        #     res.append(oneCount)
        # return res


        #dp solution
        #init dpTable
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
