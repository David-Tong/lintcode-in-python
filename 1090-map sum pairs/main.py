class Trie(object):

    def __init__(self):
        self.nodes = {}
        self.value = 0

    def insert(self, word, value):
        curr = self
        for ch in word:
            if ch not in curr.nodes:
                curr.nodes[ch] = Trie()
            curr = curr.nodes[ch]
        curr.value = value

    def startsWith(self, prefix):
        curr = self
        try:
            for ch in prefix:
                curr = curr.nodes[ch]
        except:
            return 0

        return self.getValues(curr)

    def getValues(self, curr):
        values = curr.value
        for ch in curr.nodes:
            values += self.getValues(curr.nodes[ch])
        return values


class MapSum:

    def __init__(self):
        self.trie = Trie()

    """
    @param key:
    @param val:
    @return: nothing
    """
    def insert(self, key, val):
        # write your code here
        self.trie.insert(key, val)

    """
    @param prefix:
    @return: nothing
    """
    def sum(self, prefix):
        # write your code here
        return self.trie.startsWith(prefix)


mapsum = MapSum()
mapsum.insert("apple", 3)
print(mapsum.sum("ap"))
mapsum.insert("app", 2)
print(mapsum.sum("ap"))
mapsum.insert("ap", 1)
print(mapsum.sum("ap"))
