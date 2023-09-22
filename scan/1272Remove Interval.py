class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        for i in intervals:
            #4 conditions
            #1. if i is covered, i removed, will not be appended, go to next interval
            #2. no overlap
            if i[1] <= toBeRemoved[0] or i[0] >= toBeRemoved[1]:
                res.append(i)
            else:
                #3. left side remain
                if i[0] < toBeRemoved[0]:
                    res.append([i[0], toBeRemoved[0]])
                #4. right side remain
                if i[1] > toBeRemoved[1]:
                    res.append([toBeRemoved[1], i[1]])
                #both side remain if both condition satisfied (toBeRemoved is covered by i)
        return res
            
        