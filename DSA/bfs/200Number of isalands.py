class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        row_len = len(grid)
        col_len = len(grid[0])
        res = 0
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == '1':
                    res += 1
                    grid[i][j] == '0'
                    q = deque()
                    q.append((i, j))
                    while q:
                        for _ in range(len(q)):
                            k = q.popleft()
                            #print(grid)
                            for dx, dy in direction:
                                after_x, after_y = k[0] + dx, k[1] + dy
                                if after_x < row_len and after_x >= 0 and after_y < col_len and after_y >= 0:
                                    if grid[after_x][after_y] == '1':
                                        q.append((after_x, after_y))
                                        grid[after_x][after_y] = '0'
        return res