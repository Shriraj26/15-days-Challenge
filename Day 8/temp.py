# Keep pivot as the arr[start], then only u can do further processing....

def minInRotatedBinSearch(arr, elem):

    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = start + (end - start) // 2
        if arr[mid] == elem:
            return mid

        if arr[mid] >= arr[start]:

            if elem >= arr[start] and elem < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

        else:

            if elem > arr[mid] and elem <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1


arr = [int(x) for x in input().split()]
elem = int(input())


print('elem at index - ', minInRotatedBinSearch(arr, elem))
