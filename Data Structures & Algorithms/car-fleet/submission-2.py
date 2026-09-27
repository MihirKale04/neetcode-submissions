class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #phase one: Init cars and stack  -- O(nlogn)
        highway = []
        for i in range(len(position)):
            highway.append([position[i], speed[i]])
        highway.sort()
        print(highway)
        #phase two: traverse highway right to left
        stack = []
        for i in range(len(highway) - 1, -1, -1):
            #add car to stack
                #when we add to stack we express car as travel time
            car = (target - highway[i][0]) / highway[i][1]
            stack.append(car)
            #if travel time is less than the next car then remove car from stack
            if len(stack) > 1:
                if stack[-2] >= stack[-1]:
                    stack.pop()
            print(stack) 
        #return len of stack
        return len(stack)