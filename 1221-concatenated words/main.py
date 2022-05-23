class Solution:
    """
    @param words: List[str]
    @return: return List[str]
             we will sort your return value in output
    """
    def find_all_concatenated_words_in_a_dict(self, words):
        # write your code here
        self.dicts = set()
        for word in words:
            self.dicts.add(word)

        from collections import defaultdict
        self.concatenations = defaultdict(int)

        anses = list()
        for word in words:
            if word in self.concatenations:
                anses.append(word)
            else:
                res, _ = self.__do_find(word, 0)
                if res:
                    anses.append(word)
        print(self.concatenations)
        return anses

    def __do_find(self, word, concatenation):
        if len(word) == 0:
            if concatenation >= 2:
                return True, concatenation
            else:
                return False, None

        for x in range(1, len(word) + 1):
            if word[:x] in self.dicts:
                if word[x:] in self.concatenations:
                    return True, concatenation + self.concatenations[word[x:]]
                else:
                    res, final = self.__do_find(word[x:], concatenation + 1)
                    if res:
                        if final - concatenation > 1:
                            self.concatenations[word] = final - concatenation
                        return True, final
        return False, None


words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
words = ["a","b","aba","ba","abc"]

solution = Solution()
print(solution.find_all_concatenated_words_in_a_dict(words))
