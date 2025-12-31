#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isMirror(self, p, q):  # ← 建议改名
        # base case
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (p.val == q.val 
                and self.isMirror(p.left, q.right) 
                and self.isMirror(p.right, q.left))
    
    def isSymmetric(self, root):
        return self.isMirror(root.left, root.right)

if __name__ == "__main__":
    sol = Solution()
    
    # Normal: 对称树
    #    1
    #   / \
    #  2   2
    root1 = TreeNode(1) 
    root1.left = TreeNode(2)   # ← 改正拼写
    root1.right = TreeNode(2)  # ← 改正拼写
    print(sol.isSymmetric(root1))  # ← 改正方法名
    # True
    
    # Edge 1: 不对称
    #    1
    #   / \
    #  2   2
    #   \   \
    #    3   3
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.right = TreeNode(3)
    root2.right.right = TreeNode(3)
    print(sol.isSymmetric(root2))  # False
    
    # Edge 2: 单节点
    root3 = TreeNode(1)
    print(sol.isSymmetric(root3))  # True
        
# @lc code=end

