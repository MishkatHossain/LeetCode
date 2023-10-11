class Solution:
    def rob(self, nums: List[int]) -> int:
        first, second = 0, 0;

        for i in nums:
            temp = max(i+first, second)

            first = second;
            second = temp;

        return second;
