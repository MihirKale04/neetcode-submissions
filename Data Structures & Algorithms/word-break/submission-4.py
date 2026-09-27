
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool: 
        """We iterate over each word in the dictionary.
        If a word matches the beginning (prefix) of the target string,
        we remove that prefix and recursively try to segment the remaining
        substring the same way. If we can consume the entire string via
        these recursive matches, the segmentation succeeds."""


        """ Memoization 
        We can use a dp table to check if a substring leads to a solution
        before we call our recursive function to save compute time
        """
        
        
        dp = collections.defaultdict(bool)
        dp[""] = True
        
        for i in range(len(s) - 1, -1, -1):
            subStr = s[i:]
            dp[subStr] = False
            for w in wordDict:
                if w == subStr[0:len(w)]:
                    if dp[subStr[len(w):]]:
                        dp[subStr] = True        
        return dp[s]
