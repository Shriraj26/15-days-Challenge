
def binSearchFirstOccurDupes(arr, elem):

    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start)//2

        # If u get the elem, it may not be the first occur
        if arr[mid] == elem:
            if mid > 0 and arr[mid-1] == arr[mid]:
                end = mid - 1
            else:
                return mid
        elif arr[mid] > elem:
            end = mid - 1
        else:
            start = mid + 1

    return -1


print(binSearchFirstOccurDupes([2, 3, 4, 4, 5, 6], 4))

print(binSearchFirstOccurDupes([4, 4, 4, 4, 5, 6], 4))

print(binSearchFirstOccurDupes([2, 3, 5, 6, 7], 4))

print(binSearchFirstOccurDupes([2, 3, 5, 5, 5, 6], 2))
