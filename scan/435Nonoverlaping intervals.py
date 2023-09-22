class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #does not matter the starting point, want to remove the next overlapping interval we compare the cur.end and next.start
        intervals.sort(key = lambda i : i[1])
        end = float("-inf")
        count = 0
        for i in intervals:
            if i[0] > end:
                #non-overlapping, keep the next
                end = i[1]
            else:
                #overlap, remove the next, the end point still cur.end
                count += 1
        return count
        