#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """
        Encodes a tree to a single string
        树序列化为字符串（前序遍历）
        
        【切入点】
        前序+中序能重建树，但需要两个序列
        关键发现：如果记录空节点(N)，一个前序序列就够了！
        因为N告诉我们"这条路到头了"，能确定树的结构
        
        【核心思路】
        前序遍历：根,左子树,右子树
        空节点也要记录为"N"
        用逗号分隔便于反序列化
        
        时间 O(n)：每个节点访问一次
        空间 O(n)：递归栈深度 + 返回字符串
        """
        if not root:
            return "N"
        left_str = self.serialize(root.left)
        right_str = self.serialize(root.right)
        return f"{root.val},{left_str},{right_str}"
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
            字符串反序列化为树
        
        【切入点】
        序列化是前序遍历，反序列化也按前序顺序消费
        关键：递归的调用顺序 = 前序遍历顺序
        
        【核心思路】
        1. 按顺序读取值（用idx追踪位置）
        2. 遇到数字→建节点→递归建左右
        3. 遇到"N"→返回None（这条路结束）
        4. 递归会自动把值分配到正确位置
        
        【为什么能工作】
        "1,2,N,N,3,N,N"
        读1→建节点1→递归左(消费2,N,N)→递归右(消费3,N,N)
        递归深度对应树的结构！
        
        时间 O(n)：每个值处理一次
        空间 O(n)：递归栈深度
        """
        vals = data.split(",")
        idx = 0
        
        # 构建一棵子树并返回根节点
        def build():
            nonlocal idx
            
            val = vals[idx]
            idx += 1
            
            if val == "N":
                return None
            
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node
        return build()
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

