#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
"""
1. dfs
思路：
a. 建图，注意这里加权图怎么构建,构建无向图, defaultdict(dict) {a:{b, 2.0}}
b. 遍历queries, check每一个start,end能否走通，并返回路径上的累乘权重积，因为需要多次check因此需要每次遍历都要维护自己的visited数组
c. 因此dfs返回累乘积，需要参数（start, end, visited）
        递归边界：1）起点或终点不在图里，return -1.0 2)起点等于，return 1.0 3）visited数组
        递归关系：每次都遍历邻居，计算路径上的累乘积，wei * product (product = dfs(nei, end, visited),)
        注意这里product != -1才说路径能走通，要不遍历完所有邻居后发现都走不通也有可能
"""
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        
        # build undricted weighted graph
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1/val
        
        # return weighted product on the path
        # 注意因为这里需要查询很多次start-end,因此需要每次查询独立，不能用全局的visited，visited也需要作为参数传递
        def dfs(start, end, visited):
            # edge case:起点或终点不在图里
            if start not in graph or end not in graph:
                return -1.0
            
            if start == end:
                return 1.0
            
            visited.add(start)
            
            # 遍历邻居
            for nei, wei in graph[start].items():
                if nei not in visited:
                    product = dfs(nei, end, visited)
                    # 注意这里的返回值就可以判断有无找到路径了,说明nei-end找到了路径
                    if product != -1.0:
                        return wei * product
            
            return -1.0 # 没找到路径
        
        res = []
        for start, end in queries:
            ans = dfs(start, end, set())
            res.append(ans)
        
        return res
                    
            
            
            
        
# @lc code=end

