#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # return height
        def get_height(node):
            if not node:
                return 0
            left_height = get_height(node.left)
            # unbalanced
            if left_height == -1:
                return -1
            right_height = get_height(node.right)
            # unbalanced
            if right_height == -1 or abs(right_height - left_height) > 1:
                return -1
            return max(left_height, right_height) + 1
        return get_height(root) != -1
# @lc code=end

