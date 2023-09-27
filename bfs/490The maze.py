class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        q = deque()
        q.append(start)
        visited = set()
        while q:
            for _ in range(len(q)):
                k = q.popleft()
                if k == destination:
                    return True
                if tuple(k) not in visited:
                    visited.add(tuple(k))
                #can move top?
                    x, y = k[0], k[1]
                    while x-1 >= 0 and maze[x-1][y] == 0:
                        x -= 1
                    q.append([x,y])
                #can move bot?
                    x, y = k[0], k[1]
                    while x+1 <= len(maze)-1 and maze[x+1][y] == 0:
                        x += 1
                    q.append([x,y])
                    x, y = k[0], k[1]
                    while y-1 >= 0 and maze[x][y-1] == 0:
                        y -= 1
                    q.append([x,y])
                    x, y = k[0], k[1]
                    while y+1 <= len(maze[0])-1 and maze[x][y+1] == 0:
                        y += 1
                    q.append([x,y])
        return False