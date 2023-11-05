class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
                return [-1, -1]
        #run binary search twice
        def search_left():
            l, r = 0, len(nums) - 1
            while l + 1 < r:
                mid = l + (r-l)//2
                if nums[mid] < target:
                    l = mid
                else:
                    r = mid
            if nums[l] == target:
                return l
            return r
        def search_right():
            l, r = 0, len(nums) - 1
            while l + 1 < r:
                mid = l + (r-l)//2
                if nums[mid] <= target:
                    l = mid
                else:
                    r = mid
            if nums[r] == target:
                return r
            return l
        return [search_left(), search_right()]