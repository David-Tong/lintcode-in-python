class Solution:
    """
    @param words: a list of words
    @param word1: a string
    @param word2: a string
    @return: the shortest distance between word1 and word2 in the list
    """
    def shortest_distance(self, words, word1, word2):
        # Write your code here
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(list)
        for idx, word in enumerate(words):
            dicts[word].append(idx)

        # process
        list1 = dicts[word1]
        list2 = dicts[word2]
        idx1, idx2 = 0, 0
        L1, L2 = len(list1), len(list2)

        ans = float("inf")
        while idx1 < L1 and idx2 < L2:
            if list1[idx1] < list2[idx2]:
                ans = min(ans, list2[idx2] - list1[idx1])
                idx1 += 1
            else:
                ans = min(ans, list1[idx1] - list2[idx2])
                idx2 += 1
        return ans


words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"

words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "coding"

solution = Solution()
print(solution.shortest_distance(words, word1, word2))
