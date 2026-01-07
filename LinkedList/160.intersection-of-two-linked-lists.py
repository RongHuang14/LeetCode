#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        # while l1 != l2,point to different nodes
        while l1 != l2:
            # if l1 is not null,move forward l2. if it's null set it to the begining of l2
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        
        # when the loop exit,l1 l2 both point to the intersection or end of both lists(null).return either one
        return l1
# @lc code=end

