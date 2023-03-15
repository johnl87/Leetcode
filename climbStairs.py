# lc 70
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        steps = {}
        steps[0] = 0
        steps[1] = 1
        steps[2] = 2
        for i in range(3, n+1):
            if i in steps:
                return steps[i]
            else:
                steps[i] = steps[i - 1] + steps[i - 2]
        return steps[n]