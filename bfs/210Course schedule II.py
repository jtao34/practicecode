class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #still need list of prereq
        prereq = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        #initialize
        for i in prerequisites:
            #which courses need me
            prereq[i[1]].append(i[0])
            indegree[i[0]] += 1
        #put courses with indegree 0 in queue to start
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        ans = []
        while q:
            #courses in q can be taken immediately
            k = q.popleft()
            ans.append(k)
            #whoever needs k, decrement indegree by 1
            for j in prereq[k]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)
        if len(ans) == numCourses:
            return ans
        return []