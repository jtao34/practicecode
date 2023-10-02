class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dif = set()
        l, r = 0, 0
        res = 0
        while r < len(s):
            while s[r] in dif:
                dif.remove(s[l])
                l += 1
            dif.add(s[r])
            r += 1
            res = max(res, r-l)
        return res
        #sliding window
        l, r = 0, 0
        max_len = 0
        dif = set()
        while r <= len(s)-1:
            #keep moving, search max length of a seq starting from l = 0
            if s[r] not in dif:
                dif.add(s[r])
                r += 1
                max_len = max(max_len, r - l)
            #if s[r] is a rep, new seq must start from the next letter of the first time s[r] shown
            #also need to keep track of the current max
            else:
                dif.remove(s[l])
                l += 1
        return max_len
        