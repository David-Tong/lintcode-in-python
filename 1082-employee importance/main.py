class Employee:
    def __init__(self, id, importance, reports):
        self.id = id
        self.importance = importance
        self.reports = reports

class Solution:
    """
    @param imput:
    @param id:
    @return: the total importance value
    """
    def getImportance(self, imput, id):
        # Write your code here.
        from collections import defaultdict
        employees = defaultdict(defaultdict)
        imput = eval(imput)
        for imp in imput:
            employees[imp[0]] = Employee(imp[0], imp[1], imp[2])

        def addupImportance(id):
            if id in employees:
                importances = employees[id].importance
                reports = employees[id].reports
                if len(reports) > 0:
                    for report in reports:
                        importances += addupImportance(report)
                return importances
            else:
                return 0

        return addupImportance(id)


employees = "[[1,2,[2]], [2,3,[]]]"
id = 2

#employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
#id = 1
#id = 11

#employees = []
#id = 1

solution = Solution()
print(solution.getImportance(employees, id))
