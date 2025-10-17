"""
DFS
1. For each word, start DFS from every cell.
2. dfs(i, j, k): return True if word[k:] can be formed from (i, j).
   - End if k == len(word).
   - Prune if out of bounds, visited, or mismatch.
   - Mark cell, try 4 dirs, restore cell after search.
3. Time: O(m * n * 4^t + s), Space: O(t)
   - m,n: board size; t: max word length; s: sum of all word lengths.
   - 横向分支4（每层最多4个方向）× 深度t（每层匹配一个字母）→ 路径总数最多4^t。
   - 最大深度=单词长度t，因为每一层递归只管匹配单词的下一个字母
"""
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])

        # if word is found on the board turn true, otherwise return false
        def dfs(i, j, k):
            if k == len(word):
                return True
            if not (0 <= i < rows and 0 <= j < cols) or board[i][j] != word[k]:
                return False
            board[i][j] = '#'
            found = (
                dfs(i + 1, j, k + 1) or
                dfs(i - 1, j, k + 1) or
                dfs(i, j + 1, k + 1) or
                dfs(i, j - 1, k + 1)
            )
            board[i][j] = word[k]
            return found

        res = []
        for word in words:
            for i in range(rows):
                for j in range(cols):
                    # word found
                    if dfs(i, j, 0):
                        res.append(word)
        return res


class TrieNode:
    def __init__(self):
        self.children = {}  # key是char, value是TrieNode
        self.isEnd = False  # 单词结尾标记

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True  # 一定要和self.isEnd一致

"""
DFS + Trie,剪枝优化 ✅
- Store all words in a Trie so we can quickly check if a path is a valid prefix.
- As we do DFS, we move forward in both the board and the Trie at the same time.
- If the current letter doesn’t match any Trie branch, we stop searching that path.
- This lets us skip useless branches early, making the search much faster.
"""
class TrieNode:
    def __init__(self):
        self.children = {}  # key是char, value是trienode
        self.isEnd = False  #

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res = set()

        def dfs(i, j, node, path):
            if (i < 0 or i >= ROWS or j < 0 or j >= COLS
                    or board[i][j] == "#" or board[i][j] not in node.children):
                return
            ch = board[i][j]
            nextNode = node.children[ch]
            path += ch
            if nextNode.isEnd:
                res.add(path)
            board[i][j] = '#'
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(i + dx, j + dy, nextNode, path)
            board[i][j] = ch

        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, root, "")

        return list(res)