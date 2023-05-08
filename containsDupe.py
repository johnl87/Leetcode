# lc 217
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numbers = set()
        for number in nums:
            if number not in numbers:
                numbers.add(number)
            else:
                return True
