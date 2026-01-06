#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
from typing import List
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        res = set()

        for i in range(len(s)-9):
            window = s[i:i+10]
            if window in seen:
                res.add(window)
            else:
                seen.add(window)
        return list(res)


if __name__ == "__main__":
    sol = Solution()
    # Test1
    s1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(sol.findRepeatedDnaSequences(s1)) # ["AAAAACCCCC","CCCCCAAAAA"]
        
# @lc code=end

