class Solution:
    count = 0 
    def numDecodings(self, s: str) -> int:
        """we know that there are 26 ways to decode a digit.
            (1 - 26)"""

        """ we can kinda split it up into a tree """ 


        """ ok we can use a tree and somehow resuse portions
        that we have seen before """

        """lets for now focus on the unoptimized version of the tree"""


        
        index = 0 #if this index reaches the end of the string we have found a way to decode the message
        def dfs(i):
            if i >= len(s):
                self.count += 1
                return
            
            #left is going to be one digit
            leftNum = int(s[i])
            if leftNum <= 9 and leftNum >= 1:
                dfs(i+1)
            else:
                return

            
            if i + 1 >= len(s): #overflow check
                return
            
            #right is going to be two digit
            rightNum = int(s[i:i+2])
            if rightNum <=26 and rightNum >= 10:
                dfs(i+ 2)
            else:
                return
        dfs(index)
        return self.count
            