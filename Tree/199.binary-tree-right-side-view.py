#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 自顶向下
        # 每一层最先访问的节点就是最右边的节点
        # 所以先访问右子树，如果 depth == len(res)，说明 res 里还没有这个深度的节点，就加入 res
        # 如果右子树先遍历了，这个 depth 的最右节点就会被第一个存入 res，确保它是当前层的最右节点
        # 后面再遍历左子树时，如果depth已经存在于 res 里了，就不会重复加入
        res = []
        # 传入节点和当前的深度
        def dfs(node, depth):
            if node is None:
                return
            if depth == len(res):
                res.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return res
            
# @lc code=end

