class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        l = min(sweetness)
        r = sum(sweetness)
        while l < r:
            mid = l + (r-l)//2
            cnt = 0
            cum_sum = 0
            for num in sweetness:
                cum_sum += num
                if cum_sum > mid:
                    cnt += 1
                    cum_sum = 0
            if cnt < k+1:
                r = mid
            else:
                l = mid + 1
        if r == mid:
            return r
        return l