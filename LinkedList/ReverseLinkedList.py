"""
Reverse a singly linked list in-place.

Idea:
- Iterate through the list with two pointers: prev and cur
- At each step:
    1. Save the next node (nxt = cur.next)
    2. Reverse the current pointer (cur.next = prev)
    3. Move prev and cur forward

Time: O(n)
Space: O(1)
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
