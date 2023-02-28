"""
1. Sort the array
2. Hold the first elem, then apply 2 sum on remaining parts of array so that 
when i>0 , then arr[i] != arr[i-1]
3. But this is a special case of inner 2 sum as we need to avoid duplicates so check for 
lines 30, 34 too!!
"""


def threeSum(arr):

    finalArr = []
    arr.sort()
    n = len(arr)

    for i in range(n-2):

        start = i+1
        end = n-1
        # This condition checks that we count unique triplets, and if i-1 has been included before,
        # i will not be included again as we check arr[i] != arr[i-1]
        if i == 0 or (i > 0 and arr[i] != arr[i-1]):

            # This should be start < end and not start <= end
            while start < end:

                if arr[start] + arr[end] + arr[i] == 0:
                    finalArr.append([arr[i], arr[start], arr[end]])

                    # We have an inner loop to skip duplicate elements
                    while start < end and arr[start] == arr[start+1]:
                        start += 1

                    # We have an inner loop to skip duplicate elements
                    while start < end and arr[end] == arr[end-1]:
                        end -= 1

                    # lastly just one elem ahead for start and back for end to avoid last duplicates
                    start += 1
                    end -= 1

                elif arr[start] + arr[end] + arr[i] < 0:
                    start += 1
                else:
                    end -= 1

    print(finalArr)


threeSum([-1, 0, 1, 2, -1, -4])
