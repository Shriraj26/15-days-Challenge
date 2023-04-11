

def doesPathExist(arr):
    m = len(arr)
    n = len(arr[0])
    memo = [[None for j in range(n)] for i in range(m)]

    def oob(i, j):
        if i < 0 or j < 0 or i >= m or j >= n:
            return True
        return False

    def findPath(i, j):

        # The base cases for which path does not exist forward
        # 1. oob
        # 2. 1 at curr position
        # 3. cycle
        # 4. no path from this node
        if oob(i, j) or arr[i][j] == 1 or memo[i][j] == 'VISITING' or memo[i][j] == 'PATH_NOT_FOUND':
            return False

        # if reached dest
        if i == m-1 and j == n-1:
            return True

        memo[i][j] = 'VISITING'

        for row, col in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
            if findPath(row, col):
                return True

        memo[i][j] == 'PATH_NOT_FOUND'
        return False

    return findPath(0, 0)


tempArr = [[0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0], [1, 1, 1, 1]]
print(doesPathExist(tempArr))
