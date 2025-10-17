"""
Backtracking solution to find all unique combinations where candidates sum to target.
The same number may be used unlimited times in a combination.

Approach:
1. Sort candidates (not required but improves efficiency in pruning)
2. Use backtracking to explore all possible combinations:
    - Keep track of current sum to avoid redundant calculations
    - Use 'start' index to prevent duplicate combinations in different orders
    - Prune branches where current sum exceeds target

Complexity:
Time: O(N^(T/M + 1)) where N is candidates count, 
        T is target, M is minimal candidate value
Space: O(T/M) for recursion stack depth
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start, path, currSum):
            if currSum == target:
                res.append(path[:])
                return
            if currSum > target:
                return
            
            for i in range(start, len(candidates)):
                num = candidates[i]
                path.append(num)
                backtrack(i, path, currSum + num)
                path.pop()
        backtrack(0,[], 0)
        return res