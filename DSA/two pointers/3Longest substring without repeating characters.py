class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #l, r two pointers, move r until repeating char, then move l until no repeating char
        l = r = 0
        sub = set()
        res = 0
        while r < len(s):
            if s[r] not in sub:
                sub.add(s[r])
                r += 1
                res = max(res, r-l)
            else:
                while s[r] in sub:
                    sub.remove(s[l])
                    l += 1
        return res
        