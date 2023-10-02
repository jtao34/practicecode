class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        dic = defaultdict(int)
        l, r = 0, 0
        res = 0
        while r < len(s):
            dic[s[r]] += 1
            r += 1
            #if new s[r] add len(dic)
            while len(dic) > 2:
                dic[s[l]] -= 1
                if dic[s[l]] == 0:
                    del dic[s[l]]
                l += 1
            #if new s[r] doesnt add len(dic)
            res = max(res, r-l)
        return res