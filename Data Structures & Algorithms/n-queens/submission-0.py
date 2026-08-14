class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(curr, row, cols, diagonals, anti_diagonals):
            if row == n: 
                ans.append(["".join(r) for r in curr])
            
            for col in range(n):
                diagonal = row - col
                anti_diagonal = row + col

                if col in cols or diagonal in diagonals or anti_diagonal in anti_diagonals:
                    continue
                
                cols.add(col)
                diagonals.add(diagonal)
                anti_diagonals.add(anti_diagonal)
                curr[row][col] = "Q"

                backtrack(curr, row + 1, cols, diagonals, anti_diagonals)

                cols.remove(col)
                diagonals.remove(diagonal)
                anti_diagonals.remove(anti_diagonal)
                curr[row][col] = "."

        ans = []
        curr = [["." for c in range(n)] for r in range(n)]
        backtrack(curr, 0, set(), set(), set())

        return ans 