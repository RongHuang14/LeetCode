#
# @lc app=leetcode id=156 lang=python3
#
# [156] Binary Tree Upside Down
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
    def upsideDownBinaryTree(self, root):
        if root is None or root.left is None:
            return root
        new_root = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right  # node's sibling becomes left child
        root.left.right = root        # node becomes right child
        root.left = None
        root.right = None
        return new_root

def print_tree(root):
    if not root:
        return "[]"
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result

if __name__ == "__main__":
    sol = Solution()
    
    # Normal case 1: one level -> [1,2,3] becomes [2,3,1]
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    print(f"Test 1: {print_tree(sol.upsideDownBinaryTree(root1))}")  # Expected: [2,3,1]
    
    # Normal case 2: two levels -> [1,2,3,4,5] becomes [4,5,2,null,null,3,1]
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    print(f"Test 2: {print_tree(sol.upsideDownBinaryTree(root2))}")  # Expected: [4,5,2,None,None,3,1]
    
    # Edge case: empty tree
    print(f"Test 3: {print_tree(None)}")  # Expected: []
    
    # Edge case: single node
    root4 = TreeNode(1)
    print(f"Test 4: {print_tree(sol.upsideDownBinaryTree(root4))}")  # Expected: [1]
        
# @lc code=end

