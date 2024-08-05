class Solution:
    """
    @param start: a string
    @param end: a string
    @param dict: a set of string
    @return: a list of lists of string
             we will sort your return value in output
    """
    def find_ladders(self, start, end, dict):
        # write your code here
        import string

        N = len(start)
        dict = list(dict) + [end]
        def find_next_words(word):
            new_words = list()
            for idx in range(N):
                for ch in string.ascii_lowercase:
                    new_word = word[:idx] + ch + word[idx + 1:]
                    if new_word in dict:
                        if not visited[new_word]:
                            new_words.append(new_word)
            return new_words

        from collections import deque
        bfs = deque()
        from collections import defaultdict
        visited = defaultdict(bool)

        bfs.append((start, list() + [start]))
        visited[start] = True

        ans = list()
        while bfs:
            size = len(bfs)
            for x in range(size):
                curr, sequence = bfs.popleft()
                next_words = find_next_words(curr)
                for next_word in next_words:
                    if next_word == end:
                        ans.append(sequence + [next_word])
                    else:
                        bfs.append((next_word, sequence + [next_word]))
                        visited[next_word] = True
            if ans:
                return ans
        return ans


start = "a"
end = "c"
dict = ["a","b","c"]

#start ="hit"
#end = "cog"
#dict = ["hot","dot","dog","lot","log"]

solution = Solution()
print(solution.find_ladders(start, end, dict))