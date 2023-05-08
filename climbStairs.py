# lc 70
class Solution:
    def climbStairs(self, n: int) -> int:
        # base case
        if n <= 2:
            return n
        # setting dictionary where 0 - 2 has a defined value
        steps = {}
        steps[0] = 0
        steps[1] = 1
        steps[2] = 2
        # starting from 3 to n + 1
        for i in range(3, n+1):
            # if i or the index is already in dictionay return it
            if i in steps:
                return steps[i]
            else:
                # otherwise, the value at that index is the previous index plus the current one
                steps[i] = steps[i - 1] + steps[i - 2]
        return steps[n]