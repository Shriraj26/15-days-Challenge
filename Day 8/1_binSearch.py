def binSearch(arr, elem):

    start = 0
    end = len(arr)-1

    while start <= end:
        mid = start + (end - start)//2

        if arr[mid] == elem:
            return mid
        elif arr[mid] > elem:
            end = mid - 1
        else:
            start = mid + 1

    return -1


print(binSearch([1, 2, 3, 4, 5, 6], 6))

print(binSearch([1, 2, 3, 4, 5, 6], 1))

print(binSearch([1, 2, 3, 4, 5, 6], 2))

print(binSearch([1, 2, 3, 4, 5, 6], 4))

print(binSearch([1, 2, 3, 4, 5, 6], 5.5))


print(binSearch([1, 2, 3, 4, 5, 6], 1000))
