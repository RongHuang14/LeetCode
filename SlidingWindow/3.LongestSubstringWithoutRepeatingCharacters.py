"""
with O(n) time and O(m) space, where n is the length of the string
and m is the number of unique characters in the string
"""


"""
1.brute force: o(n^2) o(n)
set remove duplicates
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            # length = 1
            seen = set()
            for j in range(i, n):
                # if s[j] == s[i]: # 这样只和起点比较了需要用set去重
                if s[j] in seen:
                    break
                # else:
                #     length += 1
                seen.add(s[j])
            res = max(res, len(seen))
        return res

"""
Sliding window to find the longest substring without repeating characters.
1. Use a set to track characters in the current window.
2. Expand the window by moving right pointer.
3. If s[r] is already in the set, shrink from the left until it's removed.
4. Update max length with the current window size.

Time: O(n), each character is added and removed at most once.
Space: O(k), where k is the character set size (e.g., 128 for ASCII). 
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        seen = set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, r - l + 1)
        return res

"""
Optimized sliding window using a hash map to skip duplicates faster.
1. Use a dict to store the last seen index of each character.
2. Expand the window by moving right pointer.
3. If s[right] is in the map, move left to max(last seen + 1, current left),
   to avoid moving left backward (which would reintroduce duplicates).
   For example: in "abba", when at second 'a', we should move left to 1 (not back to 1 if it's already at 2).
4. Update max length with the current window size.

Time: O(n), each character is visited at most once.
Space: O(k), where k is the character set size.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}  # char -> last seen index
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in mp:
                # move left pointer only forward to avoid shrinking window backwards
                # e.g. in "abba", when at second 'a', last seen 'a' = 0, but l is already 2, so we keep l = 2
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res