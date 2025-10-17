"""
Sliding window to find the longest substring where at most k characters can be replaced
to make all characters in the window the same.

1. Use a hashmap to count character frequencies in the current window.
2. Track maxf: the count of the most frequent character in the window.
3. If (window size - maxf) > k, it means we need to replace more than k characters,
   so we shrink the window from the left.
4. Update the maximum length of a valid window at each step.

Time: O(n) — each character is visited at most twice.
Space: O(1) — only 26 uppercase letters are stored in the map.
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxf = 0
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            # shrink window
            while (r - l + 1 - maxf) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
