"""
1. naive: sorting o(nlogn) o(n)
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort(key=lambda x: x[0])

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

"""
2. heap: maintain top k elements dynamically ✅
   - Time: O(n log k), Space: O(k)
   - Use a min-heap to store k most frequent elements.
   - Remove the smallest frequency when heap size exceeds k.
   - Best when k << n, avoids sorting all elements.
"""
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        min_heap = []
        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        res = []
        while min_heap:
            res.append(heapq.heappop(min_heap)[1])
        return res

"""
3. bucket sort: group by frequency ✅
   - Time: O(n), Space: O(n)
   - Store elements in buckets based on frequency.
   - Retrieve top k from the highest frequency buckets.
   - Best for large n or when k ≈ n, avoids sorting.
"""



"""
4. quickselect: find top k efficiently ✅
   - Time: O(n) expected, O(n^2) worst, Space: O(n)
   - Partition like quicksort but only recurse where needed.
   - Best when k << n, faster than heap in expectation.
   - Can degrade to O(n²) if pivot selection is bad.(array is not evenly eg:sorted)
"""