#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Good Node = 从根到该节点路径上没有比它大的值
        
        【切入点】
        需要判断路径最大值 → 把路径最大值作为参数往下传
        
        【核心思路】
        1. DFS时传递 path_max（从根到当前的最大值）
        2. 如果 node.val >= path_max → 是 good node
        3. 更新 path_max = max(path_max, node.val) 传给子节点
        
        时间 O(n)，空间 O(h)
        """
        def dfs(node, path_max):
            """
            node:当前节点
            path_max:从根节点到当前路径上见过的最大值
            """
            if not node:
                return 0
            count = 1 if node.val >= path_max else 0
            
            new_max = max(node.val, path_max)
            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)
            
            return count
        return dfs(root, root.val)
            
        
            

        
        
# @lc code=end

