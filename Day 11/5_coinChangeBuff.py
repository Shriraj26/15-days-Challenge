
def permute(total, arr):

    buff = []

    def genPermu(arrIndex, currSum):

        # Base case
        if currSum > total:
            return
        if currSum == total:
            print(buff)
            return

        for i in range(arrIndex, len(arr)):
            buff.append(arr[i])
            genPermu(i, currSum + arr[i])
            buff.pop()

    genPermu(0, 0)


permute(5, [1, 2, 5])
