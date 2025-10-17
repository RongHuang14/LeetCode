"""
DFS on BST
- If both p and q are smaller than root → search left
- If both p and q are greater than root → search right
- Else → current node is the split point → return it as LCA
Time:  O(n) in the worst case (e.g. tree looks like a linked list)
Space: O(n) for the recursion stack
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Case 1: both on left
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
