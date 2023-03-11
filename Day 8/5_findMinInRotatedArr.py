"""
If the array is not rotated, then the last element is greater than the first element!!! 
Therefore 
1. if last elem > first elem -- array not rotated, return the first elem
2. if last elem < first elem -- then the array is rotated, we need to think of our modified binary search!

Modified binary search - we need to find the inflection point where the list starts to increase in the 
ascending order!
1. if mid < first elem -- the inflecion point is to left
2. if mid > first elem -- the inflection point is to the right
3. stop when one of these 2 conditions meet - 
    1. if arr[mid] > arr[mid+1] -- means mid + 1 is smallest
    2. if arr[mid - 1] > arr[mid] -- means the mid is smallest
"""


class Solution:
    def findMin(self, arr: List[int]) -> int:
        # Check if not rotated
        if arr[0] <= arr[-1]:
            return arr[0]

        # INflection point
        start, end = 0, len(arr)-1
        while start <= end:

            mid = start + (end - start)//2

            # Found the point when mid is the smallest!!
            if mid > 0 and arr[mid] < arr[mid - 1]:
                return arr[mid]

            # Found the point when mid+1 is smallest!!
            elif mid + 1 < len(arr) and arr[mid] > arr[mid+1]:
                return arr[mid + 1]

            # Sorted from start to mid, inf point to right
            if arr[mid] > arr[0]:
                start = mid + 1
            else:
                end = mid - 1
