class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #connected components. two pass dfs
        def valid(row, col):
            return 0 <= row < rows and 0 <= col < cols and board[row][col] == "O"
               
        def dfs(row, col):
            board[row][col] = "#"   #mark as safe
            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                if valid(next_row, next_col):
                    dfs(next_row, next_col)

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and (row == 0 or row == rows - 1 or col == 0 or col == cols - 1):
                    dfs(row, col)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "#":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"