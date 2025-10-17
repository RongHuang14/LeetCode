"""
bfs:o(n) o(n)
1. use queue to deal with each level node
2. from root let the node enque and then deque the node unitl all the node it's euque once
3. then enque it's children
4. iterative unitil the queue it's empty
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])

        while q:
            level_len = len(q)
            level = []
            for i in range(level_len):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res