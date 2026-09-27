class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
            We can use a stack 

            [8 -7]
            


            if we encounter a negative asteroid
            we will check if the top of the stack is positive and compare 
            its size

        """


        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
                continue
            if asteroid < 0:
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                    stack.pop()
                if stack and stack[-1] > 0 and stack[-1] == abs(asteroid):
                    stack.pop()
                    continue #don't add the asteroid
                if stack and stack[-1] > 0 and stack[-1] > abs(asteroid):
                    continue #don't add the asteroid
                stack.append(asteroid)

        return stack
            