#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):
        """判断两棵树是否完全相同"""
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        【切入点】
        在大树中找小树 = 需要两个功能：
        1. 判断两树是否相同（isSameTree）
        2. 遍历每个节点去比较（递归）
        
        【核心思路】
        对每个节点问三个问题：
        - 从这里开始匹配吗？→ isSameTree(root, subRoot)
        - 在左边吗？→ isSubtree(root.left, subRoot)  
        - 在右边吗？→ isSubtree(root.right, subRoot)
        
        【易错】
        ❌ isSameTree(root.left, subRoot) - 只比较直接子节点
        ✅ isSubtree(root.left, subRoot) - 递归搜索整个子树
        """
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
# @lc code=end