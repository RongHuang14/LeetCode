"""
In-order DFS (left → root → right) for BST:
- The kth visited node during in-order traversal is the kth smallest.
- Use a counter to track how many nodes we've seen.
- Once count == k, we record the result and stop recursion early.

Time: O(H + k)  (H is tree height, worst O(n) if skewed)
Space: O(H)     (call stack from recursion)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder(root)
        # return self.res
        cnt = k
        res = root.val

        # inorder
        def dfs(node):
            nonlocal cnt, res
            if not node:
                return
            
            dfs(node.left)
            cnt -= 1
            if cnt == 0:
                res = node.val
                return
            dfs(node.right)
        
        dfs(root)
        return res