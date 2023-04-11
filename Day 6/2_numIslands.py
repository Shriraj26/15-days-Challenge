"""
Start from any one point, and do dfs
after that increase the count
Check other nodes that have not been visited, if not then recurse there
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def inRange(row, col):
            return 0 <= row < m and 0 <= col < n

        def dfsTraverse(i, j):
            grid[i][j] = '0'

            for row, col in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                if inRange(row, col) and grid[row][col] == '1':
                    dfsTraverse(row, col)

        numIslands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfsTraverse(i, j)
                    numIslands += 1

        return numIslands
