class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #We need to count if the number of the charcters are the same for both strings
        #We can create a hash map for both strings and compare

        if len(s) != len(t):
            return False
        
        
        smap = {}
        tmap = {}
        
        for char in s:
            smap[char] = smap.get(char, 0) + 1
        for char in t:
            tmap[char] = tmap.get(char, 0) + 1
        
        for char in s:
            if smap[char] != tmap.get(char, 0):
                return False
        

        return True