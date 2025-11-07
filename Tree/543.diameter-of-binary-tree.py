#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """_summary_
        直径 = 树中任意两节点间的最长路径
        = 某个节点的左子树最深 + 右子树最深
        每条路径都有一个最高点（转折点），在这个点上路径从上升转为下降！
        原问题：找整棵树的最长路径
        转化为：对每个节点，计算"经过它的最长路径"，取最大值
        经过节点 n 的最长路径 = n 的左子树深度 + n 的右子树深度
        """
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            left_hei = dfs(node.left)
            right_hei = dfs(node.right)
            ans = max(ans, left_hei + right_hei)
            return max(left_hei, right_hei) + 1
        dfs(root)
        return ans
        
        
# @lc code=end

