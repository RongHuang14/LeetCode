#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """DFS: We will find leaf nodes, root.left is null and root.right is null
        Until we find one of leaf nodes, we will subtract node value we find from targetSum so that we will be able to make sure the current path is true case or false case.
        1. start from root, accumulate the path sum, we can use remaining to check
        2. recursion base case: 
        - empty node: if not node: return False
        - leaf node: if not node.left and not node.right:
            return root.val == root.target
        3. Update the Target Sum
            targetSum -= root.val
        4. Recursive Calls to Left and Right Subtrees: left and right just have one path then meet the require
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum - root.val  == 0
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
# @lc code=end

