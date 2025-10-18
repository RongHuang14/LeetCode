#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

"""
1. BFS找最短路径
a. 建图：把每个单词看作图中的节点，如果两个单词只差一个字母，就在它们之间连一条边
     hit
      |
     hot
    /   \
   dot   lot
    |     |
   dog   log
     \   /
      cog
b. BFS 找最短路径：从 beginWord 开始，用 BFS 找到 endWord 的最短路径
c. 优化技巧
因为 wordList 可能很大，我们不想 O(n²) 地比较所有单词对。可以用一个巧妙的方法：
通配符模式：对于单词 "hot"，它的所有可能模式是：

*ot (第一位可以是任意字母)
h*t (第二位可以是任意字母)
ho* (第三位可以是任意字母)

所有匹配同一个模式的单词都只差一个字母！

"hot" → 生成 *ot, h*t, ho* 三个模式
"dot" → 生成 *ot, d*t, do* 三个模式
nei["*ot"] = ["hot", "dot", "lot"] → 它们互为邻居！
"""
# @lc code=start
from collections import defaultdict,deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        neighbor = defaultdict(list)
        wordList.append(beginWord)
        
        # 构建模式字典
        # 为每个单词生成所有可能的模式
        for word in wordList:
            for i in range(len(word)):
                # 把第i个位置换成*，得到一个模式
                pattern = word[:i] + '*' + word[i+1:]
                # 把这个单词加到对应模式的列表里
                neighbor[pattern].append(word)
        
        # bfs
        visited = set([beginWord]) # 已访问集合
        q = deque([beginWord]) # 队列实现逐层探索，起点入队
        res = 1                     # 记录的是到达当前层的路径长度（包含起点）
        
        # BFS 主循环：逐层探索直到找到目标或队列为空
        while q:
            # 关键：处理当前层的所有节点
            # 用 for range(len(q)) 确保只处理当前层，不混入下一层
            # 此时 res = 当前层的路径长度
            level_size = len(q)
            for _ in range(level_size):
                # 取出当前节点（队首）
                word = q.popleft()
                
                # 生成当前单词的所有通配符模式
                # 通过模式找到所有只差一个字母的邻居
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    
                    # 遍历所有匹配此模式的单词（潜在邻居）
                    for nei in neighbor[pattern]:
                        if nei not in visited:
                            # 找到目标！BFS保证这是最短路径
                            if nei == endWord:
                                return res + 1 # 找到了，直接返回
                            # 将新发现的节点标记为已访问
                            visited.add(nei)
                            # 加入队列，作为下一层待探索节点
                            q.append(nei)
            
            # 当前层处理完了，没找到目标
            # 准备处理下一层，所以路径长度要+1
            res += 1
        
        # 循环结束了，说明 q 空了
        # q 空了 = 没有节点可以探索了
        # 还没返回 = 没找到 endWord
        # 队列空了还没找到目标，说明无法到达
        return 0
                 

        
        
# @lc code=end

