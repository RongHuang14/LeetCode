"""
DFS + Hash map ✅
- Use DFS (Depth-First Search) to traverse the entire graph starting from the given node.
- Use a hash map (visited) to keep track of already cloned nodes, mapping original nodes to their copies.
- For each node:
    - If it has already been cloned, return the clone from the hash map (to avoid cycles and repeated cloning).
    - Otherwise, create a new node copy, add it to the hash map, and recursively clone all its neighbors.
- Return the clone of the starting node.

Time Complexity: O(V + E)
    - Each node and each edge is visited once during the traversal.
Space Complexity: O(V)
    - The hash map stores one copy per node, and the recursion stack may grow up to O(V).
Where V is the number of vertices (nodes), and E is the number of edges in the graph.
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(node):
            # node visited
            if node in visited:
                return visited[node]
            # clone node，since it's deep copy so we wont copy its neighbor now
            clone_node = Node(node.val, [])
            # hash map
            visited[node] = clone_node
            # go through its nei and clone its nei
            for nei in node.neighbors:
                clone_node.neighbors.append(dfs(nei))
            return clone_node

        return dfs(node) if node else None