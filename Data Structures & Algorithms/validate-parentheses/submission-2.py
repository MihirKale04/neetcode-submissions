class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in '[{(':
                stack.append(char)
            if char == ']' and (not stack or stack.pop() != '['):
                return False
            elif char == '}' and (not stack or stack.pop() != '{'):
                return False
            elif char == ')' and (not stack or stack.pop() != '('):
                return False
        if len(stack) == 0:
            return True
        return False