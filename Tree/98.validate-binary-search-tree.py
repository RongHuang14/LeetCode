#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 中序
class Solution:
    pre = -inf
    def isValidBST(self, root: Optional[TreeNode], left=-inf, right=inf) -> bool:
        if root is None:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val <= self.pre:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)
        
# 后序
python#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 方法一：中序遍历
# 思路：BST的中序遍历结果应该是严格递增的序列
# 我们记录前一个访问的节点值，确保当前值总是大于前一个值
class Solution:
    pre = -inf
    def isValidBST(self, root: Optional[TreeNode], left=-inf, right=inf) -> bool:
        if root is None:
            return True
        # 先遍历左子树
        if not self.isValidBST(root.left):
            return False
        # 检查当前节点：必须大于前一个节点
        if root.val <= self.pre:
            return False
        self.pre = root.val  # 更新前一个节点值
        # 再遍历右子树
        return self.isValidBST(root.right)
        
# 方法二：后序遍历
# 思路：每个节点向上返回其子树的(最小值, 最大值)
# BST性质：节点值必须 > 左子树最大值 且 < 右子树最小值
class Solution:
    def isValidBST(self, root: Optional[TreeNode], left=-inf, right=inf) -> bool:
        def dfs(node):
            # 空节点返回(inf, -inf)
            # inf作为最小值表示"没有下界"，-inf作为最大值表示"没有上界"
            # 这样设计使得：node.val >= inf 和 node.val <= -inf 永远不成立
            # 从而不会因为子树为空而误判
            if node is None:
                return inf, -inf
            
            # 后序遍历：先处理左右子树，获取它们的范围
            l_min, l_max = dfs(node.left)   # 左子树的(最小值, 最大值)
            r_min, r_max = dfs(node.right)  # 右子树的(最小值, 最大值)
            x = node.val
            
            # BST核心判断：
            # 当前节点必须 > 左子树的最大值（左边所有节点都应该比我小）
            # 当前节点必须 < 右子树的最小值（右边所有节点都应该比我大）
            if x <= l_max or x >= r_min:
                # 违反BST性质，返回错误标记(-inf, inf)
                # 这个组合不可能是正常子树的返回值（最小值>最大值）
                return -inf, inf
            
            # BST合法，返回以当前节点为根的子树范围
            # 整棵子树的最小值：在左边找（左子树最小值 或 当前节点）
            # 整棵子树的最大值：在右边找（右子树最大值 或 当前节点）
            return min(l_min, x), max(r_max, x)
        
        # 最终判断：检查返回的最大值是否为inf
        # 正常情况返回如(1, 9)，最大值是正常数字
        # 错误情况返回(-inf, inf)，最大值是inf
        return dfs(root)[1] != inf
        
# @lc code=end

