"""
1. Naive solution: sorting. Sort each string and group them using a hash map.
   - Time: O(m * n log n)  # Sorting each string takes O(n log n), repeated for m strings.
   - Space: O(m * n)  # Hash map stores up to m keys, each of length up to n.
   (m is the number of strings, n is the length of the longest string)
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list) # sort_str -> original_str
        for s in strs:
            sort_str = "".join(sorted(s))
            str_map[sort_str].append(s)
        return list(str_map.values())

"""
2. hash map: By the definition of an anagram, we only care about the freq of each character in a string.
map char_freq -> original str
with optimal use 26 letters aray.
o(m * n) o(m) ✅
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list) # char_freq -> original str
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord("a")] += 1
            str_map[tuple(count)].append(s)
        return list(str_map.values())