class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        res = 0
        while l < r:
            max_l, max_r = max(max_l, height[l]), max(max_r, height[r])
            if max_l <= max_r:
                if max_l - height[i] > 0:
                    res += max_l -height[i]
                l += 1
            else:
                if max_r - height[r] > 0:
                    res += max_r -height[r]
                r -= 1
        return res