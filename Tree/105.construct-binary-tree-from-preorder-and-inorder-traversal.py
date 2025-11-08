#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        分解问题
        从前序和中序遍历构建二叉树
        
        【切入点】
        前序 = [根, 左子树..., 右子树...]
        中序 = [左子树..., 根, 右子树...]
        → 前序第一个是根，用根在中序中定位，就知道左右子树的大小！
        
        【核心思路】
        1. preorder[0] = 当前树的根
        2. 在 inorder 中找根 → 分出左右子树
        3. 关键：inorder 告诉我们左子树有几个节点
        4. 用这个数量切分 preorder
        5. 递归构建左右子树
        
        【例子理解】
        preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
        - 根是3，inorder中3左边[9]→左子树1个节点
        - preorder去掉根，接下来1个给左子树，剩下给右子树
        - 左：pre[9] in[9]  右：pre[20,15,7] in[15,20,7]
        
        时间 O(n)：每个节点处理一次（index查找可优化到O(1)用哈希表）
        空间 O(n)：递归栈深度 + 切片产生的新数组
        """
        if not preorder or not inorder:  
            return None
    
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        
        # 中序切分很直观：根的左边和右边
        inorder_left = inorder[:mid]
        inorder_right = inorder[mid + 1:]
        
        # 前序切分要算左子树大小
        left_size = len(inorder_left)
        preorder_left = preorder[1: left_size + 1]
        preorder_right = preorder[left_size + 1:]
        
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        
        return root
        
# @lc code=end
