"""
Find the lowest common ancestor (LCA) of two nodes in a binary tree.

Approach:
preorder 但是自顶向下的返回因为需要用到返回值来判断lca
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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        #  Reached empty node (base case)
        if not root:
            return None
            
        # Found either p or q
        if root == p or root == q:
            return root
             
        # Recursively search both subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # Case 1: No targets found in either subtree
        if not left and not right:
            return None
            
        # Case 2: Targets found in both subtrees → current root is LCA
        if left and right:
            return root
            
        # Case 3: Target(s) found only in left subtree
        if not right and left:
            return left
            
        # Case 4: Target(s) found only in right subtree
        if not left and right:
            return right