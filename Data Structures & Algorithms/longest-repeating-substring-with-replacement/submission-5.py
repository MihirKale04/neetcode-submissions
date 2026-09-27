class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        fmap = {}
        right = 0
        left = 0
        ans = 0
        
        
        fmap[s[left]] = fmap.get(s[left], 0 ) + 1
        while left < len(s):
            #add character to f map
            max_letter = max(fmap.values())         
            if ((left-right)+1) - max_letter <= k:
                ans = max(ans, (left-right)+1)
                left += 1
                if left < len(s):
                    fmap[s[left]] = fmap.get(s[left], 0 ) + 1
            else:
                fmap[s[right]] -= 1
                right +=1

        return ans

                



