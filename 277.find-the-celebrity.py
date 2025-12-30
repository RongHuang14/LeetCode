#
# @lc app=leetcode id=277 lang=python3
#
# [277] Find the Celebrity
#

# @lc code=start
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

# Mock knows API
graph = []

def knows(a, b):
    return graph[a][b] == 1

class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity_can = 0
        # Phase 1: 找候选人
        for i in range(1, n):
            if knows(celebrity_can, i):
                celebrity_can = i
        
        # Phase 2: 验证候选人
        for j in range(n):
            if j == celebrity_can:
                continue
            if knows(celebrity_can, j) or not knows(j, celebrity_can):
                return -1
        return celebrity_can

if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: 有celebrity (1是celebrity)
    #   0 1 2
    # 0[1,1,0]  0认识1
    # 1[0,1,0]  1不认识任何人
    # 2[1,1,1]  2认识1
    graph = [[1,1,0],[0,1,0],[1,1,1]]
    print(sol.findCelebrity(3))  # 1
    
    # Test 2: 没有celebrity
    #   0 1 2
    # 0[1,0,1]  0认识2
    # 1[1,1,0]  1不认识2
    # 2[0,1,1]  2认识1
    graph = [[1,0,1],[1,1,0],[0,1,1]]
    print(sol.findCelebrity(3))  # -1
    
    # Test 3: celebrity是第0个
    #   0 1 2
    # 0[1,0,0]  0不认识任何人
    # 1[1,1,0]  1认识0
    # 2[1,0,1]  2认识0
    graph = [[1,0,0],[1,1,0],[1,0,1]]
    print(sol.findCelebrity(3))  # 0
    
    # Test 4: celebrity是最后一个
    #   0 1 2
    # 0[1,0,1]  0认识2
    # 1[0,1,1]  1认识2
    # 2[0,0,1]  2不认识任何人
    graph = [[1,0,1],[0,1,1],[0,0,1]]
    print(sol.findCelebrity(3))  # 2
        
# @lc code=end

