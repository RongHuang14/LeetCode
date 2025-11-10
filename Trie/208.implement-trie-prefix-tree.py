#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Node:
    def __init__(self):
        self.next = [None] * 26
        self.is_end = False
        
class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.next[idx]:
                cur.next[idx] = Node()
            cur = cur.next[idx]
        cur.is_end = True
            

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if cur.next[idx]:
                cur = cur.next[idx]
            else:
                return False
        return cur.is_end

        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if cur.next[idx]:
                cur = cur.next[idx]
            else:
                return False
        return True 

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

