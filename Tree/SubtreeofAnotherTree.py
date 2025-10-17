"""
DFS: O(m * n) o(m + n).m is the number of nodes in  subRoot and
n is the number of nodes in root.
Check if subRoot is a subtree of root:
- For each node in root:
    1. If current subtree == subRoot → return True
       (use isSameTree to compare full structure and values)
    2. Else check left and right subtrees

isSameTree(p, q): checks if two trees are identical (structure + values)
Time: O(m * n), m = nodes in root, n = nodes in subRoot
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 处理空树情况（即使题目约束中不会出现）
        if not subRoot:  # 空树是任何树的子树
            return True
        
        if not root: # 此时subRoot非空，但root为空
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
