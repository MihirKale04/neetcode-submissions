class Solution:
    def countSubstrings(self, s: str) -> int:
        """We know that every individual char in the string is 
        going to be a palindrome."""

        """What if we go through each char and use the 
        two pointer approach to check if adding the neighbors
        make it a valid palindrome. We need to take account of 
        the odd and even palindrome case."""

        """We will update a count/result variable whenever we detect a vaild palindrome."""

        """This approach should be about O(n^2)."""

        result = 0
        n = len(s)
        for i in range(n):
            result += self.getOdd(i, s, n)
            result += self.getEven(i, s, n)  
        return result

    def getOdd(self, start, s, n):
        """This will return the number of odd palindromes 
        surrounding the char at index "start" """
        length = 1 #base case the char itself is a palindrome
        right, left = start - 1, start + 1
        while True:
            if right < 0 or left >= n:
                break
            if s[right] == s[left]: #We detected a new palindrome
                length += 1
                print("odd detected:", length)
            else:
                break
            right -= 1
            left += 1
        return length
    
    def getEven(self, start, s, n):
        """This will reutn the number of evern palindromes
        surrounding  and including the char at index "start" and "start + 1" """
        length = 0 
        right, left = start, start + 1
        while True:
            if right < 0 or left >= n:
                break
            if s[left] == s[right]:
                length += 1
                print("even detected:", s[left], s[right])
            else:
                break
            right -= 1
            left += 1 
        return length




