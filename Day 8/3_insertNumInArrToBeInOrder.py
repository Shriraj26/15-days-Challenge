def binSearchInsertElemInOrder(arr, elem):

    start, end = 0, len(arr)-1

    while start <= end:

        mid = start + (end - start)//2

        if arr[mid] > elem:
            if mid == 0 or arr[mid-1] <= elem:
                return mid
            else:
                end = mid - 1
        else:
            if mid == len(arr) - 1:
                return mid
            else:
                start = mid + 1

    return -1


print(binSearchInsertElemInOrder([1, 2, 4, 5, 6, 8], 3))
print(binSearchInsertElemInOrder([1, 2, 4, 5, 6, 8], 0))
print(binSearchInsertElemInOrder([1, 2, 4, 5, 6, 8], 4))
