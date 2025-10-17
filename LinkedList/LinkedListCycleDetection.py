"""
141. Linked List Cycle
slow, fast two pointer: O(n) time, O(1) space
Floyd's Cycle Detection Algorithm (a.k.a. Tortoise and Hare)

Idea:
- Use two pointers: slow moves 1 step, fast moves 2 steps
- If there's a cycle, fast will eventually meet slow inside the loop
- If there's no cycle, fast will reach the end (null)

Steps:
1. Initialize slow = head, fast = head
2. While fast and fast.next exist:
    - Move slow by 1, fast by 2
    - If they meet → return True (cycle found)
3. Return False (no cycle)

Time: O(n)
Space: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

"""
Advanced version (Leetcode 142): Detect cycle and return the entry point of the cycle.

Extra steps after finding the meeting point:
1. After slow == fast, reset one pointer to head
2. Move both slow and fast one step at a time
3. They will meet again at the entry point of the cycle

Why it works:
- Let a = distance from head to cycle entry
- Let b = distance from entry to meeting point
- Let c = remaining distance to complete the loop
- Then: slow = a + b, fast = 2(a + b)
→ a = c + (n - 1)(b + c)
→ So, head → entry takes a steps, and meeting → entry also takes c steps
→ Both pointers will meet at the cycle entry after a == c steps

Time: O(n)
Space: O(1)
"""