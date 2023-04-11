"""
Is ko bohot time laga bc, get closest elem by record and move on,
Then inc or dec the window!!
Keep in mind the window starts from left = closestINdex - 1 and that is why 
initially the window is empty...
If k == 1, the while loop will exeute!! So min times while loop executes is 1!!
And that is why at the end we do left+1 :right

"""


class Solution:
    def findClosestElements(self, arr: List[int], k: int, elem: int) -> List[int]:

        def record(result, mid, elem):
            if result == -1 or abs(arr[mid]-elem) < abs(arr[result]-elem):
                return mid
            return result

        def getClosestElem():
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

        closestIndex = getClosestElem()
        left, right = closestIndex-1, closestIndex

        while right - left - 1 < k:

            if left == -1:
                right += 1
                continue

            if right == len(arr) or abs(arr[left]-elem) <= abs(arr[right]-elem):
                left -= 1
            else:
                right += 1

        return arr[left+1:right]
