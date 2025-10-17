"""
Check if all brackets are valid using a stack. o(n) o(n)

- Every closing bracket must match the most recent unmatched opening bracket.
- This is a classic LIFO (Last-In, First-Out) structure — the last opened must be closed first.
  Example: s = "({[]})" is valid because each closing bracket matches the top of the stack.
- For every char in s:
  - If it's a closing bracket, check if it matches the stack top.
  - If it matches, pop the stack; otherwise, return False.
  - If it's an opening bracket, push it onto the stack.

Time: O(n)
Space: O(n) for the stack
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        clost_to_map = {")": "(", "]":"[", "}":"{"}
        for c in s:
            if c in clost_to_map:
                if stack and stack[-1] == clost_to_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False