"""
Validate Binary Search Tree (BST) using DFS with value bounds.
Idea:
- Use DFS to traverse the tree and validate each node's value is within a valid range.
- For a node:
    - Its left subtree must be in (low, node.val)
    - Its right subtree must be in (node.val, high)
- Start with the full range (-inf, +inf) at root.
- Recursively narrow the valid range as we go down the tree. each time 
- left range will be (low, node.val)
- right range will be (node.val, high)

⚠️ Common mistake:
- Only comparing a node with its direct children is **not enough**!
- We must ensure **all descendants** in the left/right subtree follow the global BST rule.

Time: O(n), each node visited once
Space: O(h), recursion stack depth (h is tree height)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, float("-inf"), float("inf"))

    def valid(self, node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return self.valid(node.left, low, node.val) and self.valid(node.right, node.val, high)
