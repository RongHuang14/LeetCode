#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        定长滑动窗口
        1.check P中每个字符以及出现的次数算做异位词，用Counter来统计，如果窗口内Counter(sub_s) == Counter(p)
        就说明符合条件，可以加入答案，长度是len(s2)
        """
        k = len(p)
        count_p = Counter(p)
        count_s = Counter()
        l = 0
        res = []
        
        # edge case
        if len(s) < k:
            return []
        
        for r, c in enumerate(s):
            # 1. r入窗口，更新相关统计
            count_s[c] += 1
            l = r - k + 1
            if l < 0:
                continue
            
            # 2. 更新答案
            if count_s == count_p:
                res.append(l)
            
            # 3. l出窗口,更新相关统计
            count_s[s[l]] -= 1
            # 在定长滑动窗口里，每次减掉的那个字符，一定是之前加过的；
            # 也就是说，它的计数值最多减到 0，绝不可能变成 -1
            
            if count_s[s[l]] == 0:
                del count_s[s[l]]
        return res
            
        
# @lc code=end

