"""
Our dictionary will store the freq of the chars in a window from start to end,
To get the longest substring that has same chars after performing atmost K operations, 
We check this - 
(length of window - number of most frequent characters in the window) <= k
This condition should hold true always...
And we calculate max when this condition holds true
To get the most freq chars in the window, we do max(count.values()) this is a O(26) operation
If the condition does not hold true, we increment the start pointer
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        res = 0
        start = 0

        for end in range(len(s)):

            # increment the frequency of the letter in the window
            count[s[end]] = count.get(s[end], 0) + 1

            # check if length of window - most freq chars in window is less than K
            while (end - start + 1) - max(count.values()) > k:
                count[s[start]] = count[s[start]] - 1
                start += 1

            # Store the max in the var
            res = max(res, end - start + 1)

        return res
