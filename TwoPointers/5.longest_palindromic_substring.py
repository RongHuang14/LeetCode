"""
Two pointer: O(n) O(1) 
1. treat each char as middle, expand the substring from middle to both side
2. odd middle: s[i]
3. even middle: s[i] and s[i + 1]
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # helper function to return the currrent longes palindrome
        def expand(l, r):
            # expand from middle (l, r) to both side, until it's not a palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]

        res = ""
        for i in range(len(s)):
            # odd: 中心为 s[i]
            odd = expand(i, i)
            # even: 中心为s[i]和s[i + 1]
            even = expand(i, i + 1)
            res = max(res, odd, even, key=len)
        return res
