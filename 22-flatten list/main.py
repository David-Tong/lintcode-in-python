class Solution(object):

    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        def doFlatten(nestedList):
            ans = list()
            for l in nestedList:
                if type(l) == list:
                    ans.extend(doFlatten(l))
                else:
                    ans.append(l)
            return ans

        return doFlatten(nestedList)


nestedList = [[1,1],2,[1,1]]
nestedList = [1,[4,[6]]]

solution = Solution()
print(solution.flatten(nestedList))
