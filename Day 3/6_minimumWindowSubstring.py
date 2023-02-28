"""
Refer to the solution -
https://www.youtube.com/watch?v=jSto0O4AJbM

We will mantain 2 dictionaries, one fixed for the substring 
that we need to find and one that will change and will be compared
with the fixed one..
We need to variables, one to store the length of non repeating chars 
and one that will check if this condition is met

"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        windowDict, targetDict = {}, {}

        # fill up the target Dictionary -
        for c in t:
            targetDict[c] = targetDict.get(c, 0) + 1

        # initialize the variables
        have, need = 0, len(targetDict)

        # Result length and result
        res, resLen = [-1, -1], float('-inf')

        start = 0
        end = 0
        while end < len(s):
            c = s[end]

            # add the char to the window Dict
            windowDict[c] = windowDict.get(c, 0) + 1

            # Check if we need to increment have
            if c in targetDict and windowDict[c] == targetDict[c]:
                have += 1

            # If the window is fulfilled by the characters in target, we need
            # to minimize it
            while have == need:

                # Store the result first
                if resLen > end - start + 1:
                    resLen = end - start + 1
                    res = [start, end]

                # pop from the window Dictionary from left
                windowDict[s[start]] -= 1

                # Decrement have
                if s[start] in targetDict and windowDict[s[start]] < targetDict[s[start]]:
                    have -= 1

                start += 1
            end += 1

        start, end = res
        return s[start: end + 1] if resLen != float('inf') else ""
