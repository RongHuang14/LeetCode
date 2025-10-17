"""
1. Merge Lists One By One(like merge two sorted list): o(n*k) o(1)
Merges k sorted linked lists by sequential pairwise merging.
- Start with the first list as the initial result.
- For each i from 1 to k - 1:
    merged = mergeTwoLists(merged, lists[i])
Time:
    O(n * k), where n is the total number of nodes,k is the total number of lists
    - The merged list gets longer with each step
    - Total work is: (2n/k + 3n/k + ... + kn/k) = O(n * k)
Space:
    O(1) — in-place merging using existing nodes
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        merged = lists[0]
        for i in range(1, len(lists)):
            merged = self.mergeTwoLists(merged, lists[i])
        return merged

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

"""
2. divide and conquer: o(nlogk) o(logk)(recursion, iteration o(1))
- Recursively split the input into two halves (divide)
- Merge two sorted lists at each level (conquer)
- Builds a binary merge tree with log k levels:
    merge([l0,l1,l2,l3]) → merge(merge(l0,l1), merge(l2,l3))

Time: O(N log k)
    - N = total number of nodes
    - log k levels × O(N) work total (each node merged log k times)
Space: O(log k) recursion stack
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.divide(lists, 0, len(lists) - 1)

    def divide(self, lists, l, r):
        if l == r:
            return lists[l]
        mid = (l + r) // 2
        left = self.divide(lists, l, mid)
        right = self.divide(lists, mid + 1, r)
        return self.conquer(left, right)

    def conquer(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
"""
3. heap
"""
