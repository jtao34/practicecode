class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Map = defaultdict(list)
        ans = []
        for idx, i in enumerate(strs):
           # print(idx, i)
            res = ''.join(sorted(i))
            Map[res].append(idx)
            print(Map)
        for item in Map:
            ans.append([strs[i] for i in Map[item]])
        return ans