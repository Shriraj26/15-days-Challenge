"""
Just remember maxSoFar and minSoFar
"""


def maximumProfSubArray(arr):

    maxSoFar = arr[0]
    minSoFar = arr[0]
    res = arr[0]

    for i in range(1, len(arr)):
        tempMax = max(arr[i], arr[i]*maxSoFar, arr[i]*minSoFar)
        minSoFar = max(arr[i], arr[i]*maxSoFar, arr[i]*minSoFar)
        maxSoFar = tempMax
        res = max(res, maxSoFar)

    return res


print(maximumProfSubArray([2, 3, -2, 4]))
