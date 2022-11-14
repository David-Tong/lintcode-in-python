class StockSpanner:
    def __init__(self):
        """
        @param price:
        @return: int
        """
        self.prices = list()

    def next(self, price):
        # Write your code here.
        self.prices.append(price)
        count = 0
        for p in self.prices[::-1]:
            if p > price:
                return count
            else:
                count += 1
        return count


prices = [100,80,60,70,60,75,85]

solution = StockSpanner()
for price in prices:
    print(solution.next(price))
