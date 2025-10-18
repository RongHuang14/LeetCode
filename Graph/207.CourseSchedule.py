"""
1.DFS + 三色标记法
这里需要区分两种已访问，正在访问和已完全访问完毕，
有环时dfs(x)时发现下一个结点正在访问中，而不是已经全部访问完毕
如1->2->3->4->2-> 1->0
误区：不能只用两种状态表示节点「没有访问过」和「访问过」。例如上图，我们先 dfs(0)，再 dfs(1)，此时 1 的邻居 0 已经访问过，但是0是已经全部访问完毕，因此这并不能表示此时就找到了环。
算法流程：
    1.建图：把每个 prerequisites[i]=[a,b] 看成一条有向边 b→a，构建一个有向图 g。
    2/创建长为 numCourses 的颜色数组 colors，所有元素值初始化成 0。
    3.遍历 colors，如果 colors[i]=0，则调用递归函数 dfs(i)。
    4.执行 dfs(x)：
        首先标记 colors[x]=1，表示节点 x 正在访问中。
        然后遍历 x 的邻居 y。如果 colors[y]=1，则找到环，返回 true。如果 colors[y]=0（没有访问过）且 dfs(y) 返回了 true，那么 dfs(x) 也返回 true。
        如果没有找到环，那么先标记 colors[x]=2，表示 x 已经完全访问完毕，然后返回 false。
    5.如果 dfs(i) 返回 true，那么找到了环，返回 false。
    6.如果遍历完所有节点也没有找到环，返回 true。

时间复杂度：O(n+m)，其中 n 是 numCourses，m 是 prerequisites 的长度。每个节点至多递归访问一次，每条边至多遍历一次。
空间复杂度：O(n+m)。存储 g 需要 O(n+m) 的空间。
就是O(V + E)
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
        
        colors = [0] * numCourses

        def dfs(x):
            colors[x] = 1
            for nei in graph[x]:
                if colors[nei] == 1 or (colors[nei] == 0 and dfs(nei)):
                    return True # 找到了环
            colors[x] = 2 # x 完全访问完毕，从 x 出发无法找到环
            return False # 没有找到环
        
        
        for i, c in enumerate(colors):
            if c == 0 and dfs(i):
                return False # 有环
        return True # 没有环