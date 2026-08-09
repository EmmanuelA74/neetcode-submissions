class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(curr, start, total):
            if total == target:
                ans.append(curr[:])
                return
            
            for i in range(start, len(nums)):
                num = nums[i]

                if (num + total) <= target:
                    curr.append(num)
                    backtrack(curr, i, num + total)     #i instead of i+1, bc we can reuse the same elem
                    curr.pop()

        ans = []
        backtrack([], 0, 0)
        return ans