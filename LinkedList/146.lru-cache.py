#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None # prev和next是链表指针，创建后再连接
        self.next = None
        
class LRUCache:
    """
    LRU Cache 设计思路
    
    核心问题：需要 O(1) 的 get 和 put，还要维护使用顺序
    
    为什么想到 HashMap + 双向链表？
    1. O(1) 查找 → HashMap
    2. O(1) 维护顺序 → 链表
    3. O(1) 删除中间节点 → 双向链表（单链表需要前驱，要 O(n)）
    
    关键设计：
    1. HashMap 存储 key -> Node引用（不是值！）
       - 这样能 O(1) 找到节点在链表中的位置
    2. 双向链表维护顺序
       - 头部 = 最近使用
       - 尾部 = 最久未用
    3. Node 要存 key
       - 删除尾节点时需要知道 key 才能从 HashMap 删除
    4. Dummy head/tail
       - 避免边界判断，所有操作统一处理
    
    操作流程：
    - get: HashMap找到节点 → 移到头部（表示最近使用）
    - put: 
      - 存在：更新值 → 移到头部
      - 不存在：创建节点 → 加到头部 → 检查容量 → 删除尾部
    
    为什么能 O(1)？
    - HashMap 查找: O(1)
    - 链表操作（有节点引用）: O(1)
    - 不需要遍历！
    
    时间：所有操作 O(1)
    空间：O(capacity)
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> Node引用
        
        # dummy节点避免边界处理
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add_to_head(self, node):
        nxt = self.head.next
        nxt.prev = node
        node.next = nxt
        node.prev = self.head
        self.head.next = node
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # 移到头部（最近使用）
        self.remove(node) # 先从原位置删除
        self.add_to_head(node) # 再加到头部
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 更新已存在的
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.add_to_head(node)
        else:
            # 创建新节点
            node = Node(key, value)
            self.cache[key] = node
            self.add_to_head(node)
            
            if len(self.cache) > self.capacity:
                lru = self.tail.prev
                self.remove(lru)
                del self.cache[lru.key]# 链表里删 + cache里删，保持同步
                
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

