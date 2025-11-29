#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        res = []
        path = []
        n = len(s)
        
        def is_valid(segment):
            # 检查是否是合法的IP段
            if len(segment) == 0 or len(segment) > 3:
                return False
            
            # 前导0的情况：只有"0"合法，"01""001"等不合法
            if segment[0] == '0' and len(segment) > 1:
                return False
            
            # 数值范围 0-255
            num = int(segment)
            return 0 <= num <= 255
        
        def dfs(i):
             # 必须恰好4段
            if i == n and len(path) == 4:
                res.append(".".join(path))  # 用点号连接
                return
            
            # 剪枝：已经4段了但还有字符
            if len(path) == 4:
                return
            
            # 每段最多3个字符
            for j in range(i, min(i + 3, n)):
                segment = s[i:j+1]
                if is_valid(segment):
                    path.append(segment)
                    dfs(j + 1)
                    path.pop()
        
        dfs(0)
        return res
                    
                
                
        
# @lc code=end

