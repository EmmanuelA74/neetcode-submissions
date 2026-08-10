class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def backtrack(curr, start, total):
            if total == target:
                ans.append(curr[:])
                return 
            
            for i in range(start, len(candidates)):
                #skip duplicate candidates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                num = candidates[i]
                if (total + num) <= target:
                    curr.append(num)
                    backtrack(curr, i + 1, total + num)
                    curr.pop()

        ans = []
        backtrack([], 0, 0)

        return ans