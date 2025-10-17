"""
这题不太会
1. dfs: o(n^2) o(n)
Recursive DFS to construct binary tree from preorder and inorder.
- The first element in preorder is always the root.
- Find the index of this root in inorder to split:
    - Left subtree → inorder[:mid], preorder[1:mid+1]
    - Right subtree → inorder[mid+1:], preorder[mid+1:]
- Recursively build left and right subtrees.

Time: O(n^2) due to repeated list slicing and index search.
Space: O(n) for recursion stack and slices.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # Root is always the first in preorder
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        # Recursively build left and right subtrees
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root
"""
2. hashmap + dfs: o(n) o(n)
use hashmap to optimize
"""
"""
Build binary tree from preorder and inorder traversal (Optimized)

Idea:
- The first node in preorder is always the root.
- Use a hashmap to store value -> index in inorder for O(1) lookup.
- Use a global index to track current root in preorder.
- Recursively build left and right subtrees using inorder boundaries.

Time: O(n)
Space: O(n) (for hashmap and recursion stack)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}  # inorder value to index map
        self.pre_idx = 0  # current root index in preorder

        def dfs(l, r):
            if l > r:  # empty subtree
                return None

            # current root value
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            # build the root node
            root = TreeNode(root_val)

            # find the root index in inorder
            mid = indices[root_val]

            # recursively build left and right subtrees
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root

        return dfs(0, len(inorder) - 1)