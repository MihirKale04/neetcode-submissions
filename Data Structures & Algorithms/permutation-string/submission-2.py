class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1map = {}
        for char in s1:
            s1map[char] = s1map.get(char, 0) + 1
        # print (s1map)
        def IsPermutation(checkMap):
            for char in checkMap:
                if char not in s1map:
                    return False
                if checkMap[char] != s1map[char]:
                    return False
            return True
        
        #initialize a sliding window of length s1
        start = 0
        end = 0
        charMap = {}
        while end < len(s1):
            charMap[s2[end]] = charMap.get(s2[end], 0) + 1
            end += 1
        end -= 1 #this is to account for the last iteration of the sliding window init
        # print(charMap)

        #slide the window along the length of s2
        while end < len(s2) - 1:
            #on each slide we check if that window is a valid permuation of s1
            if IsPermutation(charMap):
                return True
            charMap[s2[start]] -= 1
            if charMap[s2[start]] == 0:
                charMap.pop(s2[start],None)
            start +=1
            end += 1
            charMap[s2[end]] = charMap.get(s2[end], 0) + 1
            # print(charMap)
        #one more check to account for last window
        if IsPermutation(charMap):
                return True
        return False