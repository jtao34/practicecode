class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        i = 0
        ans = []
        nums = sorted(nums)
        #can use for loop, no need to assign i
        while i < len(nums):
            start = i + 1
            end = len(nums) - 1
            if nums[i] > 0:
                break
            if i != 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            while start < end:
                if nums[i] + nums[start] + nums[end] == 0:
                    triplet = [nums[i], nums[start], nums[end]]
                    ans.append(triplet)
                    #corner case [-2, 0, 0, 2, 2]
                    while start < end and nums[start] == triplet[1]:
                        start += 1
                    while start < end and nums[end] == triplet[2]:
                        end -= 1
                elif nums[i] + nums[start] + nums[end] > 0:
                    end -= 1
                else:
                    start += 1
            i += 1
        return ans
                        