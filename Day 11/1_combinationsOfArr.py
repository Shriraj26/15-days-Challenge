"""
here instead of array we go from numbers 1 to n inclusive and fill out the buffer
for length k and return the mainArr
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        mainArr = []
        buffer = [None] * k

        def combo(arrIndex, buffIndex):

            # base case
            if buffIndex == len(buffer):
                mainArr.append(buffer[:])  # this is same as buffer.copy() !!!
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
