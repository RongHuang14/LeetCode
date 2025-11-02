#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """One pass brute force:
        遍历两个字符串的每一对字符
        如果c1已有映射：检查是否一致
        如果c1没有映射：尝试建立新映射

        但要先检查c2是否已被占用
        T: O(N)
        S: O(k),k是字符集大小（不同字符的数量）,s_to_t字典：最多存储s中所有不同字符, t_used集合：最多存储t中所有不同字符
        ASCII总共只有128个字符（0-127），空间复杂度：O(128) = O(1)
        """
        s_to_t = {}
        t_used = set() # 防止多对一映射
        for c1, c2 in zip(s, t):
            if c1 in s_to_t:
                if s_to_t[c1] != c2:
                    return False
            else:
                if c2 in t_used:
                    return False
                s_to_t[c1] = c2
                t_used.add(c2)
        return True
            
            
        
# @lc code=end

