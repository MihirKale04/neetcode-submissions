class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        area = 0
        l, r = 0, len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]
        while l < r:
            if maxLeft < maxRight:
                l += 1
                temp = maxLeft - height[l]
                if temp > 0:
                    area += temp
                maxLeft = max(maxLeft, height[l])
            else:
                r -= 1
                temp = maxRight - height[r]
                if temp > 0:
                    area += temp
                maxRight = max(maxRight, height[r])
        return area
