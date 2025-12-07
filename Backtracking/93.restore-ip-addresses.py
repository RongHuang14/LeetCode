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
        
        # 一个段是否合法？单字符合法，多字符必须没有前导零，且值在 [0, 255] 范围内
        def is_valid(segment):
            return len(segment) == 1 or (segment[0] != "0" and 0 <= int(segment) <= 255)
        
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

