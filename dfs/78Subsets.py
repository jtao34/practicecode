class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #combination/dfs backtracking
        res = []
        #call
        self.backtracking(res, 0, [], nums)
        return res
    #memorize this plz!!!
    def backtracking(self, res, start, subsets, nums):
        res.append(list(subsets))
        for i in range(start, len(nums)):
            subsets.append(nums[i])
            #start at i + 1, exit at i+1 == len(nums)
            self.backtracking(res, i+1, subsets, nums)
            subsets.pop()
    