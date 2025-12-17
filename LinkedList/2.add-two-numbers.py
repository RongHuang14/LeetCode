#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        两个链表相加 - 模拟竖式加法
        
        切入点：
        1. 链表已经反向存储（个位在前），正好符合加法从个位开始的顺序
        2. 链表已经反向存储（个位在前），正好符合加法从个位开始的顺序
        
        核心思路：
        1. 同时遍历两个链表，逐位相加
        2. 处理进位：每位和 = l1.val + l2.val + carry
           - 当前位 = 和 % 10
           - 新进位 = 和 // 10
        3. 处理长度不等：短链表用0补齐
        4. 处理最后的进位：循环条件包含 carry
        
        技巧：哨兵节点（dummy node）
        - 问题：第一次循环时无法往空链表末尾添加节点
        - 解决：创建 dummy 作为初始"空链表"
        - 好处：统一处理逻辑，避免特判第一个节点
        - 返回：dummy.next 即真正的链表头
        
        时间复杂度：O(max(m, n))，m和n为两链表长度
        空间复杂度：O(max(m, n))，新链表的长度
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            
            curr.next = ListNode(total % 10)
            curr = curr.next
            
            carry = total // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
        
# @lc code=end

