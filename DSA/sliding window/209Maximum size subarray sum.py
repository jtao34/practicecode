class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        res = len(nums)
        cur_sum = 0
        if sum(nums) < target:
            return 0
        while r < len(nums):
            cur_sum += nums[r]
            r += 1
            while cur_sum >= target:
                res = min(res, r-l)
                cur_sum -= nums[l]
                l += 1
        return res        