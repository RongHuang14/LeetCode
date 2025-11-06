#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        深拷贝带随机指针的链表
        
        核心难点：复制节点A时，它的random可能指向还未创建的节点C
        
        解决思路：两次遍历
        1. 第一次遍历：创建所有新节点，建立 原节点→新节点 的映射
        2. 第二次遍历：根据原链表的连接关系，连接新链表的指针
        
        为什么能想到用哈希表？
        - 需要快速找到"原节点对应的新节点"
        - 哈希表是存储映射关系的最佳选择
        
        为什么要两次遍历？
        - 必须先创建所有节点，才能处理random指针
        - 如果边创建边连接，random指向的节点可能还不存在
        
        时间：O(n) - 遍历两次
        空间：O(n) - 哈希表存储n个映射关系
        """
        if not head:
            return None
        
        old_to_new = {}
        
        # 第一次遍历：创建所有新节点
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next
        
        # 第二次遍历：连接next和random指针
        cur = head
        while cur:
            if cur.next:
                old_to_new[cur].next = old_to_new[cur.next]
            if cur.random:
                old_to_new[cur].random = old_to_new[cur.random]
            cur = cur.next
        
        return old_to_new[head]  # 返回新链表的头节点
        
# @lc code=end

