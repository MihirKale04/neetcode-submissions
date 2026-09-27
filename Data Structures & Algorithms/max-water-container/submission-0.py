class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #We want to maximize the area between 2 walls
            #One limiting factor we can point out 
            #is the smaller "wall" defines the height
            #of the rectangle
        
        #Brute-force method would be to itterate through
        #each of the walls calc the area and return the max
        
        #--BRUTEFORCE--
        # res = 0
        # for i in range(len(heights)):
        #     for j in range(i + 1,len(heights)):
        #         dist = j - i
        #         height = min(heights[i], heights[j])
        #         res = max(dist * height, res)
        # return res
        #--BRUTEFORCE--
        

        
       
       #We use a two pointer approach
       #We would init the start pointer to be at the
            #beggining of the array and the end pointer
            # to be at the end of the array to start off at the max distance
        #We then could calc the area based on the height of the smaller "wall" 
        #If the start wall is smaller then the height of the end wall we would move 
            #that one step right because that would be the limiting factor
        #If the end wall is smaller then the height of the start wall 
            #we would move that one step left because that would be the limiting factor
        #We would continue to calc and move "walls" until the start wall and end wall intersect ( go passed each other )
       
       
        #--TWO-POINTER--
        start = 0
        end = len(heights) - 1
        res = 0
        while start < end:
            #Area calculation
            height = min(heights[start], heights[end])
            dist = end - start
            area = height * dist
            res = max(area, res)
            
            #Todo: Pointer update
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1

        return res




    
        