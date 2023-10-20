class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #need list of prerequisites and calculate the indegree for each course
        #remember to store prerequisites in a list so we know which courses to decrement their indegree
        prereq = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for i in prerequisites:
            prereq[i[1]].append(i[0])
            indegree[i[0]] += 1
        #initialize queue consists of courses with indegree 0
        q = deque()
        #here append course number that indegree = 0
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        #pop the queue and update the indegree and prereq
        ans = 0
        while q:
            #take course k
            k = q.popleft()
            ans += 1
            for j in prereq[k]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)
        return ans == numCourses    
            
            
            