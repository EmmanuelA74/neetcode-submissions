class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #BFS (which cells can water from the ocean flow up to)
        pqueue, aqueue = deque(), deque()
        pSeen, aSeen = set(), set()

        rows, cols = len(heights), len(heights[0])

        for c in range(cols):
            pqueue.append((0, c))
            pSeen.add((0, c))
        
        for r in range(1, rows):
            pqueue.append((r, 0))
            pSeen.add((r, 0))
        
        for c in range(cols):
            aqueue.append((rows - 1, c))
            aSeen.add((rows - 1, c))
        
        for r in range(rows):
            aqueue.append((r, cols - 1))
            aSeen.add((r, cols - 1))
        
        def bfs(queue, seen):
            def valid(row, col, height):
                return 0 <= row < rows and 0 <= col < cols and heights[row][col] >= height
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while queue:
                row, col = queue.popleft()
                height = heights[row][col]
        
                for dx, dy in directions:
                    next_row, next_col = row + dx, col + dy

                    if valid(next_row, next_col, height) and (next_row, next_col) not in seen:
                        seen.add((next_row, next_col))
                        queue.append((next_row, next_col))
        
        bfs(pqueue, pSeen)
        bfs(aqueue, aSeen)

        return [list(cell) for cell in pSeen & aSeen]
