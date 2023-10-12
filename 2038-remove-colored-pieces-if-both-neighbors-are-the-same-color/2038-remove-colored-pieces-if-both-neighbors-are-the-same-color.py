class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = 0
        bob = 0

        for index, character in enumerate(colors):
            if index != 0 and index != len(colors)-1:
                if colors[index] == colors[index-1] == colors[index+1] == 'A':
                    alice += 1
                elif colors[index] == colors[index-1] == colors[index+1] == 'B':
                    bob += 1

        return alice > bob 