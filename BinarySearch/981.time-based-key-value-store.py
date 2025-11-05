#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
class TimeMap:

    def __init__(self):
        self.keyStore = {} # {key : [(timestamp, val)]}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][0] <= timestamp:
                res = values[m][1] # 继续往右找更接近的
                l = m + 1
            else:
                r = m - 1
        return res
        
# 开区间写法
# class TimeMap:

#     def __init__(self):
#         self.keyStore = {} # {key : [(timestamp, val)]}
        
#     def set(self, key: str, value: str, timestamp: int) -> None:
#         if key not in self.keyStore:
#             self.keyStore[key] = []
#         self.keyStore[key].append((timestamp, value))

#     def get(self, key: str, timestamp: int) -> str:
#         res, values = "", self.keyStore.get(key, [])
#         l, r = -1, len(values)

#         while l + 1 < r:  
#             mid = (l + r) // 2   
#             if values[mid][0] > timestamp: 
#                 r = mid  
#             else:
#                 l = mid  
#         if l == -1: return ""
#         return values[l][1] 

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

