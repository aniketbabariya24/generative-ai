# 1. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     - *Output*: "[0, 1]"


def sumAndTarget(nums, target):
    numberDict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in numberDict:
            return [numberDict[complement], i]
        numberDict[num] = i

    return []


nums = [2, 7, 11, 15]
target = 9

result = sumAndTarget(nums, target)
print(result)  
