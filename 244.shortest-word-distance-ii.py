from collections import defaultdict

# https://leetcode.com/problems/shortest-word-distance-ii/description/
# T:O(N),O(K + L) S:O(N) 
class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self.idx_map = defaultdict(list)
        for idx,word in enumerate(wordsDict):
            self.idx_map[word].append(idx)

    def shortest(self, word1: str, word2: str) -> int:
        i = j = 0
        min_dis = float("inf")
        
        list1 = self.idx_map[word1]
        list2 = self.idx_map[word2]

        while i < len(list1) and j < len(list2):
            min_dis = min(min_dis, abs(list1[i] - list2[j]))
            if list1[i] < list2[j]:
                i += 1
            else:
                j += 1
        return min_dis

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)