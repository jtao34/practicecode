class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_que = deque()
        d_que = deque()
        for idx, j in enumerate(senate):
            if j == 'R':
                r_que.append(idx)
            else:
                d_que.append(idx)
        while r_que and d_que:
            ra = r_que.popleft()
            di = d_que.popleft()
            if ra < di:
                r_que.append(ra + len(senate))
            else:
                d_que.append(di + len(senate))
        if r_que:
            return "Radiant"
        return "Dire"