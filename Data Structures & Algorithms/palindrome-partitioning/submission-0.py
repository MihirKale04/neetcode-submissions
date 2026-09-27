class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            start, end  = 0, len(s) - 1
            while start < end:
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                else:
                    return False
            return True
        res = []
        def backtrack(s, partition):
            nonlocal res
            if not s:
                res.append(partition)
            subStr = ""
            for i in range(len(s)):
                subStr += s[i]
                if isPalindrome(subStr):
                    partition.append(subStr)
                    backtrack(s[len(subStr):], partition.copy())
                    partition.pop()
        backtrack(s, [])
        return res