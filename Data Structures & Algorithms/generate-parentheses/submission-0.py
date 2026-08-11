class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(curr, op, closed):
            if op == closed == n:
                ans.append("".join(curr))
                return 
            
            if op < n:
                curr.append("(")
                backtrack(curr, op + 1, closed)
                curr.pop()

            if closed < op:
                curr.append(")")
                backtrack(curr, op, closed + 1)
                curr.pop()

        ans = []
        backtrack([], 0, 0)

        return ans 