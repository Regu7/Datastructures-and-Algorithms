class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0
        n = len(nums) - 1
        maxi = nums[0]
        summ = 0
        while (i<=n):
            summ += nums[i] 
            maxi =max(summ,maxi)
            if summ < 0:
                summ = 0
           
            i+=1
        return maxi
            
            
            
    
                

    
        '''maxi =arr[0] 
        count = 0 
        for i in range(0,len(arr)):
            for j in range(i,len(arr)):
                count = count + arr[j]
                if count > maxi :
                    maxi = count 
            count = 0
            return maxi'''
        
    
        
