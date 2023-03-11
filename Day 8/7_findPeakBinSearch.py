class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = (start+end)//2

            left = nums[mid-1] if mid > 0 else float('-inf')
            right = nums[mid+1] if mid < len(nums)-1 else float('-inf')

            if left <= nums[mid] <= right:
                start = mid + 1
            elif left >= nums[mid] >= right:
                end = mid - 1
            elif nums[mid] > left and nums[mid] > right:
                return mid
            else:
                # u can go left or right anything works because of more peaks!
                end = mid - 1

        return 0
