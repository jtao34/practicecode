class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums)-1
        m = 0
        while m < r:
            if nums[m] == 2:
                nums[m], nums[r] = nums[r], nums[m]
                #dont move m yet, if nums[m] now is 
                r -= 1
            elif nums[m] == 0:
                nums[m], nums[l] = nums[l], nums[m]
                l += 1
                m += 1
            else:
                m += 1
        