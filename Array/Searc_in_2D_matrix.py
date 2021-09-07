class Solution:
    
    '''def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in matrix :
            if target in i:
                return True
        return False 
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                print('hi')
                if target ==  matrix[i][0] or target == matrix[i][-1] :
                    return True
                else:
                    for j in range(0,len(matrix[0])-1):
                        if target ==  matrix[i][j]:
                            return True
        return False '''
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            n = len(matrix)
            m = len(matrix[0])
            if len(matrix ) == 0 :
                return False
            low = 0
            high = n * m -1
            
            while(low <= high ):
                mid = (low + (high - low)//2)
                if(matrix[mid//m][mid%m] ==  target):
                    return True
                if target < matrix[mid//m][mid%m] :
                    high = mid - 1
                    
                else:
                    low = mid + 1
            return False
                                
            
            
    
        
