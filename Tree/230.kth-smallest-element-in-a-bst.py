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
        """
        DST中序遍历找第k小
        
        【切入点】
        DST中序遍历 = 升序序列 → 第k个访问的就是第k小
        
        【核心思路】
        1. 中序遍历（左→根→右）
        2. 用计数器倒数，访问一个节点就 cnt -= 1
        3. cnt == 0 时记录答案并停止遍历
        
        时间 O(H+k)：最多访问 k 个节点
        空间 O(H)：递归栈深度
        """
        def dfs(node): 
            nonlocal ans, cnt
            if not node or ans is not None: # 找到答案就停
                return
            dfs(node.left)
            # 访问当前节点，计数器减1
            cnt -= 1
            if cnt == 0:
                ans = node.val # 找到第k个了！
                return
            dfs(node.right)
        
        ans = None # 答案：初始为None
        cnt = k # 计数器：从k倒数到0
        dfs(root)
        return ans
        
# @lc code=end

