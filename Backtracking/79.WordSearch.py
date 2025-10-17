"""
Determines if the given word exists in the 2D board by searching adjacent cells.

Uses DFS with backtracking:
1. Checks boundaries and character match first
2. Marks visited cells temporarily to prevent reuse
3. Recursively searches all 4 directions for next character
4. Restores cell values when backtracking

Args:
    board: 2D list of characters to search through
    word: Target word to find
    
Returns:
    bool: True if word exists, False otherwise
    
Example:
    >>> exist([["A","B"],["C","D"]], "AB")
    True
    >>> exist([["A","A"]], "AAA")
    False
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(i, j, k):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            
            board[i][j] = ''
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
