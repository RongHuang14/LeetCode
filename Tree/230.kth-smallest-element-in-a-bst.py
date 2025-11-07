#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node): 
            if not node or len(inorder) == k:
                return
            dfs(node.left)
            if len(inorder) < k:  # 避免多余的添加
                inorder.append(node.val)
            dfs(node.right)
        
        inorder = []
        dfs(root)
        return inorder[k-1]
        
# @lc code=end

