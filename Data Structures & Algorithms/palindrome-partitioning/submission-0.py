class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(curr, start):
            #we're at the end of the string
            if start == len(s):
                ans.append(curr[:])
                return 
            
            for i in range(start, len(s)):
                substring = s[start : i + 1]

                if substring == substring[::-1]:
                    backtrack(curr + [substring], i + 1)
                
                    
        ans = []
        backtrack([], 0)

        return ans 