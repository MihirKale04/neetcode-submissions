class Solution:
    def longestPalindrome(self, s: str) -> str:
        # we need to scan through the string 
        n = len(s)
        resLen = 0
        res = ""    
        for i in range(n):
            string = self.getLengthOdd(i, s)
            string2 = self.getLengthEven(i, s)
            strLen = len(string)
            strLen2 = len(string2)
            print(strLen, strLen2)
            if strLen < strLen2:
                string = string2
                strLen = strLen2
            if  strLen > resLen:
                resLen = strLen
                res = string
        return res

    def getLengthOdd(self, index, string):
        # for now we are going to assume that Palindromes are odd
        length = 1 
        build = string[index]
        for i in range(1,len(string)):
            if index + i >= len(string) or index - i < 0:
                break
            if string[index + i] == string[index - i]:
                build = string[index - i] + build + string[index + i]
                length += 1
            else:
                break
        return build

    def getLengthEven(self, index, string):
        n = len(string)
        build = ""
        left, right = index, index + 1
        while True:
            if left < 0 or right >= n:
                break
            if string[left] == string[right]:
                build = string[left] + build + string[right]
            else:
                break
            left -= 1
            right += 1
        return build


