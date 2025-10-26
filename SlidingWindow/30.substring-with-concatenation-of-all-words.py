#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """滑动窗口
        题目要找数组单词的任意排列拼接，注意题目说单词必须拼接，中间不能有其他字符，所有单词长度相同
        1. 维护一个定长的滑动窗口， 窗口大小 = 单词长度 * 单词个数
        2. 窗口内切分，把窗口内字符串按单词长度切成小段
        3. 频率匹配：比较切出来的单词频率和words数组的频率是否一致
        滑动的时候可以按照单词长度去滑动，而不是单个单词滑动
        
        **overload 的巧思**
        - 记录"超频"的单词数量
        - 当 overload = 0 时，说明所有单词频率都正好匹配
        - 避免了每次都完整比较两个 Counter
        """
        word_len = len(words[0]) # 一个单词的长度
        window_len = word_len * len(words) # 所有单词的总长度，即窗口大小
        
        # 目标：窗口中的单词出现次数必须与 target_cnt 完全一致
        target_cnt = Counter(words)
        
        ans = []
        # 枚举窗口起点，做 word_len 次滑动窗口
        for start in range(word_len):
            cnt = Counter()
            overload = 0 #  超出目标数量的单词种类数
            
            # 枚举窗口最后一个单词的右端点+1
            for right in range(start + word_len,len(s) + 1, word_len):
                # 1. in_word 进入窗口
                in_word = s[right - word_len: right]
                # 这个单词加入后会不会从"正好"变成"超出"
                # 下面 cnt[in_word] += 1 后，in_word 的出现次数过多
                if cnt[in_word] == target_cnt[in_word]:
                    overload += 1
                cnt[in_word] += 1
                
                left = right - window_len  # 窗口第一个单词的左端点
                if left < 0:
                    continue
                
                # 2. 更新答案
                # 如果没有超出 target_cnt 的单词，那么也不会有少于 target_cnt 的单词
                if overload == 0:
                    ans.append(left)
                
                # 3. 窗口最左边的单词 out_word 离开窗口，为下一轮循环做准备
                out_word = s[left: left + word_len]
                cnt[out_word] -= 1
                if cnt[out_word] == target_cnt[out_word]:
                    overload -= 1
        return ans
                
                
                
            
            
        
# @lc code=end

