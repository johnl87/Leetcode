# lc 69
class Solution:
    def mySqrt(x: int) -> int:
        high, low = x, 0
        while low <= high:
            mid = (low + high) //2
            if mid*mid > x:
                high = mid - 1
            elif mid*mid < x:
                low = mid + 1
            else:
                return mid
        return high
    
    print(mySqrt(16))