#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """双数组写法
        T:O(N)
        S:O(N)
        """
        if root is None:
            return []
        ans = []
        cur = [root]
        even = False
        while cur:
            nxt = []
            vals = []
            for node in cur:
                vals.append(node.val)
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            cur = nxt
            ans.append(vals[::-1] if even else vals)
            even = not even
        return ans 
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:       
        """队列写法
        T:O(N)
        S:O(N)
        """
        if root is None:
            return []
        ans = []
        q = deque([root])
        even = not even

        while q:
            vals = []
            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(vals)
        return ans
                
# @lc code=end

