
def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows ,cols= len(matrix) , len(matrix[0])
    columnflag = True
    for i in range(rows):
        if matrix[i][0] == 0 :
            columnflag =  False
        for j in range(1,cols):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0

    for i in range(rows-1,-1,-1):
        for j in range(cols-1,0,-1):
            if (matrix[i][0] ==0 or matrix[0][j] == 0):
                matrix[i][j] = 0
        if columnflag == False :
            matrix[i][0] = 0

                
                
            