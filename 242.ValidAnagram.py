"""
1. brute force: sort. O(nlogn + mlogm) O(n + m) (sorting)
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

"""
2. hashmap: o(n + m) o(1) since we have at most 26 different characters.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # return Counter(s) == Counter(t)
        for i in range(len(s)): # map char -> freq
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        return count_s == count_t
"""
3. optinal hashmap: o(n + m) o(1), use array to replace hashmap ✅
字母 'a' 到 'z' 可以直接map到数组索引，only have lowercase letter
count[ord(s[i]) - ord('a')]， calculate the offset
nums[index] = freq
相互抵消（cancel each other out） to avoid use two count
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord("a")] += 1
            count[ord(t[i]) - ord("a")] -= 1
        for value in count:
            if value != 0:
                return False
        return True