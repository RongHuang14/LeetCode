#
# @lc app=leetcode id=2273 lang=python3
#
# [2273] Find Resultant Array After Removing Anagrams
#

# @lc code=start
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        """ 保留每组连续anagram的第一个
        连续相同的字母异位词，只保留其中最左边的。
        示例 1 的 abba,baba,bbaa 互为字母异位词，保留最左边的 abba；cd,cd 互为字母异位词，保留最左边的 cd。
        根据题意，如果两个字符串每种字母的出现次数相同，就是一对字母异位词。可以用哈希表统计字母出现次数，也可以把字符串排序，两个排序后相同的字符串是一对字母异位词。
        原始: ["abba", "baba", "bbaa", "cd", "cd"]
            ↑-------组1--------↑    ↑--组2--↑
            (这三个都是anagram)    (这两个是anagram)

        目标: 每组只保留第一个
        结果: ["abba", "cd"]
        遍历相邻元素对(s, t)：
        - 如果s和t是anagram → t属于s的组，不要t
        - 如果s和t不是anagram → t是新组的开始，保留t
        """
        k = 1  # 下一个写入位置（从索引1开始，因为0位置的元素总是保留）
        
        # pairwise是Python 3.10+的函数，返回相邻元素对
        for s, t in pairwise(words):
            if sorted(s) != sorted(t):  # 不是anagram
                words[k] = t  # 把t写到位置k
                k += 1
        
        # 只要前k个元素，del 用来删除列表的一部分
        del words[k:]
        return words
        
        
        
# @lc code=end

