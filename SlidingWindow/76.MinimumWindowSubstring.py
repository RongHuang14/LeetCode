"""
sliding window: o(n) o(k)
1. count the value of t string, also use another hashmap to track the freq in window of s
   need to track the number of char meet the req, count_s and count_t
2. use sliding window
- right to expand until find substring meet the requirements, need == len(count_t)
- left to shrink to find the minums one until it's not meet the req
- update the res when shrink the window
  ✅ Note: only update res when a shorter window is found, using:
      if r - l + 1 < min_length:
          min_length = r - l + 1
          res = s[l: r + 1]
  ⚠️ Bug: previously updated res unconditionally, which may overwrite the true shortest result
3. complexity:
t: o(n) s:o(k), n is the length of s and k is the distinct char in s
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        l = 0
        count_s = {}
        need = 0
        res = ""
        min_length = float("inf")
        for r in range(len(s)):
            count_s[s[r]] = 1 + count_s.get(s[r], 0)
            if s[r] in count_t and count_s[s[r]] == count_t[s[r]]:
                need += 1
            # shrink the window first
            while need == len(count_t):
                # record the res
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    res = s[l: r + 1]
                # then shrink the window
                count_s[s[l]] -= 1
                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    need -= 1
                l += 1
        return res