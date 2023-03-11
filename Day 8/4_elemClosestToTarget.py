def binSearchClosestElem(arr, elem):

    def record(result, mid, elem):
        if result == -1 or abs(arr[mid]-elem) < abs(arr[result]-elem):
            return mid
        return result

    result = -1
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start)//2
        result = record(result, mid, elem)

        if arr[mid] == elem:
            return mid
        elif arr[mid] > elem:
            end = mid - 1
        else:
            start = mid + 1

    return result


print(binSearchClosestElem([10, 20, 30, 40, 50], 23))

print(binSearchClosestElem([10, 20, 30, 40, 50], -1))

print(binSearchClosestElem([10, 20, 30, 40, 50], 100))

print(binSearchClosestElem([10, 20, 30, 40, 50], 20))
