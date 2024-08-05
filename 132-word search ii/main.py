class Trie(object):
    def __init__(self):
        from collections import defaultdict
        self.children = defaultdict(Trie)
        self.leaf = False
        self.word = None

    def insert(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.leaf = True
        curr.word = word

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
             we will sort your return value in output
    """
    def word_search_i_i(self, board, words):
        # write your code here
        # pre-process
        M = len(board)
        N = len(board[0])
        visited = [[False] * N for _ in range(M)]

        trie = Trie()
        for word in words:
            trie.insert(word)

        ans = set()

        def dfs(visited, x, y ,trie):
            if 0 <= x < M and 0 <= y < N and not visited[x][y]:
                c = board[x][y]
                if c not in trie.children:
                    return

                curr = trie.children[c]
                if curr.leaf:
                    ans.add(curr.word)

                # dfs
                if curr.children:
                    visited[x][y] = True
                    dfs(visited, x + 1, y, curr)
                    dfs(visited, x - 1, y, curr)
                    dfs(visited, x, y + 1, curr)
                    dfs(visited, x, y - 1, curr)
                    visited[x][y] = False
            
        # process
        for x in range(M):
            for y in range(N):
                dfs(visited, x, y, trie)

        ans = list(ans)
        return ans


board = ["doaf","agai","dcan"]
words = ["dog","dad","dgdg","can","again"]

board = ["a"]
words = ["b"]

board = ["a"]
words = ["a"]

board = ["oaan", "etae", "ihkr", "iflv"]
words = ["oath","pea","eat","rain","oathi","oathk","oathf","oate","oathii","oathfi","oathfii"]

board = ["oabn", "otae", "ahkr", "aflv"]
words = ["oa", "oaa"]

solution = Solution()
print(solution.word_search_i_i(board, words))
