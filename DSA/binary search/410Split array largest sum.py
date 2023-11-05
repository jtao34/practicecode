class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        
        while l < r:
            mid = l + (r - l) // 2
            count = 1  # Initialize the number of subarrays to 1
            cum_sum = 0
            
            for num in nums:
                cum_sum += num
                if cum_sum > mid:
                    count += 1
                    cum_sum = num  # Start a new subarray
            
            if count > k:
                l = mid + 1
            else:
                r = mid

        return l