class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        q = deque()
        #distance also need to be compared so included in the tuple
        q.append(tuple(start + [0]))
        #lookup table
        visited = {tuple(start) : 0}
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            prev_x, prev_y, dist = q.popleft()
            for dx, dy in direction:
                x, y, dis = prev_x, prev_y, dist
                while 0 <= x + dx < len(maze) and 0 <= y + dy < len(maze[0]) and maze[x+dx][y+dy] == 0:
                    x += dx
                    y += dy
                    dis += 1
                #check if pos not visited, or a better path -> update smaller dis
                if (x,y) not in visited or ((x,y) in visited and visited[(x,y) > dis]):
                     visited[(x,y)] = dis
                     q.append((x,y,dis))
        if tuple(destination) not in visited:
            return -1
        return visited[tuple(destination)]
                    
            