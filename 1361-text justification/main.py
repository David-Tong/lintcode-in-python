class Solution:
    """
    @param words: an array of string
    @param max_width: a integer
    @return: format the text such that each line has exactly maxWidth characters and is fully
    """
    def full_justify(self, words, max_width):
        # write your code here
        width = 0
        space = []
        lines = []
        line = []
        # arrange words by line
        for word in words:
            if width + len(word) > max_width:
                space.append(max_width - width + len(line))
                width = 0
                lines.append(line[:])
                line = []
            width += len(word) + 1
            line.append(word)

        if len(line) > 0:
            space.append(max_width - width + len(line))
            lines.append(line[:])

        # arrange line by rule
        anses = []
        for idx, line in enumerate(lines):
            if idx == len(lines) - 1 or len(line) == 1:
                ans = ""
                for word in line:
                    ans += word + " "
                ans = ans[:-1]
                ans += " " * (max_width - len(ans))
                anses.append(ans)
            else:
                div = space[idx] // (len(line) - 1)
                mod = space[idx] % (len(line) - 1)
                spaces = [" " * div] * (len(line) - 1) + [""]
                for x in range(mod):
                    spaces[x] += " "
                ans = ""
                for idx2, word in enumerate(line):
                    ans += word + spaces[idx2]
                anses.append(ans)

        return anses


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16

words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20

solution = Solution()
print(solution.full_justify(words, maxWidth))
