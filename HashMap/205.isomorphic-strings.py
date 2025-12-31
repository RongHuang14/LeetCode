#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t, t2s = {}, {}
        for a, b in zip(s, t):
            if ((a in s2t and s2t[a] != b) or (b in t2s and t2s[b] != a)):
                return False 
            s2t[a], t2s[b] = b, a
        return True
    
if __name__ == "__main__":
    sol = Solution()
    # normal case
    s1 = "egg"
    t1 = "abb"
    print(sol.isIsomorphic(s1, t1)) # True

    # edge case: one to many
    s2 = "aae"
    t2 = "bcf"
    print(sol.isIsomorphic(s2, t2)) # False

    # edge case: many to one
    s3 = "aed"
    t3 = "bbf"
    print(sol.isIsomorphic(s3, t3)) # False

        
# @lc code=end

