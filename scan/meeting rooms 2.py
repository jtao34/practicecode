#meeting room 2
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def minMeetingRooms(self, intervals):
        s = sorted([i.start for i in intervals])
        e = sorted([i.end for i in intervals])
        res, cur = 0, 0
        j, m = 0, 0
        #res max attains before j reaches len(s)
        while j < len(s):
            if s[j] < e[m]:
                j += 1
                cur += 1
            else:
                m += 1
                cur -= 1
            res = max(res, cur)
        return res
             
        