#
# @lc app=leetcode id=269 lang=python3
#
# [269] Alien Dictionary
#
"""
1. 如何找出字符顺序？比较相邻单词，找第一个不同的字符
word1[j] -> word2[j]
比较 "wrt" 和 "wrf":
  w = w (相同)
  r = r (相同)  
  t ≠ f → 所以 t < f （t在f前面）

比较 "wrf" 和 "er":
  w ≠ e → 所以 w < e

比较 "er" 和 "ett":
  e = e (相同)
  r ≠ t → 所以 r < t

比较 "ett" 和 "rftt":
  e ≠ r → 所以 e < r
2. 构建图
从上面得到的关系：
- t → f (t在f前面)
- w → e
- r → t  
- e → r
w->e->r->t->f
3. 拓扑排序
```
入度：w=0, e=1, r=1, t=1, f=1
队列：[w]

处理w → e的入度变0 → 队列：[e]
处理e → r的入度变0 → 队列：[r]  
处理r → t的入度变0 → 队列：[t]
处理t → f的入度变0 → 队列：[f]
处理f

"""
# @lc code=start
from collections import defaultdict,deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        #建图和入度
        graph = defaultdict(set) #这里是为了去除重复边
        in_degree = {char:0 for word in words for char in word} # 创建一个字典，包含所有出现过的字符，初始入度都是0
        
        # 比较相邻单词找出字符顺序
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))
            
            # edge case:如果前缀相同但word1更长，说明顺序错误
            if word1[:min_len] == word2[:min_len] and len(word1) > len(word2):
                return ""
            # 找第一个不同的字符
            for j in range(min_len):
                if word1[j] != word2[j]:
                    # 避免重复边
                    if word2[j] not in graph[word1[j]]:   
                            graph[word1[j]].add(word2[j])
                            in_degree[word2[j]] += 1
                    break # 只看第一个不同的！
        
        # 拓扑排序
        q = deque([c for c in in_degree if in_degree[c] == 0])  
        res = []
        
        # BFS
        while q:
            char = q.popleft()
            res.append(char)
            
            for nei in graph[char]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
            
        return "".join(res) if len(res) == len(in_degree) else ""        
            
                  
            
        
# @lc code=end

