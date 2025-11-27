#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Find the lowest common ancestor (LCA) of two nodes in a binary tree.

Approach:
preorder 但是自顶向下的返回因为需要用到返回值来判断lca
1. Base Cases:
    - If root is None → return None (reached leaf)
    - If root is p or q → return root (found target)
2. Recursively search left and right subtrees
3. Four Possible Scenarios:
    - Both subtrees return None → return None
    - Both subtrees find targets → current root is LCA
    - Only left finds target → return left result
    - Only right finds target → return right result

Time Complexity: O(n) where n is number of nodes
Space Complexity: O(h) where h is tree height (recursion stack)
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        return right
# @lc code=end

