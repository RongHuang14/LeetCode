#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        DFS + 回溯在网格中搜索word路径
        
        思路：
        1. 每个格子作为起点，DFS搜索
        2. DFS(i,j,k): 从(i,j)开始匹配word[k:]
           - 越界/不匹配 → False
           - k到末尾 → True  
           - 标记→四方向递归→回溯
        
        优化：
        1. 预检查：word字符数 > board字符数 → False
        2. 反转word：从出现次数少的字符开始搜索
        
        时间：O(mn·3^L)  空间：O(L)
        """
        from collections import Counter
        
        m, n = len(board), len(board[0])
        
        # 优化1：字符数检查
        board_count = Counter(c for row in board for c in row)
        word_count = Counter(word)
        for char, count in word_count.items():
            if board_count[char] < count:
                return False
        
        # 优化2：反转
        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]
        
        def dfs(i, j, k):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            
            tmp = board[i][j]
            board[i][j] = ""
            res = (dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or 
                   dfs(i,j+1,k+1) or dfs(i,j-1,k+1))
            board[i][j] = tmp
            return res
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False
# @lc code=end

