def replaceEveny2(arr):

    for i in range(len(arr)):

        if i % 2 == 0:
            arr[i] = 2

    print(arr)


replaceEveny2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
