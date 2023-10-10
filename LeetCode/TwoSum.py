class Solution:
    def maxSubArray(self, nums: list[int])->int:
        x = -99;

        for i in range(len(nums)):
            for j in range(i, len(nums)+1):
                all = 0;
                for k in range(i, j):
                    all = all + nums[k];

                x = max(x, all)        
        
        return x;


obj = Solution();

nums = [-2,1-3,4,-1,2,1,-5,4]

x = obj.maxSubArray(nums);

print(x);