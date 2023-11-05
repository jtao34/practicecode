class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #two pointers l, r, let r increase until sum > 7, move l
        l = r = 0
        cum_sum = 0
        res = len(nums)
        if sum(nums) < target:
            return 0
        while r < len(nums):
            cum_sum += nums[r]
            while cum_sum >= target:
                res = min(res, r-l+1)
                cum_sum -= nums[l]
                l += 1
            r += 1
        return res
                