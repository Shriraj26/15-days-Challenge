def lenOfLongestSubstringWithoutRepeatingChars(a):

    start = 0
    end = 1
    lenLongest = len(a[start])
    myDict = {a[start]: start}

    while end < len(a):

        # Check if end exists in the dict and check if current start is less than last occured end element in dict then only inc start
        if myDict.get(a[end]) is not None and start <= myDict.get(a[end]):
            start = myDict.get(a[end]) + 1

        # add the char at end to the dictionary
        myDict[a[end]] = end

        # Check the length of the longest string
        if lenLongest < len(a[start: end+1]):
            lenLongest = len(a[start: end+1])

        end += 1

    return lenLongest


print(lenOfLongestSubstringWithoutRepeatingChars('whatwhywhere'))
