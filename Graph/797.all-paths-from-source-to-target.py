#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#
"""
算法：DFS + 回溯
思路：从节点0开始，探索所有到达n-1的路径
关键点：
1. DAG保证无环，不需要visited集合
2. 使用回溯法维护当前路径
3. 到达终点时保存路径的副本
"""

# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)
        
        def dfs(node, path):
            # 将当前节点加入路径
            path.append(node)
            
            # 递归边界：到达终点
            if node == n - 1:
                res.append(path.copy())  # 保存当前路径的副本
            else:
                # 递归关系：探索所有邻居节点
                for nei in graph[node]:
                    dfs(nei, path)
            
            # 回溯：移除当前节点，恢复path状态
            path.pop()
            
        dfs(0, [])
        return res
        
# @lc code=end

