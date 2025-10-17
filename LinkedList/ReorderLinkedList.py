"""
revers second half and merge first and second alternately. o(n) o(1)

Steps:
1. Find the middle node using slow/fast pointers
2. Reverse the second half starting from mid
3. Merge head and reversed second half alternately

Important:
- The last node from the reversed list (head2) is shared with the original list.
- If we continue merging when head2 == last node (e.g., node 3), it might form a self-loop like 3 → 3.
- So we use `while head2.next:` to skip the last node and avoid a cycle.

Example:
Input: [2, 4, 6, 8]
       [8, 6]
1: mid = 6
2: reverse(6) = 8 → 6, head = 2->4->6->None, head2 = 8->6->None
3: merge: 2 → 8 → 4 → 6 -> None,只循环了1次
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        mid = self.findMiddle(head)
        head2 = self.reverseList(mid)
        while head2.next:
            nxt = head.next
            nxt2 = head2.next
            head.next = head2
            head2.next = nxt
            head = nxt
            head2 = nxt2

    # find the middle of the linked list, if list is even,return the second node of the middle
    # slow 每次走 1 步，fast 每次走 2 步，fast 走到终点时，slow 正好在中点
    def findMiddle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head):
        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev