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

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        # Base case
        if not root:
            return 0
        
        # 递归计算左右子树深度
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # 当前深度 = max(左, 右) + 1
        return max(left_depth, right_depth) + 1

if __name__ == "__main__":
    sol = Solution()
    
    # Normal
    #  1 
    # 2 2
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(2)
    print(sol.maxDepth(root1))  # 2
    
    # Edge 1: 单节点
    root2 = TreeNode(1)
    print(sol.maxDepth(root2))  # 1
    
    # Edge 2: 空树
    root3 = None
    print(sol.maxDepth(root3))  # 0
        
# @lc code=end

