class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        res = []    
        def addToString(string, o, c):
            if o == c == n:
                print (o, c, n)
                res.append(string)
                return 
            if o < n:
                addToString(string+"(", o + 1, c)
            if c < o:
                addToString(string+")", o, c + 1)     

        addToString("",0,0)
        return res

    
        
        