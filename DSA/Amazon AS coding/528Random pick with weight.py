import random
class Solution:
    def __init__(self, w):
        self.w = w
        self.tot = sum(w)
        self.prob = []
        cum_weight = 0
        for i in w:
            cum_weight += i/self.tot
            self.prob.append(cum_weight)
    def pickIndex(self):
        sample = random.random()
        #for i, num in enumerate(self.prob):
        #   if sample < num:
        #       return i
        #use binary search
        l, r = 0, len(self.prob)
        while l <= r:
            mid = l + (r-l)//2
            if sample <= self.prob[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return l
if __name__ == "__main__":
    obj = Solution([1,2,3])
    for i in range(3):
        param = obj.pickIndex()
        print(param)