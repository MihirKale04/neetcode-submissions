class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        def dfs(res, idx, string, digits, digitMap):
            if idx >= len(digits):
                res.append(string)
                return
            for ch in digitMap[digits[idx]]:
                string += ch
                dfs(res, idx + 1, string, digits, digitMap)
                string = string[:-1]

        def createDigitMap():
            return {"2" : "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}


        if not digits:
            return []

        digitMap = createDigitMap()
        combinations = []
        dfs(combinations, 0, "", digits, digitMap)
        return combinations

        