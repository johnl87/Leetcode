# lc 11
def maxArea(height):
    result = 0
    # left pointer at most left and right pointer at most right
    left, right = 0, len(height)-1
    
    while left < right:
        area = (right - left) * min(height[left], height[right])
        result = max(area,result)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return area