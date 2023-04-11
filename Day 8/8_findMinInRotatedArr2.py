"""
Compare the mid with last element..
1. Case 1 - arr[mid] < arr[end] 
    This means that min elem can be either mid or anythng less than mid
    Thats why we do end = mid and not end = mid - 1
2. Case 2 - arr[mid] > arr[end]
    This means that the min elem lies in mid+1 portion as mid is greater
    than the end, go right -- start = mid + 1
    Certainly mid is not the minimum elem
3. Case 3 - arr[mid] == arr[end]
    This means that mid can be anywhere now, and we dont know 
    wheere to go.. We can safely say that end = end - 1 because we
    know that arr[mid] == arr[end], even if it is the minimum
    elem, we are not missing that!!
4. In the end, we arrive at a point where mid is the minimum elem
    Then return arr[mid]!!
"""


class Solution:
    def findMin(self, arr: List[int]) -> int:
        start = 0
        end = len(arr) - 1

        while start <= end:

            mid = start + (end - start)//2

            # mid is less than end
            if arr[mid] < arr[end]:
                # go left, but instead of doing that, do
                # end = mid and not end = mid - 1
                end = mid
            elif arr[mid] > arr[end]:
                start = mid + 1
            else:
                end -= 1

        return arr[mid]
