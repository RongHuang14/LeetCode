#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """iteration reverse
        each time, we add
        the current digit of a
        the current digit of b
        the last turn carry(进位)
        1. i = the end of a, j = the end of b,carry = the current carry
        res = each position result(we should revsers at the end)
        2. reverse loop:
        each time
        calculate total = carry + a[i] + b[j]
        res = total % 2
        carry = total // 2
        """
        i, j = len(a) -1 , len(b) - 1
        carry = 0
        res = [] # string is immutable, every time we add char to s,it will create a new string
        # a, b not deal with or have carry to deal with(carry != 0)
        while i >= 0 or j >= 0 or carry:
            total = carry # add last turn carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[i])
                j -= 1
            res.append(str(total % 2))
            carry = total // 2
        return "".join(reversed(res))
                
        
# @lc code=end

