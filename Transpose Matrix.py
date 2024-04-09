class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposedmatrix = []
        col = len(matrix[0])
        row = len(matrix)
        
        for i in range(col):
            newrow = []
            for j in range(row):
                newrow.append(matrix[j][i])
            transposedmatrix.append(newrow)

        return transposedmatrix
        
