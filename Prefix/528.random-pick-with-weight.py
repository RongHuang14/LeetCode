#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#

# @lc code=start
import random
from typing import List

class Solution:
    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total

    def pickIndex(self) -> int:
        target = random.randint(1,self.total)
        
        # search in self.prefix [0, n-1] -> (-1, n)
        left, right = -1, len(self.prefix) 
        while left + 1 < right:
            mid = (left + right) // 2
            if self.prefix[mid] < target:
                left = mid
            else:
                right = mid
        return right 

if __name__ == "__main__":
    # Normal case: w = [1, 3]
    # Expected: index 0 约 2-3次 (25%), index 1 约 7-8次 (75%)
    sol1 = Solution([1, 3])
    print("Normal case: w = [1, 3]")
    results1 = [sol1.pickIndex() for _ in range(10)]
    print(f"Results: {results1}")
    print(f"Count: 0 appears {results1.count(0)} times, 1 appears {results1.count(1)} times")
    
    # Edge case 1: single element
    # Expected: index 0 出现 5次 (100%)
    sol2 = Solution([1])
    print("\nEdge case 1: w = [1]")
    results2 = [sol2.pickIndex() for _ in range(5)]
    print(f"Results: {results2}")
    print(f"Count: 0 appears {results2.count(0)} times (should be 5)")
    
    # Edge case 2: equal weights
    # Expected: 每个index约出现 2-3次 (25% each)
    sol3 = Solution([1, 1, 1, 1])
    print("\nEdge case 2: w = [1, 1, 1, 1]")
    results3 = [sol3.pickIndex() for _ in range(10)]
    print(f"Results: {results3}")
    print(f"Count: 0:{results3.count(0)}, 1:{results3.count(1)}, 2:{results3.count(2)}, 3:{results3.count(3)}")

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

