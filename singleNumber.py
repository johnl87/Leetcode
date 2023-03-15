# lc 136
class Solution:
    def singleNumber(nums: list[int]) -> int:
        for i in nums:
           if nums.count(i) == 1:
               return i
    def singleNumber1(nums: list[int]) -> int:
        answer = 0
        for i in nums:
            answer ^= i
        return answer


    
    nums = [4,1,2,1,2]
    print(singleNumber(nums))
    print(singleNumber1(nums))