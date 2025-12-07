#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, path, currentSum):
            if not node:
                return

            currentSum += node.val
            path.append(node.val)
            
            if not node.left and not node.right and currentSum == targetSum:
                res.append(path[:])

            dfs(node.left, path, currentSum)
            dfs(node.right, path, currentSum)
            path.pop() # 恢复现场
        
        
        dfs(root,[],0)
        return res
        
# @lc code=end

