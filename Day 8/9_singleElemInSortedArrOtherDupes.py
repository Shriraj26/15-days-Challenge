"""
Ye Mast hai bhai!!! Jam gaya apun ko!
Mid can repeat or not repeat...
If mid does not repeat, it means that it is the ans, return it!
Else if it repeats, it repeats in right or left!
    If repeats in left: check the length of half arr(except mid),
    if len of half arr is odd, go right as left cannot have non repeating elem
    Else go left

    If it repeats in right, check the length of half arr(except mid),
    If len of half arr is odd, go left as now right cannot have non repearing elem
    Else go right

Carefull, we do end = mid - 2 and start = mid + 2 to avoid the repeating mid in the 
half array!!
If we come accross start == end, then we return that elem at last

"""


class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:

        start = 0
        end = len(arr) - 1
        n = len(arr)
        counter = 0

        while start < end:

            mid = start + (end - start) // 2

            # When mid is the non repeating elem
            if mid > 0 and mid+1 < n and arr[mid-1] < arr[mid] < arr[mid+1]:
                return arr[mid]

            # mid repeats in right
            if mid > 0 and arr[mid-1] == arr[mid]:
                # Check if length odd of half List
                if len(arr[start:mid]) % 2 == 1:
                    # go left
                    start = mid + 1
                else:
                    # go right
                    end = mid - 2

            # mid repeats in left
            elif mid + 1 < n and arr[mid] == arr[mid + 1]:
                # Check if length odd of half List
                if len(arr[start:mid]) % 2 == 1:
                    # go right
                    end = mid - 1

                else:
                    # go left
                    start = mid + 2

        return arr[start]
