#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        # 1. 找长度并停在尾节点
        cur = head
        length = 1
        while cur.next:
            cur = cur.next
            length += 1
        # 2. 计算实际位移，如果不需旋转则直接安全返回
        k = k % length
        if k == 0 or length == 1:
            return head
        # 3. 此时连环，并移动 length - k 步找到新尾部
        cur.next = head 
        for _ in range(length - k):
            cur = cur.next
        # 4. unlink the cycle in new tail
        new_head = cur.next
        cur.next = None
        return new_head

    def print_linked(self, head):
        cur = head
        while cur:
            print(str(cur.val) + "->", end="")
            cur = cur.next
        print("None")
if __name__ == "__main__":
    sol = Solution()
    # normal case 1: k < len(linkedlist)
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    head1.next.next.next = ListNode(4)
    k1 = 2
    new_head1 = sol.rotateRight(head1, k1)
    # 1->2->3->4->1
    sol.print_linked(new_head1) # Expected: 3->4->1->2->None

    # edge case 1: k > len(linkedlist)
    print("\nEdge Case 1 (k=10, len=3):")
    head_e1 = ListNode(0, ListNode(1, ListNode(2)))
    new_head_e1 = sol.rotateRight(head_e1, 10) # 10 % 3 = 1
    sol.print_linked(new_head_e1) # Expected: 2->0->1->None

    # edge case 2: k == 0
    print("\nEdge Case 2 (k=0):")
    head_e2 = ListNode(1, ListNode(2))
    new_head_e2 = sol.rotateRight(head_e2, 0)
    sol.print_linked(new_head_e2) # Expected: 1->2->None

    # edge case 3: linked list is empty
    print("\nEdge Case 3 (Empty):")
    head_e3 = None
    new_head_e3 = sol.rotateRight(head_e3, 5)
    sol.print_linked(new_head_e3) # Expected: None
# @lc code=end

