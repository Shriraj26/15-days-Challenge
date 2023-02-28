"""
IN this question you have to find the next permutation for the array, this should be increasing one
and then return the ans...
Refer to this awesome solution video for more details = 
https://www.youtube.com/watch?v=quAS1iydq7U
"""


def nextPermmutation(s):

    # Find the index of the number from behind just less than the longest increasing sequence.
    i = len(s) - 2
    while i >= 0 and s[i + 1] <= s[i]:
        i -= 1

    # Find the number that is just greater than this number from beihind in this sequence
    # and then swap it
    if i >= 0:
        j = len(s) - 1
        while s[j] <= s[i]:
            j -= 1
        (s[i], s[j]) = (s[j], s[i])

    # Then reverse the sequence after the index
    s[::] = s[:i + 1] + s[i + 1:][::-1]

    print(s)


# nextPermmutation([6, 2, 1, 5, 4, 3, 0])
nextPermmutation([1, 3, 2])
# nextPermmutation([2, 1, 3])
# nextPermmutation([3, 2, 1])
