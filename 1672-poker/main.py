class Solution:
    """
    @param cards:
    @return: the minimal times to discard all cards
    """
    def get_ans(self, cards):
        # Write your code here
        L = len(cards)
        cards_dict = [0] * 10

        # pre-process
        for card in cards:
            cards_dict[card] += 1

        def play(index, count):
            if count >= L:
                return 0

            plays = float("inf")
            while cards_dict[index] == 0:
                index += 1
                if index == 10:
                    return 0


            # discard any single card
            cards_dict[index] -= 1
            plays = min(plays, play(index, count + 1) + 1)
            cards_dict[index] += 1

            # discard two or more cards with the same points
            if cards_dict[index] > 1:
                discards = cards_dict[index]
                cards_dict[index] = 0
                plays = min(plays, play(index, count + discards) + 1)
                cards_dict[index] = discards

            # discard at least 5 consecutive and distinct cards
            if index <= 5:
                has = True
                upper = 10 - index
                k = 0
                while index + k < 10:
                    if cards_dict[index + k] == 0:
                        if k < 4:
                            has = False
                        upper = k
                        break
                    k = k + 1

                if has:
                    for k in range(upper):
                        cards_dict[index + k] -= 1
                    plays = min(plays, play(index, count + upper) + 1)
                    for k in range(upper):
                        cards_dict[index + k] += 1

            return plays

        return play(1, 0)


cards = [2, 2, 2, 3, 4, 5, 7, 1]
cards = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
cards = [1, 1, 2, 3, 4, 5, 6, 6, 8, 9, 9]

solution = Solution()
print(solution.get_ans(cards))
