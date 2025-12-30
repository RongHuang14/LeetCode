#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Find the lowest common ancestor (LCA) of two nodes in a binary tree.

Approach:
PostOrder
1. Base Cases:
    - If root is None → return None (reached leaf)
    - If root is p or q → return root (found target)
2. Recursively search left and right subtrees
3. Four Possible Scenarios:
    - Both subtrees return None → return None
    - Both subtrees find targets → current root is LCA
    - Only left finds target → return left result
    - Only right finds target → return right result

Time Complexity: O(n) where n is number of nodes
Space Complexity: O(h) where h is tree height (recursion stack)
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # case 1: root is p or q itself, root is the lca
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # case 2: left and right both find the q or q
        if left and right:
            return root
        # case 3: left find or right find
        return left if left else right

if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: left and right both found (different subtrees)
    #     1
    #    / \
    #   2   3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(sol.lowestCommonAncestor(root, root.left, root.right).val)  # 1
    
    # Test 2: only left found (same left subtree)
    #     3
    #    /
    #   5
    #  / \
    # 6   2
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    print(sol.lowestCommonAncestor(root, root.left.left, root.left.right).val)  # 5
    
    # Test 3: only right found (same right subtree)
    #   1
    #    \
    #     3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print(sol.lowestCommonAncestor(root, root.right.left, root.right.right).val)  # 3
    
    # Test 4: edge - p is ancestor of q
    #   1
    #  /
    # 2
    #  \
    #   3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(3)
    print(sol.lowestCommonAncestor(root, root.left, root.left.right).val)  # 2
# @lc code=end

