"""
Get maximum sum using a window of size k
First create a window of size k and get its sum
Define a max variable
Now slide the window calculating the max along side.
"""


def slidingWindowSumK(arr, k):

    # Get current sum for the window
    curr_sum = sum([arr[i] for i in range(k)])
    highest_Sum = float('-inf')

    n = len(arr)

    for i in range(n-k):
        highest_Sum = max(highest_Sum, curr_sum)
        curr_sum = curr_sum - arr[i] + arr[i+k]

    print(highest_Sum)


slidingWindowSumK([1, 5, 2, 3, 7, 1], 3)
