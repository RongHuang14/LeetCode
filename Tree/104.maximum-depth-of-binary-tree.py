#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         """
#         1. 递归传节点，后序遍历自下往上DFS
#         T: O(N)
#         S: O(N),退化成链表时
#         """
#         if root is None:
#             return 0
#         l_depth = self.maxDepth(root.left)
#         r_depth = self.maxDepth(root.right)
#         return max(l_depth, r_depth) + 1

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        1. 递归传节点个数，先序遍历自上往下DFS
        T: O(N)
        S: O(N),退化成链表时
        """
        ans = 0
        # cnt经过的节点个数,return None
        def dfs(node, cnt):
            if not node:
                return
            cnt += 1 # 进入节点，深度+1
            nonlocal ans
            ans = max(ans,cnt)
            dfs(node.left, cnt)
            dfs(node.right, cnt)
        dfs(root, 0)
        return ans
            
            
            
        
        
# @lc code=end

