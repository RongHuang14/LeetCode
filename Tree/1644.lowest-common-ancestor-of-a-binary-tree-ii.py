#
# @lc app=leetcode id=1644 lang=python3
#
# [1644] Lowest Common Ancestor of a Binary Tree II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        
        def helper(node):
            if not node:
                return 0
            
            cur = node == p or node == q
            left = helper(node.left)
            right = helper(node.right)
            
            if cur+left+right == 2 and not self.res:
                self.res = node
            return cur+left+right
                
        helper(root)
        return self.res
# @lc code=end

