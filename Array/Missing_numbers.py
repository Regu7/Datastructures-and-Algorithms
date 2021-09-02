def missing(arr):
    miss ,repeated= [], []
    b = []
    for i in range(1,len(arr)+1):
        if i not in arr:
            miss.append(i)
        if arr[i-1] in b:
            repeated.append(arr[i-1])
        else:
            b.append(arr[i-1])
    return miss,repeated

if __name__ =='__main__':
    arr= [7, 3, 4, 5, 5, 6, 2]
    a,b = missing(arr)
    print("missing numbers:" ,a ,'repeated numbers:',b)
    
    
    
    
    
    
                
        
