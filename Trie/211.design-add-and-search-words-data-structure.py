#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = [None] * 26 # 26个小写字母的子节点
        self.is_end = False # 标记是否为单词结尾
             
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
 
    def addWord(self, word: str) -> None:
        cur = self.root
        
        for char in word:
            idx = ord(char) - ord('a') # 计算字符对应的索引 (0-25)
            
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        
        cur.is_end = True

    def search(self, word: str) -> bool:
        def dfs(char_idx, node):
            if char_idx == len(word):
                return node.is_end
            char = word[char_idx]
            if char == ".":
                for child in node.children:
                    if child and dfs(char_idx + 1, child):
                        return True
                return False 
            else:
                idx = ord(char) - ord('a')
                if not node.children[idx]:
                    return False
                return dfs(char_idx + 1, node.children[idx])
        return dfs(0, self.root)
            
                
                
                
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

