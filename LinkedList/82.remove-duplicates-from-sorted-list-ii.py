#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        T:O(N),虽然是循环套循环，但是每次移动要么删除一个节点要么向右移动，因此o(N)
        S:O(1)
        """
        dummy = ListNode(next=head)
        cur = dummy
        
        while cur.next and cur.next.next:
            val = cur.next.val
            # 不断删除所有值为val的节点，然后通过改变cur.next
            # 因为cur.next其实是一直在删除重复节点的所以需要不断检查cur.next直到cur.next不为val
            if cur.next.next.val == val:
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
# @lc code=end

