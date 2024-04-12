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
