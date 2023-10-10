class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        
        l, r = 0, len(nums)-1


        while l<r:
            curSum = nums[l] + nums[r]

            if curSum > t:
                r=r-1;
            elif curSum < t:
                l=l+1;    
            else :
                return [l+1, r+1]
