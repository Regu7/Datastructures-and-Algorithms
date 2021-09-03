def generate(self, numRows: int) -> List[List[int]]:
        result = []
        
        if numRows < 1 :
            return result
        
        for i in range(numRows):
            row = [] 
            if  i ==  0 :
                row.append(1)
            else :
                row.insert(0,1)
                row.insert(i,1)
                for j in range(1,i):
                    leftabove = result[i-1][j-1]
                    rightabove = result[i-1][j]
                    row.insert(j ,rightabove + leftabove)
            result.append(row)
        return result
            
                    
                    
