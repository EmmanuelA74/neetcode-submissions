class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #graph bfs (start from all rotting oranges)

        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        seen = set()
        m = len(grid)
        n = len(grid[0])
        fresh = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    seen.add((row, col))
                    queue.append((row, col, 0))
                elif grid[row][col] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        result = 0
        while queue:
            row, col, minute = queue.popleft()
            result = max(result, minute)

            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy

                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    fresh -= 1
                    seen.add((next_row, next_col))
                    queue.append(((next_row, next_col, minute + 1)))
        
        return result if fresh == 0 else -1