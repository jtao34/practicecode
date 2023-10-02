class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        self.backtracking(res, visited, [], nums)
        return res
    def backtracking(self, res, visited, subsets, nums):
        if len(subsets) == len(nums):
            res.append(subsets)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtracking(res, visited, subsets+[nums[i]], nums)
                visited.remove(i)