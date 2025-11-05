# for height[i], min(leftMost, rightMost) - height[i]
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMost, rightMost = height[l], height[r]
        res = 0
        while l < r:
            # the small height can influence the res
            if leftMost < rightMost:
                res += leftMost - height[l]
                l += 1
                # update the leftMost
                leftMost = max(leftMost, height[l])
            else:
                res += rightMost - height[r]
                r -= 1
                rightMost = max(rightMost, height[r])
        return res
            