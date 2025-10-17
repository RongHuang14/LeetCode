"""
two pass: o(n) o(1)
1. first find the length
2. second remove the (length - n)th node from left to right
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        # Special case: delete head
        if n == length:
            return head.next

        # Otherwise, remove (length - n)th node
        cur = head
        for _ in range(length - n - 1):
            cur = cur.next
        cur.next = cur.next.next
        return head

"""
One-pass solution using two pointers. o(n) o(1)
想不到！！！
这个解法的核心数学原理是：
"当快指针先走n步后，两个指针保持n的间距，快指针到终点时，慢指针正好在倒数第n个的前面"
这样因为为了统一处理头节点, slow指向dummy，所以要再走一步
因此快指针指向tail的时候要再走一步，循环结束的条件是while r,这样l才会指向倒数第n个节点的前一个节点

Core idea:
- Use two pointers `l` and `r`, with `r` starting n steps ahead of `l`.
- When `r` reaches the None, `l` is just before the node to remove.
- A dummy node is used to handle edge cases (like removing the head).

Common mistake:
- Initializing both `l` and `r` at `head` will cause `l` to stop at the
  node to delete, not the one before it — making deletion incorrect.
  `l` must start at the dummy node to ensure `l.next` is the target.
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l = dummy
        r = head

        for _ in range(n):
            r = r.next

        while r:
            l = l.next
            r = r.next

        l.next = l.next.next
        return dummy.next

