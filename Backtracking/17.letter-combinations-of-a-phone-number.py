#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    """
    T:O(n * 4^n)
    S:O(n)
    """
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        if not digits:
            return []

        n = len(digits)
        def dfs(i, path):
            if i == n:
                res.append("".join(path)) # 注意这里join会返回一个新的字符串所以不需要shallow copy
                return
            
            d = int(digits[i])
            for char in mapping[d]:
                path.append(char)
                dfs(i + 1, path)
                path.pop()
        res = []
        dfs(0,[])
        return res
# @lc code=end

