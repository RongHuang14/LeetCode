#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
MAPPING = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
class Solution:
    """
    T:O(n * 4^n)
    S:O(n)
    """
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        path = []
        res = []
        def dfs(i):
            if i == n:
                res.append("".join(path))
                return
            
            digit = int(digits[i])
            for letter in MAPPING[digit]:
                path.append(letter)
                dfs(i + 1)
                path.pop()
        dfs(0)
        return res
# @lc code=end

