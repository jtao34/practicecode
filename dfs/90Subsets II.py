class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        self.backtracking(res, 0, [], nums)
        return res
    def backtracking(self, res, start, subsets, nums):
        res.append(subsets.copy())
        for i in range(start, len(nums)):
            if i == start or nums[i] != nums[i-1]:
                subsets.append(nums[i])
                self.backtracking(res, i+1, subsets, nums)
                subsets.pop()