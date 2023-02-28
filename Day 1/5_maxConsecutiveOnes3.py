"""
In this problem, u can replace at most k zeroes with ones and 
count the maximum number of consecutive ones together.

Sliding window approach - 
keep left and right , gradually increase right and if u enounter zero, decrement k
if k goes negative, start incrementing left, but also check if left has zero,
increment k
At last the window size will be max number of ones... 
For clear understanding, dry run this code
"""


def maxConsecutiveOnes(arr, k):

    start = 0
    end = 0

    for end in range(len(arr)):

        if arr[end] == 0:
            k -= 1

        if k < 0:
            if arr[start] == 0:
                k += 1

            start += 1

    return end - start + 1


print(maxConsecutiveOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))

print(maxConsecutiveOnes([0, 0, 1, 1, 0, 0, 1,
      1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
