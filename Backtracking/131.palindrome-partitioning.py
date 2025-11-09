#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        回文分割 - 找出所有可能的回文子串分割方案
        
        算法思路：
        1. 使用回溯法枚举所有可能的分割方式
        2. dfs(i) 表示从索引i开始，分割s[i:]的所有方案
        3. 对于每个位置i，尝试所有可能的分割点j (i <= j < n)
           - 如果s[i:j+1]是回文，则这是一个有效分割
           - 将s[i:j+1]加入path，继续递归处理s[j+1:]
           - 回溯时撤销选择
        4. 当i==n时，说明整个字符串都被分割完了，记录当前方案
        
        举例: s = "aab"
        递归树：
                        ""
                    /    |    \
                  "a"   "aa"   X(aab不是回文)
                 /  \     |
               "a"   X   "b"
               |
              "b"
        结果: [["a","a","b"], ["aa","b"]]
        
        时间复杂度: O(n * 2^n)
        - 最坏情况下，字符串可以在每个位置选择分割或不分割，共2^n种分割方式
        - 对于每种分割方案，需要O(n)时间来检查回文和构建结果
        - 总时间 = 分割方案数 × 每个方案的处理时间 = 2^n × n
        
        空间复杂度: O(n)
        - 递归调用栈深度最大为n（每次至少分割一个字符）
        - path数组最大长度为n（每个字符单独分割）
        - 不计算答案数组的话，额外空间为O(n)
        """
        ans = []
        path = []
        n = len(s)
        
        def dfs(i):
            # i表示当前要处理s[i:]的部分
            if i == n:
                # 所有字符都处理完了，找到一个有效分割
                ans.append(path.copy())
                return
            
            # 枚举分割点：从i到n-1
            # j是结束位置（包含），所以子串是s[i:j+1]
            for j in range(i, n):
                t = s[i: j + 1]  # 当前尝试的子串
                if t == t[::-1]:  # 检查是否回文
                    path.append(t)  # 选择：将回文子串加入路径
                    dfs(j + 1)      # 递归：处理剩余部分s[j+1:]
                    path.pop()      # 回溯：撤销选择
        
        dfs(0)
        return ans

# @lc code=end

