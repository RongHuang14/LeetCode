#
# @lc app=leetcode id=1202 lang=python3
#
# [1202] Smallest String With Swaps
#

# @lc code=start
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False

        # union by size
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        return True

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        """
        Union-Find解法 - 关键是识别出这是连通分量问题
        
        切入点：如果位置i和j能交换，j和k能交换，那么i,j,k三个位置可以任意排列
        这就是图的连通性问题！
        
        算法步骤：
        1. 用Union-Find将所有可交换的位置连接起来，形成若干连通分量
        2. 同一连通分量内的字符可以任意排列，所以排序即可得到最小字典序
        3. 巧妙实现：
           - 收集每个连通分量的所有字符（不记录位置）
           - 逆序排序（大到小），这样可以用O(1)的pop()取最小值
           - 按位置0,1,2...顺序遍历，每个位置分配其所在分量的最小未用字符
        
        时间：O(nlogn + m*α(n))，n=字符串长度，m=pairs数量，α是反阿克曼函数
        空间：O(n)
        
        例子：s="dcab", pairs=[[0,3],[1,2]]
        连通分量：{0,3}的字符['d','b'], {1,2}的字符['c','a']
        排序后分配：位置0→'b', 位置1→'a', 位置2→'c', 位置3→'d'
        结果："bacd"
        """
        n = len(s)
        uf = UnionFind(n)

        # Step 1: 连接所有可交换的位置
        for a, b in pairs:
            uf.union(a, b)
        
        # Step 2: 收集每个连通分量的字符
        mp = defaultdict(list) 
        for i, ch in enumerate(s):
            mp[uf.find(i)].append(ch)
        
        # Step 3: 逆序排序（便于pop最小值）
        for vec in mp.values():
            vec.sort(reverse=True)
        
        # Step 4: 按位置顺序分配最小字符
        ans = []
        for i in range(len(s)):
            x = uf.find(i)
            ans.append(mp[x][-1])
            mp[x].pop()
            
        return ''.join(ans)
# @lc code=end

