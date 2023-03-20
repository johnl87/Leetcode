def twoSum(nums, target):
    d = {}
    
    for i, j in enumerate(nums):
        result = target - j
        if result in d:
            return [d[result], i]
        d[j] = i


nums = [2,7,11,15]
target = 9        
for i, j in enumerate(nums):
    print("i= ", i )
    print("j= ", j )