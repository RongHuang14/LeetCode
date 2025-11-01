#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        """Hash set check if there is a loop
        不断求各位数字的平方和，最终只有两种结果：
        到达1（在1处循环）→ 快乐数
        进入其他循环 → 不快乐数
        不断计算一个数各位数字的平方和，这个过程最终会进入循环。判断循环点是否为1。
        1. 循环计算：对当前数n，求其各位数字的平方和，得到新的n
        2. 记录路径：用Set记录出现过的数字
        3. 检测终止：
            如果n变成1 → 快乐数，返回True
            如果n在Set中（重复了）→ 进入非1循环，返回False
        4. 持续迭代：重复步骤1-3直到终止
        数字范围有限，必然会重复
        T: O(logn),处理一个数字需要提取每位数字：O(log n)次操作（n有log n位）,循环次数是有限常数（最多到243以内的循环）,这个循环执行次数 = n的位数 = log₁₀(n)
        S: O(logn), Set会存储遇到的所有不同数字,从大数n收敛到小数的过程中，Set要存储这条路径上的数字（n → log n → log log n → ...），这条路径长度是O(log n)。
        """
        seen = set() # 记录见过的数
        while n != 1 and n not in seen:
            seen.add(n)
            
            # 计算下一个数
            total = 0
            while n > 0:
                digit = n % 10
                total += digit ** 2
                n //= 10 # 去掉最后一位
            n = total
        return n == 1
class Solution:
    def isHappy(self, n: int) -> bool:
        """
        快慢指针判断链表环
        快慢指针找循环点，判断循环点是否是1，是1就是快乐数
        核心思路：
        1. 把数字变换看成链表：19→82→68→100→1→1→1...
        2. 所有数字最终都会进入循环
        3. 快乐数：循环在1（1→1→1...）
        4. 不快乐数：循环在其他地方（4→16→37→...→4）
        
        算法步骤：
        1. 快指针走2步，慢指针走1步
        2. 退出循环的两种情况：
           - fast到达1：说明是快乐数（不用等相遇）
           - fast和slow相遇：说明在环中相遇
        3. 判断：如果fast==1则是快乐数，否则不是
        """
        
        # 计算各位数字的平方和
        def getNext(n):
            total = 0
            while n > 0:
                digit = n % 10
                total += digit ** 2
                n //= 10
            return total
        
        # 初始化：快指针先走一步（避免一开始就相等）
        slow = n
        fast = getNext(n)
        
        # 循环直到：快指针到1 或 快慢相遇
        while fast != 1 and fast != slow:
            slow = getNext(slow)  # 慢指针走1步（bug修正：是slow不是n）
            fast = getNext(getNext(fast))  # 快指针走2步（bug修正：是fast不是n）
        
        # 判断退出原因：是因为到1了吗？
        return fast == 1
# @lc code=end

