#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        n = len(letters)

        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return letters[left] if left != n else letters[0]

if __name__ == "__main__":
    sol = Solution()
    
    # 1. Normal Case
    print(f"Normal Case: {sol.nextGreatestLetter(['c', 'f', 'j'], 'f')}") 
    # Output: "j"

    # 2. Edge Case: Target larger than all (Wrap around)
    print(f"Wrap Around: {sol.nextGreatestLetter(['c', 'f', 'j'], 'z')}") 
    # Output: "c"

    # 3. Edge Case: Duplicates
    print(f"Duplicates: {sol.nextGreatestLetter(['e', 'e', 'e', 'n', 'n'], 'e')}") 
    # Output: "n"
# @lc code=end

