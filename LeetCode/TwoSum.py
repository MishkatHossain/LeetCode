class Solution:
    def twoSum(self, nums: list[int], t: int)->list[int]:
        prevMap = {} 

        for i, n in enumerate(nums):
            diff = t - n;
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
