
'''Input : arr[] = {4, 2, 2, 6, 4}, m = 6
Output : 4
Explanation : The subarrays having XOR of 
              their elements as 6 are {4, 2}, 
              {4, 2, 2, 6, 4}, {2, 2, 6},
               and {6} '''



def xxor(arr , n,k):
    count = 0 
    xor = 0
    has = {}
    for i in range(n):
        xor = arr[i] ^ xor
        
        y = xor ^ k
        if y in has.keys():
            count+= has[y]
        if xor == k :
            count+=1 
        has[xor] = has.get(xor, 0) + 1
    return count

arr = [4, 2, 2, 6, 4]
n = len(arr)
m = 6
 
print("Number of subarrays having given XOR is",
                        xxor(arr, n, m))
        
