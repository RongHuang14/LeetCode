"""
Encode and decode a list of strings using length-based encoding.

Encoding Strategy:
- Each string is converted to "length#string" format.
- The "#" acts as a separator to distinguish the length from the content.
- Example: ["leet", "code"] → "4#leet4#code"

Decoding Strategy:
- Read the length prefix before each "#".
- Extract the corresponding substring using the length.
- Continue parsing until the entire encoded string is processed.

Time Complexity: O(m) for encode() and decode(),
where m is the total length of all strings in strs.

Space Complexity: O(m + n), where m is the size of the encoded string
and n is the number of strings in the list.
"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#": # Find "#"
                j += 1
            length = int(s[i: j]) # Get length
            i = j + 1 # Move past "#"
            res.append(s[i:i + length])  # Extract string
            i += length  # Move to next
        return res