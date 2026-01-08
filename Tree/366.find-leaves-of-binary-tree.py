#
# @lc app=leetcode id=366 lang=python3
#
# [366] Find Leaves of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        # return the height of the tree
        def dfs(node):
            nonlocal res
            if not node:
                return -1
            l_height = dfs(node.left)
            r_height = dfs(node.right)
            curr_height = max(l_height, r_height) + 1
            # If height is 0 and res is [], we need to add res[0]
            # If height is 1 and res has only res[0], we need to add res[1]
            if curr_height == len(res):
                res.append([])
            res[curr_height].append(node.val)
            return curr_height
        dfs(root)
        return res


if __name__ == "__main__":
    sol = Solution()
    # Normal Case 1: Standard Binary Tree
    root1 = TreeNode(1)
    root1.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root1.right = TreeNode(3)
    # Output: [[4, 5, 3], [2], [1]]
    print(f"Normal Case: {sol.findLeaves(root1)}")
    
    # Edge Case 1: Single Node
    root_single = TreeNode(1)
    # Output: [[1]]
    print(f"Single Node: {sol.findLeaves(root_single)}")

    # Edge Case 2: Skewed Tree (Left-leaning line)
    # 1 -> 2 -> 3
    root_line = TreeNode(1, TreeNode(2, TreeNode(3)))
    # Output: [[3], [2], [1]]
    print(f"Skewed Tree: {sol.findLeaves(root_line)}")
# @lc code=end

