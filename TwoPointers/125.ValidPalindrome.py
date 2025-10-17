"""
1. brute force: o(n) o(n)
create a copy of the string, reverse it,
and then check for equality.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

"""
2. two pointer: o(n) o(1) left right check
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            # while l < r and not s[l].isalnum():
            # also can use built-in .isalnum()
            while l < r and not self.alphaNum(s[l]):
                l += 1
                
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    # implement alphaNum manually
    def alphaNum(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))