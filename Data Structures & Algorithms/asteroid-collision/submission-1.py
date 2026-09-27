class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:       # top asteroid destroyed
                    stack.pop()
                elif stack[-1] == -asteroid:    # mutual destruction
                    stack.pop()
                    break
                else:                           # incoming asteroid destroyed
                    break
            else:
                stack.append(asteroid)          # asteroid survived, add it

        return stack
            