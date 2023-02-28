# this is O(n) solution using dictionary
from ctypes.wintypes import tagRECT


def twoSum(arr, target):

    myDict = {arr[0]: 0}
    for i in range(1, len(arr)):

        # Check if target - current elem in arr exists in the dictionary
        if myDict.get(target - arr[i]) is not None:
            return [myDict.get(target - arr[i]), i]

        myDict[arr[i]] = i

# this is O(nlog(n)) solution using sorting and 2 pointers


def twoSumUsingTwoPointer(arr, target):

    # u need to sort the array first
    arr.sort()

    start = 0
    end = len(arr) - 1
    while start <= end:
        if arr[start] + arr[end] == target:
            return [start, end]
        elif arr[start] + arr[end] < target:
            start += 1
        else:
            end -= 1

    return []


print(twoSum([3, 2, 4], 6))

print(twoSumUsingTwoPointer([3, 2, 4], 6))
