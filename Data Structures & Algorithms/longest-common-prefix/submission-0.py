class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        charMap = set()
        firstWord = strs[0]
        
        
        s = ""
        for ch in firstWord:
            charMap.add(s)
            s += ch
        charMap.add(s)
        print(charMap)
        
    
        res = firstWord
        for i in range(1, len(strs)):
            s = ""
            for ch in strs[i]:
                if s + ch  not in charMap:
                    break
                s += ch 
                
            res = min(res, s)
            print(res)
        
        return res
        