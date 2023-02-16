from shutil import move


def moveAllTheZeroesToTheBeginning(arr):

    partition = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            arr[partition], arr[i] = arr[i], arr[partition]
            partition += 1

    print(arr)


def moveAllTheZeroesToTheEnd(arr):

    partition = len(arr) - 1

    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 0:
            arr[partition], arr[i] = arr[i], arr[partition]
            partition -= 1

    print(arr)


moveAllTheZeroesToTheBeginning([4, 2, 0, 1, 0, 3, 0])
moveAllTheZeroesToTheEnd([4, 2, 0, 1, 0, 3, 0])
