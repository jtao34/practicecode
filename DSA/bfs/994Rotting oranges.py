class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ans = -1
        q = deque()
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == 2:
                    q.append((i, j))
        while q:
            ans += 1
            for _ in range(len(q)):
                k = q.popleft()
                grid[k[0]][k[1]] = 0
                for dx, dy in directions:
                    des_x, des_y = k[0] + dx, k[1] + dy
                    if des_x >= 0 and des_x < row_len and des_y >= 0 and des_y < col_len:
                        if grid[des_x][des_y] == 1:
                            grid[des_x][des_y] = 2
                            q.append((des_x, des_y))
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == 1:
                    return -1
        if ans == -1:
            return 0
        return ans