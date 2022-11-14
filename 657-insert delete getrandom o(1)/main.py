class RandomizedSet:

    def __init__(self):
        # do intialization if necessary
        self.set = set()

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        # write your code here
        if val not in self.set:
            self.set.add(val)

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        # write your code here
        if val in self.set:
            self.set.remove(val)

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        # write your code here
        elements = list(self.set)
        from random import randint
        idx = randint(0, len(elements) - 1)
        return elements[idx]


obj = RandomizedSet()
obj.insert(1)
obj.remove(2)
obj.insert(2)
print(obj.getRandom())
obj.remove(1)
obj.insert(2)
print(obj.getRandom())
