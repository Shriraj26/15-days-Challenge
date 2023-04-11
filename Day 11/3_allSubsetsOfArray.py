"""
Change print(buffer) -> print(buffer[:bufferIndex]) and place it just when the function starts
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        mainArr = []
        buffer = [None] * k

        def combo(arrIndex, buffIndex):
            print(buffer[:buffIndex])
            # base case
            if buffIndex == len(buffer):

                return

            if arrIndex == n+1:
                return

            for i in range(arrIndex, n+1):

                # fill the buffer with this startIndex of arr
                buffer[buffIndex] = i

                # get the permutations for next index
                combo(i+1, buffIndex + 1)

        combo(1, 0)

        return mainArr
