#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """Iteration
        Iteration the s by reverse from the first non-empty char and if meet the empty again
        or go to the start of the string, then the steps is the answer
        """
        i = len(s) - 1
        step = 0
        # skip the blank
        while i >= 0 and s[i] == " ":
            i -= 1
        # read the word
        while i >= 0 and s[i].isalpha():
            step += 1
            i -= 1
        return step
                
        
# @lc code=end

