"""
THis is a very good example to count the total number of 
palindromic substrings in a given string... just start 
from an index and go till end... counting the
even length and odd length substrings alon the way...
"""


class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)

        def countSubstringsFromi(start, end):
            count = 0
            while start >= 0 and end < n and s[start] == s[end]:
                count += 1
                start -= 1
                end += 1

            return count

        total = 0
        for i in range(n):
            countEven = countSubstringsFromi(i, i+1)

            countOdd = countSubstringsFromi(i, i)

            total += countEven + countOdd

        return total
