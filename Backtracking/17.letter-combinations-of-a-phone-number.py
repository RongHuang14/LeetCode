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
        
        ans = []
        path = [' '] * n
        def dfs(i):
            if i == n:
                # 找到答案，数组转换为字符串，加到路径中
                ans.append(''.join(path))
                return 
            # 非边界条件，枚举第i个字母是什么
            for c in MAPPING[int(digits[i])]:
                path[i] = c
                dfs(i + 1)
        dfs(0)
        return ans
# @lc code=end

