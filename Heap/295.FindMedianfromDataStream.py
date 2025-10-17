"""
直接维护一个有序列表确实可以解决问题，但每次插入新数字时都需要保持列表有序，插入操作的时间复杂度为O(n)，这在数据量很大时会很慢。为了提高效率，可以使用两个堆来优化：

最大堆（Max Heap）：存储较小的一半数字，堆顶是这一半的最大值。

最小堆（Min Heap）：存储较大的一半数字，堆顶是这一半的最小值。

通过这种方式，可以确保最大堆的所有元素都小于或等于最小堆的所有元素。这样，中位数就可以通过这两个堆的堆顶元素来快速计算：

如果两个堆的大小相等，中位数就是两个堆顶元素的平均值。

如果两个堆的大小不等，中位数就是元素较多的那个堆的堆顶元素。

"""
import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap = [] # stores the smaller half, max at the top 
        self.min_heap = []  # stores the larger half, min at the top
    
    def addNum(self, num)->None:
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        # balance the heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            moved_num = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, moved_num)
        elif len(self.min_heap) > len(self.max_heap):
            moved_num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -moved_num)
    
    def findMedian(self)->float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return (-self.max_heap[0])
        