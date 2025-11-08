#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        二叉树最大路径和
        
        【切入点】
        类比直径题：直径 = 左深度 + 右深度
        这道题：最大路径和 = 左路径和 + 节点值 + 右路径和
        关键发现：每条路径都有个"转折点"（最高节点）
        
        【核心思路】
        1. 对每个节点，计算经过它的最大路径和（可以是V形）
        2. 但返回给父节点时只能选一边（不能分叉）
        3. 负数路径可以不选：max(0, 子树路径和)
        
        【为什么需要两个值】
        - 更新答案：left + node.val + right（V形路径）
        - 返回父节点：node.val + max(left, right)（单边路径）
        
        【易错点】
        - ans 初始化为 -inf（可能全是负数）
        - 递归用 node.left 不是 root.left
        - 负数不要：max(0, dfs(...))
        
        时间 O(n)：每个节点访问一次
        空间 O(h)：递归栈深度
        """
        ans = float("-inf")
        
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            
            # 获取左右子树贡献，负数不要
            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))
            
            # 更新全局最大（可以V形）
            ans = max(ans, left_max + right_max + node.val)
            
            # 返回单边最大（给父节点用）
            return max(left_max, right_max) + node.val
        
        dfs(root)
        return ans
            
# @lc code=end