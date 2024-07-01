class Solution:
    def twoSum(nums, target):
        numToIndex = {}

        for i, num in enumerate(nums):
            if target - num in numToIndex:
                return numToIndex[target - num], i
            numToIndex[num] = i


    # main function

    List = [2, 7, 11, 15]
    print(twoSum(List, 9))