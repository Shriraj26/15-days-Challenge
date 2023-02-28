"""
This is a similar example to the one we did before in which we found a 
longest substring in the string which has distinct characters..
It has this condition - 
myDict.get(a[end]) is not None and start <= myDict.get(a[end]):
And ours have this - 
if seen[s[startIndex]] == startIndex:
These are good problems that u need to check


Use this example and do dry run - 
aabacccac
"""
from collections import defaultdict


def longestSubWithAtMostKChars(s, k):

    if len(s) == 0 or k == 0:
        return 0

    startIndex, endIndex = 0, 0
    result = 0
    seen = defaultdict(int)

    while endIndex < len(s):

        if s[endIndex] not in seen:
            k -= 1

        seen[s[endIndex]] = endIndex

        # This is most imp condition, in this, we check till k is negative, we have to
        # minimize our window, and till that time, check if currenet element at
        # start index has been already ocurred in the dict before... so for elements
        # in the window after wards, seen[s[startIndex]] > startIndex will hold true
        # until we get an element where seen[s[startIndex]] == startIndex
        while k < 0:
            if seen[s[startIndex]] == startIndex:
                k += 1
            startIndex += 1

        result = max(result, endIndex - startIndex + 1)

        endIndex += 1

    print(result)


longestSubWithAtMostKChars("ecebaa", 2)
