#
# @lc app=leetcode id=1188 lang=python3
#
# [1188] Design Bounded Blocking Queue
#

# @lc code=start
class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = deque()
        self.condition = Condition()

    def enqueue(self, element: int) -> None:
        with self.condition:
            # 等待队列不满
            self.condition.wait_for(lambda: len(self.queue) < self.capacity)
            self.queue.append(element)
            self.condition.notify_all()  # 唤醒等待dequeue的线程
    def dequeue(self) -> int:
        with self.condition:
            # 等待队列不空
            self.condition.wait_for(lambda: len(self.queue) > 0)
            element = self.queue.popleft()
            self.condition.notify_all()  # 唤醒等待enqueue的线程
            return element

    def size(self) -> int:
        with self.condition:
            return len(self.queue)
        
# @lc code=end

