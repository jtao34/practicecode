class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = 0
        zero_count = 0
        max_length = 0
        while r < len(nums):
            #condition variable change block put it outside 
            if nums[r] == 0:
                zero_count += 1
            #when move l
            while zero_count > k:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1
            max_length = max(max_length, r-l+1)
            r += 1
        return max_length