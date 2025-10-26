#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        滑动窗口
        1.换句话说也就是，只要s2的子串中长度为len(s1)的子串中含有相同的字母和出现次数即可
        2.用counter统计s1出现的字母和次数，if Counter(sub_s2) == Counter(sub_s1)就是找到了
        3.right指针遍历定长滑动窗口，left = right - len(s1) + 1, 统计Counter(s2[left:right+1]), if Counter(s2[left:right+1]) == Counter(sub_s1)
        就是找到了，否则进入下一个循环，最后遍历完了还没找到就return False
        4.边界条件，if left < 0直接skip
        因为窗口内部状态要o(1)更新，因此这里最好不要用counter()，因为这样会带来额外的时间复杂度，每一次都要重新进计算一次窗口的counter 
        Counter(s2[l:r+1])，这个操作每次都要重新扫描子串 s2[l:r+1]，子串长度是 k，时间复杂度是 O(k)，总的时间复杂度会变成O（nk）
        # 每次只对一个字符加、一个字符减
        window[s2[i]] += 1
        window[s2[i - k]] -= 1
        这个窗口是维护出来的，你不再重新统计子串，而是增量更新。
        """
        # k = len(s1)
        # for r in range(len(s2)):
        #     l = r - k + 1
        #     if l < 0:
        #         continue
        #     if Counter(s2[l:r+1]) == Counter(s1):
        #         return True
        #     if r - l + 1 > k:
        #         l += 1
        # return False
        k = len(s1)
        if k > len(s2):
            return False
        
        cnt_s1 = Counter(s1) # 统计 s1 的每种字母的出现次数
        cnt_t = Counter() # 对于 s2 的长为 k 的子串 t，统计 t 的每种字母的出现次数
        
        for i, c in enumerate(s2):
            # 1. 进入窗口
            cnt_t[c] += 1
            if i < k - 1:  # 窗口大小不足 k
                continue
            # 2. 判断子串 t 的每种字母的出现次数是否均与 s1 的相同
            # 最多比较 26 个字母 → O(26) = O(1)
            if cnt_t == cnt_s1: 
                return True
            # 3. 离开窗口，为下一个循环做准备
            cnt_t[s2[i - k + 1]] -= 1
        return False
            
        
        
        

# @lc code=end

