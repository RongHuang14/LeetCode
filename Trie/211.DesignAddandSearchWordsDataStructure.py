"""
trie + dfs
Search for a word in the trie with support for '.' wildcard.

1. Define dfs(j, cur): matches word[j:] from current node cur.
2. If j == len(word): return whether cur.isEnd is True.
3. If word[j] == '.': try all 26 branches; return True if any dfs(j+1, next) succeeds.
4. Else: go to the child node matching word[j]; return False if missing.
"""
class TrieNode:
    def __init__(self):
        self.next = [None] * 26
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.next[idx]:
                cur.next[idx] = TrieNode()
            cur = cur.next[idx]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(j, cur):
            if j == len(word):
                return cur.isEnd
            c = word[j]
            if c == ".":
                for next in cur.next:
                    if next and dfs(j + 1, next):
                        return True
                return False
            else:
                idx = ord(c) - ord('a')
                if not cur.next[idx]:
                    return False
                return dfs(j + 1, cur.next[idx])

        return dfs(0, self.root)