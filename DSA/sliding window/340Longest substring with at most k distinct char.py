class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l, r = 0, 0
        res = 0
        dic = defaultdict(int)
        while r < len(s):
            dic[s[r]] += 1
            r += 1
            while len(dic) > k:
                dic[s[l]] -= 1
                if dic[s[l]] == 0:
                    del dic[s[l]]
                l += 1
            res = max(res, r-l)
        return res