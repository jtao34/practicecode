class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l + 1 < r:
            mid = l + (r-l)//2
            if nums[mid] < nums[mid+1]:
                l = mid
            else:
                r = mid
        if nums[l] > nums[r]:
            return l
        return r