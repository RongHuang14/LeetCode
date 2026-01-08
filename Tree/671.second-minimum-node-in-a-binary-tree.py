#
# @lc app=leetcode id=671 lang=python3
#
# [671] Second Minimum Node In a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return -1
            if node.val > root.val:
                return node.val
            left = dfs(node.left)
            right = dfs(node.right)
            if left != -1 and right != -1:
                return min(left, right)
            
            return left if left != -1 else right
        return dfs(root)

if __name__ == "__main__":
    sol = Solution()
    # normal case 1:
    # edge case 1: nodes have same value
    root1 = TreeNode(2)
    root1.left = TreeNode(2)
    root1.right = TreeNode(5)
    root1.right.left = TreeNode(5)
    root1.right.right = TreeNode(7)
    print(f"Normal Case: {sol.findSecondMinimumValue(root1)}") # Output: 5

    # Edge Case 1: All nodes same [2, 2, 2]
    root2 = TreeNode(2, TreeNode(2), TreeNode(2))
    print(f"All nodes same: {sol.findSecondMinimumValue(root2)}") # Output: -1

    # Edge Case 2: Large value candidate
    root3 = TreeNode(2, TreeNode(2), TreeNode(10))
    print(f"Large candidate: {sol.findSecondMinimumValue(root3)}") # Output: 10
# @lc code=end

