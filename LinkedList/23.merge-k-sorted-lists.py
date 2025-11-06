#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    1. 归并分治法合并K个有序链表
    
    核心思路：
    不要逐个合并（效率低），而是用分治法两两合并
    
    为什么分治更快？
    逐个合并：[1]+[2]=[12], [12]+[3]=[123], [123]+[4]=[1234]...
    - 第1次处理2n个节点，第2次3n，第3次4n...
    - 总计：n(2+3+...+k) = O(nk²) = O(Nk)
    
    分治合并：
    第1轮：[1,2]→[12], [3,4]→[34], [5,6]→[56], [7,8]→[78]
    第2轮：[12,34]→[1234], [56,78]→[5678]
    第3轮：[1234,5678]→[12345678]
    
    时间复杂度分析：O(N log k)
    - N = 所有节点总数（如果k个链表，每个n长，则N=nk）
    - k = 链表个数
    
    详细推导：
    - 递归树有 log k 层（每次对半分）
    - 每层都要处理所有 N 个节点一次
      * 第1层：k/2 次合并，每次平均 2N/k 个节点 = N
      * 第2层：k/4 次合并，每次平均 4N/k 个节点 = N
      * 第3层：k/8 次合并，每次平均 8N/k 个节点 = N
    - 总计：N × log k = O(N log k)
    
    空间复杂度：O(log k)
    - 递归调用栈的最大深度
    - 不需要额外数组存储（原地合并链表）
    """
    def mergeList(self, l1, l2):
        """合并两个有序链表 - O(n+m) n和m是两链表长度"""
        dummy = ListNode()
        cur = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next
            
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        # 分治：对半分
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])   # 递归合并左半部分
        right = self.mergeKLists(lists[mid:])  # 递归合并右半部分
        
        # 合并两个已排序的链表
        return self.mergeList(left, right)
    """
    ================== 另一种最优解：最小堆 ==================
    
    最小堆思路：
    1. 将k个链表的头节点放入最小堆（大小为k）
    2. 每次取出最小节点，将其next节点加入堆
    3. 重复直到堆为空
    
    Python实现要点：
    - 使用heapq，存储(node.val, index, node)三元组
    - index用于处理相同值的情况（避免比较ListNode对象）
    
    伪代码：
    heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
    heapify(heap)
    
    while heap:
        val, idx, node = heappop(heap)
        curr.next = node
        if node.next:
            heappush(heap, (node.next.val, idx, node.next))
    
    堆方法复杂度：
    - 时间：O(N log k) - 每个节点进出堆一次
    - 空间：O(k) - 堆的大小
    
    分治 vs 堆：
    - 时间复杂度相同 O(N log k)
    - 分治空间 O(log k) < 堆空间 O(k)
    - 分治代码更简洁，堆避免递归
    - 两者都是最优解，实际性能差异很小
    """
# @lc code=end

