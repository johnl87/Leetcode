# lc 217
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create an empty set
        numbers = set()
        # run through the given nums array, if the number is not already inside set
        # then add the number to the set, otherwise return True because the second
        # occurance will confirm that the nums array has more than one of the 
        # same numbers
        
        for number in nums:
            if number not in numbers:
                numbers.add(number)
            else:
                return True
