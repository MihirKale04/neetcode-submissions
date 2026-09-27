class Solution:
    def isPalindrome(self, s: str) -> bool:
        pointer1 = 0 
        pointer2 = len(s) - 1

        s = s.lower()
        print(s)
        
        while pointer2 > pointer1:

            if not s[pointer2].isalnum():
                pointer2 -= 1
                continue
            if not s[pointer1].isalnum():
                pointer1 += 1
                continue            
            print (s[pointer1], s[pointer2])
            if s[pointer2] != s[pointer1]:
                return False

            pointer2 -= 1
            pointer1 += 1

            



        return True

        