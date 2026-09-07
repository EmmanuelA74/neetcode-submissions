class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1

        def dfs(row, col):
            nonlocal curr_area
            for dx, dy in directions:
                next_row, next_col = row +dx, col + dy
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    curr_area += 1
                    dfs(next_row, next_col)


        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(grid)
        n = len(grid[0])
        seen = set()
        max_area = 0
        curr_area = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row, col) not in seen:
                    seen.add((row, col))
                    curr_area += 1
                    dfs(row, col)
                    max_area = max(max_area, curr_area)
                    curr_area = 0
        
        return max_area
                    
                    