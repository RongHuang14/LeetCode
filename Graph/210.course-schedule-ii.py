#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
"""
1.build the graph
2.use bft to toplogic
"""

# @lc code=start
from collections import defaultdict,deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # bfs
        res = []
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        while q:
            node = q.popleft()
            res.append(node)
            
            for nei in graph[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
        return res if len(res) == numCourses else [] 
        
        
# @lc code=end

