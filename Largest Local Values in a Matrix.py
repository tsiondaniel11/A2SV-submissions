class Solution:
     def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        max_local = []
        for i in range(n - 2):
            temp_row = []
            for j in range(n - 2):
                max_value = float('-inf')
                for x in range(3):
                   for y in range(3):
                       max_value = max(max_value, grid[i + x][j + y])
                temp_row.append(max_value)
            max_local.append(temp_row)
        return max_local


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res =[[0]*(n-2) for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        res[i][j] =max(res[i][j],
                                       grid[r][c])
        return res 
